import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

EMAIL_PROMPT = """
Given the following meeting transcript, decisions, and action items, draft a concise, professional follow-up email to attendees. Focus on clarity and actionable next steps.

Transcript:
\"\"\"
{transcript}
\"\"\"

Decisions:
{decisions}

Action Items:
{action_items}

Email:
"""

def generate_follow_up_email(transcript: str, decisions: list, action_items: list) -> str:
    prompt = EMAIL_PROMPT.format(
        transcript=transcript,
        decisions="\n".join(f"- {d}" for d in decisions),
        action_items="\n".join(f"- {a}" for a in action_items)
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=350
    )
    email = response['choices'][0]['message']['content']
    return email.strip()
