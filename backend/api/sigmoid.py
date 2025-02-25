import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SIGMOID_API_KEY")
SIGMOID_URL = "https://api.sigmoid.com/generate"

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "num_images": 1,
        "size": "512x512" 
        
    response = requests.post(SIGMOID_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("image_url")
    else:
        return None
