import pandas as pd
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

load_dotenv()

df = pd.read_csv("documents/products_completed_fully_translated_en.csv", sep=";")

docs = []

for _, r in df.iterrows():
    content = (
        f"{r['product_name']} | " 
        f"{r['category']} |"
        f"{r['cost_price']} |"
        f"{r['store_recommendation']} |"
        f"{r['community_recommendation']} |"
        f"{r['product_description']} "
    )
    docs.append(Document(page_content=content, metadata={"sku_id":r["sku_id"]}))

embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
faiss_index = FAISS.from_documents(docs, embeddings)

faiss_index.save_local("faiss_index")

print("VectorStore save")