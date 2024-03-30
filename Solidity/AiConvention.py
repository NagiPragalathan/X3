# chatapp/views.py

from django.http import JsonResponse
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

text_data = """
VAR counter = 0
FUN inc(num)
    VAR counter = counter + 1
END
FUN dec(num)
    VAR counter = counter - 1
END

"""

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
llm = ChatOpenAI(api_key=api_key)
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a helpful AI to converting pseudo code into perfect solidity."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template(text_data)
    ]
)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
conversation = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)
sample = conversation.predict(input="""give me the solidity code for this pseudocode dicler all of lisince and remove all of the print statements and give me the solidity code""")

print(sample)



