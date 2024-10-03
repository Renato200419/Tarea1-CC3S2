class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = str(correct_answer).strip()  # Convertir a string para comparación uniforme

    def is_correct(self, answer):
        # Comparar como strings para evitar diferencias de tipo
        return str(answer).strip() == self.correct_answer

class Quiz:
    def __init__(self):
        self.questions = []  # Lista de preguntas
        self.current_question_index = 0  # Índice de la pregunta actual
        self.correct_answers = 0  # Respuestas correctas
        self.incorrect_answers = 0  # Respuestas incorrectas
        self.difficulty = "Normal"  # Nivel de dificultad inicial
        self.answers = []  # Registrar las respuestas del usuario

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        # Convertir el input del usuario a la opción correspondiente
        try:
            selected_option = int(answer) - 1  # Convertir el número a índice de lista
            self.answers.append(selected_option)  # Registrar el índice de la opción seleccionada
            if question.options[selected_option] == question.correct_answer:
                self.correct_answers += 1
                if self.correct_answers >= 3:
                    self.difficulty = "Difícil"
                return True
            else:
                self.incorrect_answers += 1
                if self.incorrect_answers >= 3:
                    self.difficulty = "Fácil"
                return False
        except (ValueError, IndexError):
            print("Entrada no válida. Inténtalo de nuevo.")
            return False
