from models import Quiz, Question

def run_quiz():
    # Mensaje de bienvenida y explicación
    print("\033[1m\033[94mBienvenido al Juego de Trivia!\033[0m")
    print("\033[93mResponde las siguientes preguntas seleccionando el número de la opción correcta.\033[0m\n")

    # Crear una instancia de Quiz
    quiz = Quiz()

    # Cargar preguntas de ejemplo
    question1 = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    question2 = Question("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris")
    question3 = Question("What is the largest planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter")

    # Agregar preguntas al Quiz
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)

    # Lógica del juego con manejo de rondas
    while quiz.current_question_index < len(quiz.questions):
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

    # Mostrar resultados al final del juego
    print("\033[1m\nJuego terminado.\033[0m")
    print(f"\033[96mPreguntas contestadas: {quiz.current_question_index}\033[0m")
    print(f"\033[92mRespuestas correctas: {quiz.correct_answers}\033[0m")
    print(f"\033[91mRespuestas incorrectas: {quiz.incorrect_answers}\033[0m\n")

    # Resumen detallado de respuestas correctas e incorrectas
    print("\033[1mResumen de respuestas:\033[0m")
    for idx, question in enumerate(quiz.questions):
        user_answer_index = quiz.answers[idx]  # Obtener el índice de la respuesta seleccionada por el usuario
        user_answer = question.options[user_answer_index]  # Obtener la respuesta seleccionada a partir del índice
        correct_or_not = "Correcto" if question.is_correct(user_answer) else "Incorrecto"
        color = "\033[92m" if correct_or_not == "Correcto" else "\033[91m"
        print(f"Pregunta {idx + 1}: {question.description} - {color}{correct_or_not}\033[0m")

# Ejecutar el juego si este archivo es el principal
if __name__ == "__main__":
    run_quiz()
