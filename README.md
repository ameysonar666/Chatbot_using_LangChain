Introduction
This project is a simple chatbot built using LangChain and Google's Gemini model.  
It is designed to solve one of the most basic problems of Large Language Models (LLMs) — **they do not remember previous conversations**.

Problem Statement
Most LLMs are stateless, meaning:
*They do not remember past interactions
*Every response is independent
* Conversations lack continuity

# Solution
This chatbot overcomes this problem in the **easiest possible way** by maintaining a chat history.

Instead of sending only the latest message, the program:
- Stores all previous messages in a list (`chat_history`)
- Sends the entire conversation to the model every time
- Allows the model to respond with context
