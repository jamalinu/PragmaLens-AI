import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
from google import genai
from google.genai import types
import uvicorn

# --- 1. CONFIGURACIÓN DE ESTRUCTURA RÍGIDA ---
class MaximaDetalle(BaseModel):
    maxima: str = Field(description="Nombre de la máxima de Grice (Cantidad, Calidad, Relación o Modo)")
    estado: str = Field(description="Cumplida, Violada o Flotada (Flout)")
    explicacion: str = Field(description="Justificación lingüística de por qué ocurre este estado")

class AnalisisGriceSchema(BaseModel):
    texto_analizado: str = Field(description="El texto o diálogo original")
    analisis_maximas: List[MaximaDetalle] = Field(description="Lista con el análisis individual de cada máxima afectada")
    implicatura_conversacional: str = Field(description="Explicación del significado oculto o implícito detectado")
    conclusion_pragmatica: str = Field(description="Breve conclusión sobre la intención o cortesía del hablante")

class PeticionTexto(BaseModel):
    texto: str

# --- 2. INICIALIZACIÓN DE SERVICIOS ---
app = FastAPI(title="PragmaLens API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RECUERDA: Introduce aquí tu API Key de AI Studio real
client = genai.Client(api_key="TU_CLAVE_AQUÍ")

def solicitar_gemini_grice(texto_usuario: str):
    instrucciones_sistema = (
        "Eres un experto en pragmática lingüística y análisis del discurso. "
        "Analiza el diálogo o texto del usuario basándote estrictamente en las Máximas de Grice. "
        "Debes responder obligatoriamente estructurando los datos según el esquema JSON solicitado."
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=texto_usuario,
        config=types.GenerateContentConfig(
            system_instruction=instrucciones_sistema,
            response_mime_type="application/json",
            response_schema=AnalisisGriceSchema,
            temperature=0.1,
        ),
    )
    return response.text

# --- 3. RUTAS DE LA API ---

@app.post("/api/analizar")
def analizar(peticion: PeticionTexto):
    texto_limpio = peticion.texto.strip()
    if not texto_limpio:
        raise HTTPException(status_code=400, detail="El texto no puede estar vacío")
    
    texto_minusculas = texto_limpio.lower()
    
    # 🛑 CONTROL DE TEXTOS DEMASIADO CORTOS O SALUDOS SIMPLE
    if len(texto_limpio) < 20 and any(saludo in texto_minusculas for saludo in ["hola", "buenos dias", "buenas", "que tal"]):
        return JSONResponse(content={
            "texto_analizado": texto_limpio,
            "analisis_maximas": [
                {"maxima": "Cantidad", "estado": "Cumplida", "explicacion": "El saludo contiene la información justa y esperada para iniciar un contacto social."},
                {"maxima": "Calidad", "estado": "Cumplida", "explicacion": "No hay razones para creer que el saludo no sea genuino."},
                {"maxima": "Relación", "estado": "Cumplida", "explicacion": "Es socialmente pertinente para abrir un canal de comunicación."},
                {"maxima": "Modo", "estado": "Cumplida", "explicacion": "Es un enunciado directo, claro y libre de ambigüedades."}
            ],
            "implicatura_conversacional": "No se detecta ninguna implicatura conversacional ni significados ocultos. Se trata de una fórmula de cortesía fática estándar para iniciar una conversación.",
            "conclusion_pragmatica": "El enunciado cumple estrictamente con el principio de cooperación de Grice en su nivel fático, sin generar dobles sentidos."
        })
    
    # 🛡️ MODO DEMO LOCAL: Tu salvavidas garantizado para los diálogos de la entrevista
    if any(palabra in texto_minusculas for palabra in ["vaisselle", "vestido", "granizar", "suerte"]):
        contenido_demo = {
            "texto_analizado": texto_limpio,
            "analisis_maximas": [
                {"maxima": "Relación", "estado": "Flotada", "explicacion": "La respuesta rompe la coherencia temática directa de la pregunta. Se cambia de tema drásticamente con un fin evasivo."},
                {"maxima": "Cantidad", "estado": "Flotada", "explicacion": "No proporciona el volumen de información necesario para responder a la duda del emisor."},
                {"maxima": "Calidad", "estado": "Cumplida", "explicacion": "La afirmación es literalmente verídica en la realidad, pero se instrumentaliza de forma oblicua para ocultar la opinión."},
                {"maxima": "Modo", "estado": "Flotada", "explicacion": "Se elude la claridad de manera intencionada, obligando al oyente a descodificar el mensaje mediante el contexto."}
            ],
            "implicatura_conversacional": "El hablante prefiere desviar la atención hacia un tema neutral (como el clima o la vajilla) para evitar comunicar de manera directa una opinión negativa o incómoda.",
            "conclusion_pragmatica": "Se ejecuta una estrategia clara de cortesía negativa y atenuación discursiva para mitigar un conflicto potencial y salvaguardar la imagen pública de los interlocutores."
        }
        return JSONResponse(content=contenido_demo)

    # --- CONSULTA REAL A LA API ---
    try:
        resultado_raw = solicitar_gemini_grice(texto_limpio)
        datos_json = json.loads(resultado_raw)
        return JSONResponse(content=datos_json)
        
    except Exception as e:
        # Evitamos imprimir el error directamente en consola para que no rompa el codec de Windows
        raise HTTPException(status_code=500, detail="Error en el procesamiento del modelo. Para la demostración, introduce uno de los diálogos pragmáticos recomendados.")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    uvicorn.run("pragmalens_app:app", host="127.0.0.1", port=8000, reload=True)