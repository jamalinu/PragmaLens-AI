Markdown
# 🔍 PragmaLens: Advanced Discourse Audit Platform

**PragmaLens** es una herramienta web avanzada de auditoría lingüística y pragmática diseñada para analizar de manera unificada la coherencia, la claridad y la validez lógica de discursos, diálogos y textos complejos. 

Combinando fundamentos teóricos de la lingüística con modelos de inteligencia artificial de última generación (**Gemini API**), la plataforma deconstruye las capas analíticas del lenguaje para identificar cómo nos comunicamos, dónde fallamos y de qué manera se manipula la información.

---

## 🎯 Características Principales (Estructura Modular)

La plataforma opera bajo un enfoque modular analizando tres pilares lingüísticos clave:

### 1. 💬 Módulo Pragmático (Principio de Cooperación de Grice)
* **Máximas Lingüísticas:** Evalúa el cumplimiento o flote (*flouting*) de las cuatro máximas conversacionales de Paul Grice: **Cantidad, Cualidad, Relación y Modalidad**.
* **Implicaturas Conversacionales:** Extrae el significado oculto, las intenciones indirectas o el subtexto, procesando dinámicamente ironías, metáforas y respuestas evasivas.

### 2. ⚠️ Módulo Semántico (Detección de Ambigüedades)
* **Ambigüedad Léxica:** Identifica problemas de polisemia u homonimia donde un término confunde el sentido del mensaje.
* **Ambigüedad Sintáctica (Anfibología):** Detecta estructuras frasales defectuosas que abren la puerta a múltiples interpretaciones erróneas.

### 3. 🔨 Módulo Lógico (Falacias Argumentativas)
* **Auditoría de Discurso:** Localiza y aísla segmentos específicos del texto que incurren en vicios lógicos y trampas retóricas habituales (ej. *Ad Hominem*, *Falso Dilema*, *Pendiente Resbaladiza*).
* **Análisis Crítico:** Ofrece una explicación rigurosa de por qué el argumento carece de validez formal.

---

## 🌐 Capacidades Multilingües Avanzadas
Gracias a su herencia filológica, **PragmaLens** está diseñado para auditar textos que combinan múltiples idiomas de manera fluida (cambios de código o *code-switching*). Sólido soporte analítico en:
* **Berber (Tamazight)**
* **Árabe**
* **Catalán**
* **Español**
* **Francés**
* **Inglés**

---

## 🛠️ Stack Tecnológico

* **Backend:** FastAPI (Python 3.13)
* **Core IA:** Google GenAI SDK (Modelos Gemini)
* **Frontend:** HTML5, JavaScript (Fetch API / Promesas asíncronas), Tailwind CSS (Interfaz moderna con UI oscura).
* **Despliegue:** Hugging Face Spaces.

---

## 🚀 Instalación y Ejecución en Local

Si deseas probar o auditar la aplicación en tu propio entorno:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/Pragmalens-AI.git](https://github.com/TU_USUARIO/Pragmalens-AI.git)
   cd Pragmalens-AI
Instalar dependencias:

Bash
pip install fastapi uvicorn google-genai
Configurar la API Key:
Establece tu credencial de Google AI Studio en tus variables de entorno:

En Windows (PowerShell): $env:GEMINI_API_KEY="tu_clave_aquí"

En Linux/Mac: export GEMINI_API_KEY="tu_clave_aquí"

Arrancar el servidor de desarrollo:

Bash
uvicorn pragmalens_app:app --reload
Abre tu navegador en http://127.0.0.1:8000.
