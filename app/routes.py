# app/routes.py

from fastapi import FastAPI
from pydantic import BaseModel
from .models import Question  # Importar solo Question, ya que Quiz no se usa en las rutas.

# Crear la instancia de la aplicación FastAPI
app = FastAPI()

# Base de datos temporal en memoria para almacenar preguntas
questions_db = []


class QuestionCreate(BaseModel):
    """Estructura de datos para la creación de preguntas a través de la API."""
    description: str
    options: list
    correct_answer: str


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del juego Trivia"}


@app.post("/questions/")
def create_question(question: QuestionCreate):
    # Crear una nueva pregunta y agregarla a la base de datos en memoria
    new_question = Question(question.description, question.options, question.correct_answer)
    questions_db.append(new_question)
    return {"description": new_question.description, "correct_answer": new_question.correct_answer}


@app.get("/questions/")
def get_questions():
    # Retornar todas las preguntas almacenadas en la base de datos
    return [{"description": q.description, "options": q.options, "correct_answer": q.correct_answer} for q in questions_db]
