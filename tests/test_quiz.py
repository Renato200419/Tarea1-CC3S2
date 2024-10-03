from app.models import Quiz, Question

def test_quiz_difficulty_increase():
    # Prueba para verificar que la dificultad cambia a "Difícil" después de 3 respuestas correctas
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    for _ in range(4):  # Responder correctamente más de 3 preguntas
        quiz.add_question(question)
        quiz.answer_question(question, "4")
    assert quiz.difficulty == "Difícil"

def test_quiz_difficulty_decrease():
    # Prueba para verificar que la dificultad cambia a "Fácil" después de 3 respuestas incorrectas
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    for _ in range(4):  # Responder incorrectamente más de 3 preguntas
        quiz.add_question(question)
        quiz.answer_question(question, "3")  # Respuesta incorrecta
    assert quiz.difficulty == "Fácil"

def test_quiz_correct_and_incorrect_answers():
    # Prueba para validar el conteo de respuestas correctas e incorrectas
    quiz = Quiz()
    question = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    quiz.add_question(question)

    # Responder correctamente
    quiz.answer_question(question, "4")
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0

    # Responder incorrectamente
    quiz.answer_question(question, "3")
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 1

def test_quiz_flow_of_questions():
    # Prueba para validar el flujo correcto de preguntas en el quiz
    quiz = Quiz()
    question1 = Question("What is 2 + 2?", ["1", "2", "3", "4"], "4")
    question2 = Question("What is the capital of France?", ["Berlin", "London", "Paris", "Madrid"], "Paris")
    quiz.add_question(question1)
    quiz.add_question(question2)

    # Validar que las preguntas se presentan en el orden correcto
    next_question = quiz.get_next_question()
    assert next_question == question1
    next_question = quiz.get_next_question()
    assert next_question == question2
    # Verificar que no quedan más preguntas
    next_question = quiz.get_next_question()
    assert next_question is None
