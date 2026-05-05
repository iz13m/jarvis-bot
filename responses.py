from datetime import datetime

def get_response(message):
    message = message.lower().strip()

    if "good morning" in message:
        return "Good morning! Ready to conquer the day?"

    elif "good evening" in message:
        return "Good evening! Time to relax and recharge."

    elif "good afternoon" in message:
        return "Good afternoon!"

    elif "what is today?" in message:
        today = datetime.now()
        day_name = today.strftime("%A")
        return f"Today is {day_name}"

    else:
        return "Sorry, I don't understand that yet."


print(get_response("what is today?"))