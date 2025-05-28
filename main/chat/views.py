from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")

        # TODO: Мұнда кейін контекст пен GPT жауабы болады
        bot_reply = f"Сіз айттыңыз: {user_message}. Жауап функционалы әлі дайын емес."

        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "POST сұранысы қажет!"}, status=400)
