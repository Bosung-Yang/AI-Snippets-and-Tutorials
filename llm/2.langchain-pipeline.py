import getpass
import os
import dotenv
from dotenv import load_dotenv

dotenv.load_dotenv('../dotenv/.env')

from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4o-mini", model_provider="openai")

from langchain_core.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]
from langchain_core.prompts import PromptTemplate

templete = PromptTemplate.from_template("my name is {nickname}")
chain = templete | model
# 

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
chain = templete | model | output_parser

response = chain.invoke({"nickname": "John"})

print(response)