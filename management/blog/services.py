
import mimetypes
from django.conf import settings
import requests

def generate_topics(lesson_description):
    webhook_url = settings.N8N_WEBHOOK_URL

    data = {
        "task": "topics",
        "lesson_description": lesson_description,
    }
    if data:
        response = requests.post(
            webhook_url,
            data=data,
            timeout=120,
        )

    response.raise_for_status()
    payload = response.json()

    if not isinstance(payload, list) or not payload:
        raise ValueError("The webhook returned an invalid response")

    output = payload[0].get("output")

    if not isinstance(output, list):
        raise ValueError("The webhook response has not output list.")

    return output[:5]


def generate_blog(blog_questions):
    data = {
        "task": "generate_blog",
        "topic": blog_questions.generated_topic,
        "principle": blog_questions.principle,
        "question1": blog_questions.question1,
        "answer1": blog_questions.answer1,
        "question2": blog_questions.question2,
        "answer2": blog_questions.answer2,
        "question3": blog_questions.question3,
        "answer3": blog_questions.answer3,
        "question4": blog_questions.question4,
        "answer4": blog_questions.answer4,
        "question5": blog_questions.question5,
        "answer5": blog_questions.answer5,
    }

    response = requests.post(
        settings.N8N_WEBHOOK_URL,
        data=data,
        timeout=120,
    )

    response.raise_for_status()

    payload = response.json()

    # Handle N8N response 

    if isinstance(payload, list):
        if not payload:
            raise ValueError(
                "The blog webhook returned a empty list."
            )
        payload = payload[0]

    if isinstance(payload, dict) and "output" in payload:
        payload = payload["output"]

    if not isinstance(payload, dict):
        raise ValueError(
            "The blog webhook did not return a valid object."
        )

    return payload