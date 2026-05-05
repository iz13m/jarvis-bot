def get_response(message):
    message = message.lower().strip()

    if "good morning" in message:
        return "Good morning! Ready to conquer the day?"

    elif "good evening" in message:
        return "Good evening! Time to relax and recharge."

    elif "good afternoon" in message:
        return "good after noon."
  
    elif "What is today?":
        return "Today is a great day!"
  
    else:
        return "Sorry, I don't understand that yet."