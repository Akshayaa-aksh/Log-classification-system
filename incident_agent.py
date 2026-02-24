import json
import requests
import re


class IncidentAgent:

    def __init__(self, aggregator):
        self.aggregator = aggregator
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "llama3"   # You already have this installed

    def generate_incident_report(self):

        top_errors = self.aggregator.get_top_frequent()
        high_severity_logs = self.aggregator.get_high_severity_logs()
        spikes = self.aggregator.detect_spike()

        prompt = self.build_prompt(top_errors, high_severity_logs, spikes)

        try:
            response = requests.post(
                self.ollama_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
        except Exception as e:
            return f"⚠️ Failed to connect to Ollama: {str(e)}"

        result = response.json()
        print("DEBUG RESPONSE:", result)

        # Handle possible response structures
        if "response" in result:
            raw_output = result["response"].strip()
        elif "message" in result and "content" in result["message"]:
            raw_output = result["message"]["content"].strip()
        elif "error" in result:
            return f"⚠️ Ollama Error: {result['error']}"
        else:
            return f"⚠️ Unexpected Ollama response format: {result}"

        # Remove markdown formatting if present
        raw_output = raw_output.replace("```json", "")
        raw_output = raw_output.replace("```", "").strip()

        # Extract JSON block using regex
        json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)

        if not json_match:
            return f"⚠️ Could not extract JSON from response:\n{raw_output}"

        json_text = json_match.group(0)

        # Validate JSON
        try:
            parsed_json = json.loads(json_text)
            return json.dumps(parsed_json, indent=2)
        except json.JSONDecodeError:
            return f"⚠️ Extracted invalid JSON:\n{json_text}"

    def build_prompt(self, top_errors, high_severity_logs, spikes):

        return f"""
You are a strict JSON generator.

Analyze the log data below and return ONLY valid JSON.

Top Frequent Errors:
{top_errors}

High Severity Logs:
{high_severity_logs}

Spikes Detected:
{spikes}

Rules:
- Output must be valid JSON
- No explanations
- No markdown
- No extra text
- No commentary

Output format:

{{
  "incidentSummary": "...",
  "rootCauseGuess": "...",
  "recommendedAction": "..."
}}
"""