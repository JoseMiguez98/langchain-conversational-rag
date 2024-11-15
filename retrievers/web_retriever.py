import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader, DirectoryLoader

from dotenv import load_dotenv

load_dotenv()

web_loader = WebBaseLoader(
    "https://www.promtior.ai",
    bs_kwargs=dict(
      parse_only = bs4.SoupStrainer()
    )
  )
dir_loader = DirectoryLoader("docs", glob="*.pdf")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
web_documents = web_loader.load()
dir_documents = dir_loader.load()

all_documents = web_documents + dir_documents
splits = text_splitter.split_documents(all_documents)

vecttorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vecttorstore.as_retriever()
