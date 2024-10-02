class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description  # Descripción de la pregunta
        self.options = options  # Opciones de respuesta
        self.correct_answer = correct_answer  # Respuesta correcta

    def is_correct(self, answer):
        """Verifica si la respuesta dada es correcta"""
        return self.correct_answer == answer


class Quiz:
    def __init__(self):
        self.questions = []  # Lista de preguntas
        self.current_question_index = 0  # Índice de la pregunta actual
        self.correct_answers = 0  # Respuestas correctas
        self.incorrect_answers = 0  # Respuestas incorrectas
        self.difficulty = "Normal"  # Nivel de dificultad inicial

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            # Incrementar dificultad si el jugador responde correctamente más de 3 preguntas
            if self.correct_answers >= 3:
                self.difficulty = "Difícil"
            return True
        else:
            self.incorrect_answers += 1
            # Disminuir dificultad si el jugador falla más de 3 veces
            if self.incorrect_answers >= 3:
                self.difficulty = "Fácil"
            return False
