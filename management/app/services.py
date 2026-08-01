
import mimetypes
from django.conf import settings
import requests

def generate_post(image, name, date, lesson, facebook, instagram, linkedin, tiktok, imagewithpost):

    
    webhook_url = settings.N8N_WEBHOOK_URL

    data = {
        "task": "smpost",
        "name": name,
        "date": date,
        "lesson": lesson,
        "facebook": facebook,
        "linkedin": linkedin,
        "instagram": instagram,
        "tiktok": tiktok,
        "imagewithpost": imagewithpost,
    }
    if image and image.name:
        content_type, _ = mimetypes.guess_type(image.name)
        with image.open("rb") as image_file:
            files = {
                "image": (
                    image.name,
                    image_file,
                    content_type or "applicaton/octet-stream",
                )
            }

            response = requests.post(
                webhook_url,
                data=data,
                files=files,
                timeout=120,
            )

    else:
        response = requests.post(
            webhook_url,
            data=data,
            timeout=120,
        )

    response.raise_for_status()

    try: 
         return response.json()
    except requests.exceptions.JSONDecodeError:
        return {
            "status_code": response.status_code, 
            "body": response.text
            }