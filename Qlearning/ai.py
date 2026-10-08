import os
import json
from google import genai


def generate_learning_content(topic, age):

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert educational storyteller.

Create an engaging learning lesson for a {age}-year-old child.

Topic:
{topic}

Requirements:

1. Create a fun, age-appropriate story that teaches the topic.
2. Use simple language suitable for a {age}-year-old.
3. Include characters and a small adventure.
4. Make sure the educational concept is scientifically or mathematically correct.
5. The story should actually teach the concept.
6. Create exactly 5 multiple-choice questions.
7. Each question must have exactly 4 options.
8. Questions must test understanding of the topic, not memorization of the story.
9. Give the correct answer for every question.
10. Return ONLY valid JSON.

Use exactly this structure:

{{
    "title": "Story title",
    "story": "Complete story here",
    "questions": [
        {{
            "question": "Question here",
            "options": {{
                "A": "Option A",
                "B": "Option B",
                "C": "Option C",
                "D": "Option D"
            }},
            "answer": "A"
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