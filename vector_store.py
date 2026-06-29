from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from retriever import get_context
from config import GOOGLE_API_KEY


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY
)


def build_vector_store(topic: str):

    text = get_context(topic)

    if not text:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = splitter.create_documents([text])

    vector_store = FAISS.from_texts(
        [doc.page_content for doc in documents],
        embedding=embeddings
    )

    return vector_store


def retrieve_context(vector_store, query: str):

    if vector_store is None:
        return ""

    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    docs = retriever.invoke(query)

    return "\n".join([d.page_content for d in docs])