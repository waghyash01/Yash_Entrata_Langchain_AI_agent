import os
from retriever import get_context
from vector_store import build_vector_store, retrieve_context

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from models import Quiz
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

structured_llm = llm.with_structured_output(Quiz)



prompt = ChatPromptTemplate.from_template("""
You are an expert educational quiz generator.

Use ONLY the following context to generate questions:

{context}

Topic: {topic}

Rules:
- Generate exactly 5 multiple-choice questions
- Each question must have 4 options (A, B, C, D)
- Only one correct answer
- Include a short explanation
- Return structured output only
""")


chain = prompt | structured_llm


def generate_quiz(topic: str):

    
    vector_db = build_vector_store(topic)

    context = retrieve_context(vector_db, topic)

    # debug
    print("retrieved context")

    return chain.invoke({
        "topic": topic,
        "context": context
    })
