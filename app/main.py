# app/main.py
from models import Quiz, Question

def run_quiz():
    quiz = Quiz()

    # Aquí se cargarían las preguntas, por ejemplo:
    question1 = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    question2 = Question("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris")

    # Agregar las preguntas al quiz
    quiz.add_question(question1)
    quiz.add_question(question2)

    # Lógica del juego
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(question.description)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}) {option}")
            answer = input("Tu respuesta: ")
            if quiz.answer_question(question, answer):
                print("¡Correcto!")
            else:
                print("Incorrecto.")
        else:
            break

    print(f"Juego terminado. Respuestas correctas: {quiz.correct_answers}, incorrectas: {quiz.incorrect_answers}")

# Ejecutar el juego si este archivo es el principal
if __name__ == "__main__":
    run_quiz()
