#Chat-BOT Using

import datetime
import time

name = input("Enter name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning " , name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon", name)
elif 17 <= presentHour <= 20:
    print("Good Evening", name)
else:
    print("Good Night", name)


print("Namastee! Welcome to Your ChatBOT")
print("--You can ask basic questions?--")

responses = {
    "hello" : "HI, Welcome iam here to help you..",
    "how are you" : "Iam fine",
    "who are you" : "Iam Chat-bot",
    "motivate me" : "Keep going..YOu will acheive",
    "happy" : "Great"
}

happy_word = ["happy","good","awesome","fanstatic"]
sad_word = ["sad","bad","upset","cry","angry"]

def getResponseOfbot(userQuestion):
    userQuestion = userQuestion.lower()

    for word in happy_word:
        if word in userQuestion:
            return "Thats's great ALL THE BEST"
    
    for word in sad_word:
        if word in userQuestion:
            return "I'm Sorry"
        
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I Don't Know"



while True:
        
    userInput = input("Please ask your question:")

    print("Bot is typing...")
    time.sleep(2)

    reply = getResponseOfbot(userInput)
    print("Bot response: ", reply)

    if "bye" in  userInput.lower():
        break