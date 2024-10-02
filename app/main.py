# app/main.py
from models import Quiz, Question

def run_quiz():
    # Mensaje de bienvenida y explicación
    print("\033[1m\033[94mBienvenido al Juego de Trivia!\033[0m")
    print("\033[93mResponde las siguientes preguntas seleccionando el número de la opción correcta.\033[0m\n")

    # Crear una instancia de Quiz
    quiz = Quiz()

    # Cargar preguntas de ejemplo (pueden ser cargadas desde una base de datos en una versión más avanzada)
    question1 = Question("Cuánto es 2 + 2?", ["1", "2", "3", "4"], "4")
    question2 = Question("Cuál es la capital de Francia?", ["Berlín", "Londres", "París", "Madrid"], "París")
    question3 = Question("Cuál es el planeta más grande?", ["Tierra", "Marte", "Júpiter", "Saturno"], "Júpiter")

    # Agregar preguntas al Quiz
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)

    # Lógica del juego con manejo de rondas
    while quiz.current_question_index < 10:
        question = quiz.get_next_question()
        if question:
            print(f"\033[1m\nPregunta {quiz.current_question_index + 1}: {question.description}\033[0m")
            for idx, option in enumerate(question.options):
                print(f"  {idx + 1}. {option}")
            answer = input("Tu respuesta (ingresa el número de la opción): ")
            if quiz.answer_question(question, answer):
                print("\033[92m¡Correcto!\033[0m")  # Mensaje en verde para correcto
            else:
                print("\033[91mIncorrecto.\033[0m")  # Mensaje en rojo para incorrecto
        else:
            break


# Ejecutar el juego si este archivo es el principal
if __name__ == "__main__":
    run_quiz()
