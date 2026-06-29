from typing import Literal
from pydantic import BaseModel


class Options(BaseModel):
    A: str
    B: str
    C: str
    D: str


class Question(BaseModel):
    question: str
    options: Options
    correct_answer: Literal["A", "B", "C", "D"]
    explanation: str


class Quiz(BaseModel):
    questions: list[Question]