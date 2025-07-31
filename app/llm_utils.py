import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
You are an assistant helping process meeting transcripts.

Transcript:
\"\"\"
{transcript}
\"\"\"

Please extract:
1. A bullet-point list of DECISIONS made.
2. A bullet-point list of ACTION ITEMS (with names if mentioned).

Format:
Decisions:
- ...
Action Items:
- ...
"""

def extract_meeting_data(transcript: str):
    prompt = PROMPT_TEMPLATE.format(transcript=transcript)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512
    )
    content = response['choices'][0]['message']['content']

    # Parse content
    decisions = []
    action_items = []
    section = None
    for line in content.splitlines():
        if line.strip().lower().startswith("decisions:"):
            section = "decisions"
            continue
        if line.strip().lower().startswith("action items:"):
            section = "action_items"
            continue
        if line.strip().startswith("- "):
            if section == "decisions":
                decisions.append(line.strip()[2:])
            elif section == "action_items":
                action_items.append(line.strip()[2:])
    return decisions, action_items
