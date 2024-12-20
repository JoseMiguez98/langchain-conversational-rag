
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from retrievers.web_retriever import retriever

from dotenv import load_dotenv

load_dotenv()

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini")
history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
