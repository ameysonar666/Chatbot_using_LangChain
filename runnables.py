from langchain.chat_models import init_chat_model
import os 
os.environ['GOOGLE_API_KEY']="AIzaSyARomTa0GNb5bEGbVZeynkboSC0GqE8fSU"
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



prompt_A = PromptTemplate(
    template="make a joke on the topic {topic}", 
    input_variables=['topic']
)

prompt_B=PromptTemplate(template="explain the joke in 2-3 lines {joke}", input_variables=['joke'])

parser = StrOutputParser()

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

chain = prompt_A | model | parser | prompt_B | model | parser

result = chain.invoke({'topic': 'AI'})
print(result)