from langchain.chat_models import init_chat_model
import os
os.environ['GOOGLE_API_KEY']="AIzaSyALvgk-DF4bGNzX7rKLy9kK3Mdu1gBH_as"

model=init_chat_model("google_genai:gemini-2.5-flash-lite")

chat_history=[]

while True:
    user_input=input("User: ")
    chat_history.append(user_input)
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI:",result.content)