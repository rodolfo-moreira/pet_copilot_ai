from langchain.tools import BaseTool
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from pydantic import PrivateAttr
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class SearchProductsByDescription(BaseTool):

    _vectorstore: FAISS = PrivateAttr()

    name: str = "SearchProductsByDescription"
    description: str = """
    Find pet products based in the categories (ex: Best Shampoo for dogs with a sensible skin, interacves toys for babie cats, 5 best products for dogs dental clean)
    The input most have a clear sentence with the desire product.
    Return 5 products with name, price and a short description.
    """

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        self._vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    def _run(self, input: str, max_retries: int = 1):

        results = self._search_products(input)
        return results

    
    def _search_products(self, input: str, max_retries: int = 1):

        matches = self._vectorstore.similarity_search(input, k=10)

        context = "\n ".join([m.page_content for m in matches])

        prompt_text = """
            Your are an assistant that helps pet caregivers find the best products.

            Database (only these line exist):

            {context}

            User said: "{input}"

            Task:
            - Return up to 5 products stricly from the database above.
            - For each products provide: product_name, category, price and a short description.
            - Do not invent products that are not in the database
        """

        prompt = PromptTemplate(
            input_variables=["input", "context"],
            template=prompt_text
        )

        llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

        chain = prompt | llm
        answer = chain.invoke({"input": input, "context": context}).content
        return answer