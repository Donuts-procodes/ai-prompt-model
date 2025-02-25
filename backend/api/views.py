from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sigmoid import generate_image

@csrf_exempt
def generate_prompt_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get("prompt", "")

        if not prompt:
            return JsonResponse({"error": "No prompt provided"}, status=400)

        image_url = generate_image(prompt)
        if image_url:
            return JsonResponse({"image_url": image_url})
        return JsonResponse({"error": "Failed to generate image"}, status=500)
    
    return JsonResponse({"error": "Invalid request"}, status=400)
