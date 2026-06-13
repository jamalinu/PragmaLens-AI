import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional
from google import genai
from google.genai import types

app = FastAPI(title="PragmaLens: Advanced Discourse & Linguistic Audit Platform")

# Intentar montar el frontend (index.html)
if os.path.exists("index.html"):
    @app.get("/", response_class=HTMLResponse)
    async def read_index():
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()

# =====================================================================
# 📋 NUEVAS ESTRUCTURAS DE DATOS (JSON SCHEMAS VIA PYDANTIC)
# =====================================================================

class MaximResult(BaseModel):
    maxim: str = Field(description="Name of the Gricean maxim (Quantity, Quality, Relation, Manner)")
    status: str = Field(description="Must be either 'Fulfilled' or 'Flouted'")
    explanation: str = Field(description="Brief explanation in Spanish detailing how the maxim is handled.")

class AmbiguityItem(BaseModel):
    type: str = Field(description="Type of ambiguity found: 'Léxica' (polysemy/homonymy) or 'Sintáctica/Estructural' (amphibology)")
    segment: str = Field(description="The exact word, phrase, or sentence where the ambiguity occurs.")
    explanation: str = Field(description="Clear explanation in Spanish of why it is ambiguous and how it could be rephrased to be clearer.")

class FallacyItem(BaseModel):
    name: str = Field(description="The formal name of the logical fallacy identified (e.g., Ad Hominem, Straw Man, False Dilemma, Post Hoc).")
    segment: str = Field(description="The exact fragment of text where the fallacious argument is deployed.")
    explanation: str = Field(description="Explanation in Spanish of how the argument breaks logical validity or manipulates discourse.")

# El contenedor principal unificado
class LinguisticAuditResponse(BaseModel):
    # Módulo 1: Pragmática (Grice)
    maxims_analysis: List[MaximResult]
    implicature: str = Field(description="The uncovered, underlying meaning or conversational implicature. If none, state so.")
    
    # Módulo 2: Semántica (Ambigüedades)
    ambiguities_detected: List[AmbiguityItem] = Field(description="List of lexical or structural ambiguities found in the text. Empty list if none.")
    
    # Módulo 3: Lógica (Falacias)
    fallacies_detected: List[FallacyItem] = Field(description="List of logical fallacies or manipulative argumentation detected. Empty list if none.")
    
    # Conclusión
    global_discourse_evaluation: str = Field(description="A concise summary in Spanish (2-3 sentences) evaluating the overall quality, clarity, and cooperative nature of the text.")

# =====================================================================
# 🚀 CLIENTE DE GOOGLE GENAI
# =====================================================================
api_key = "GEMINI_API_KEY"  
client = genai.Client(api_key=api_key)

# =====================================================================
# 🔍 ENDPOINT DE ANÁLISIS UNIFICADO
# =====================================================================
class TextInput(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_discourse(payload: TextInput):
    user_text = payload.text.strip()
    if not user_text:
        raise HTTPException(status_code=400, detail="El texto no puede estar vacío.")

    # 1. Filtro local de cortesía / Fático (Fatic/Courtesy Filter)
    greetings = ["hola", "buenos dias", "buenas tardes", "buenas noches", "adios", "hasta luego", "gracias", "merci", "bonjour", "hello"]
    clean_text = "".join(c for c in user_text.lower() if c.isalnum() or c.isspace()).strip()
    
    if clean_text in greetings:
        return {
            "maxims_analysis": [
                {"maxim": "Quantity", "status": "Fulfilled", "explanation": "Fórmula fática estándar de cortesía."},
                {"maxim": "Quality", "status": "Fulfilled", "explanation": "Intercambio social genuino."},
                {"maxim": "Relation", "status": "Fulfilled", "explanation": "Apertura o cierre normal del canal comunicativo."},
                {"maxim": "Manner", "status": "Fulfilled", "explanation": "Expresión clara y directa."}
            ],
            "implicature": "No hay implicatura oculta; es una interacción fática o de cortesía estándar.",
            "ambiguities_detected": [],
            "fallacies_detected": [],
            "global_discourse_evaluation": "Intercambio fático básico y cooperativo para mantener el contacto social."
        }

    # 2. Control de conexión con la API de Google
    if not client:
        raise HTTPException(
            status_code=500, 
            detail="Error de configuración: GEMINI_API_KEY no encontrada en las variables de entorno."
        )

    # 3. Llamada estructurada a Gemini 2.5 Flash
    system_prompt = (
        "You are an expert Computational Linguist and Discourse Analyst specializing in Pragmatics, Semantics, and Logic. "
        "Analyze the user's input text dynamically across three core modules:\n"
        "1. PRAGMATICS (Grice's Maxims): Evaluate Quantity, Quality, Relation, and Manner. Determine if they are 'Fulfilled' or 'Flouted'. "
        "Extract the conversational implicature (indirect meaning) if the speaker intentionally flouts a maxim.\n"
        "2. SEMANTICS & SYNTAX (Ambiguity): Identify any Lexical Ambiguities (multiple meanings, polysemy) or Structural Ambiguities (amphibology, confusing syntax).\n"
        "3. LOGIC & ARGUMENTATION (Fallacies): Scan for any logical fallacies used to manipulate or weaken the argument (e.g., Ad Hominem, Straw Man, False Dilemma).\n\n"
        "CRITICAL: The text can be in English, Spanish, French, Arabic, Catalan, or Berber. Regardless of the input language, "
        "your text explanations inside the structured JSON properties MUST be written in Spanish."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_text,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                response_schema=LinguisticAuditResponse,
                temperature=0.2, # Baja temperatura para análisis analítico y consistente
            ),
        )
        # Gemini devuelve un string JSON perfectamente validado por el esquema
        import json
        return json.loads(response.text)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar con Gemini API: {str(e)}")
