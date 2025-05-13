import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")
IMAGE_URL = os.getenv("IMAGE_URL")
CAPTION = os.getenv("CAPTION")

def post_image():
    # Etapa 1: Criar contêiner de mídia
    media_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media"
    media_payload = {
        'image_url': IMAGE_URL,
        'caption': CAPTION,
        'access_token': ACCESS_TOKEN
    }
    media_response = requests.post(media_url, data=media_payload)
    media_json = media_response.json()

    if 'id' not in media_json:
        print("Erro ao criar contêiner:", media_json)
        return

    creation_id = media_json['id']

    # Etapa 2: Publicar o contêiner
    publish_url = f"https://graph.facebook.com/v19.0/{IG_USER_ID}/media_publish"
    publish_payload = {
        'creation_id': creation_id,
        'access_token': ACCESS_TOKEN
    }
    publish_response = requests.post(publish_url, data=publish_payload)
    print("Resultado da publicação:", publish_response.json())

if __name__ == "__main__":
    post_image()
