import httpx
from fastapi.testclient import TestClient
from app.main import app  # Esta línea ajusta esta importación si `main.py` está en otra ubicación

# Crear un cliente de pruebas para la aplicación FastAPI
client = TestClient(app)

def test_create_question():
    """Prueba para verificar la creación de una pregunta en la API."""
    # Datos de la pregunta que se enviará en la solicitud POST
    question_data = {
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    }
    
    # Realizar una solicitud POST para crear una nueva pregunta
    response = client.post("/questions/", json=question_data)
    
    # Verificar que la respuesta tenga un código de estado 201 (creado)
    assert response.status_code == 201
    # Verificar que los datos de la respuesta coincidan con los de la pregunta enviada
    response_data = response.json()
    assert response_data["description"] == question_data["description"]
    assert response_data["correct_answer"] == question_data["correct_answer"]

def test_get_questions():
    """Prueba para verificar la obtención de preguntas desde la API."""
    # Realizar una solicitud GET para obtener la lista de preguntas
    response = client.get("/questions/")
    
    # Verificar que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200
    # Verificar que la lista de preguntas no esté vacía
    assert len(response.json()) > 0
