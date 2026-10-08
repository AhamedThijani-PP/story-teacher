import os
import json
from google import genai


def generate_learning_content(topic, age):

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
Create an engaging educational story for a child of age {age} about:
{topic}

The story must teach the concept naturally through an adventure.
Use simple, age-appropriate language.

After the story, create exactly 5 multiple-choice questions.

For each question provide:
- question
- 4 options: A, B, C, D
- correct answer
- a short, simple explanation of WHY the correct answer is correct

The explanations must be suitable for a child of age {age}.
If a child chooses the wrong answer, the explanation should help them
understand the concept rather than simply saying they are wrong.

Return ONLY valid JSON in this exact structure:

{{
    "title": "Story title",
    "story": "The complete story",
    "questions": [
        {{
            "question": "Question text",
            "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            }},
            "answer": "B",
            "explanation": "Simple explanation of why B is correct."
        }}
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    text = response.text

    # Remove markdown code fences if Gemini adds them
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)