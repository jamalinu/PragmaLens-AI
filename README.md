# PragmaLens: AI-Powered Pragmatics & Gricean Maxims Analyzer

**PragmaLens** is a Computational Linguistics web application that bridges the gap between formal linguistic theory and modern Artificial Intelligence. Built using **FastAPI** and powered by the **Gemini 2.5 Flash** model via the Google GenAI SDK, this tool automates the detection of conversational implicatures by analyzing dialogue through the lens of **H. P. Grice’s Cooperative Principle**.

While traditional Natural Language Processing (NLP) models excel at semantic and syntactic analysis, they often struggle with **pragmatics**—the meaning derived from context, social nuances, and what is left unsaid. **PragmaLens** solves this by evaluating how speakers intentionally flout conversational maxims to convey indirect meanings.

---

## 🚀 Key Features

* **Real-Time Pragmatic Analysis:** Leverages Gemini 2.5 Flash to decode complex human interactions, subtext, irony, and evasive maneuvers.
* **Gricean Maxims Breakdown:** Evaluates inputs against the four core maxims: **Quantity, Quality, Relation, and Manner**, instantly flagging whether each is *Fulfilled* (Cumplida) or *Flouted* (Flotada).
* **Conversational Implicature Extraction:** Dynamically isolates the hidden meaning or "true intent" behind the dialogue.
* **Fatic/Courtesy Filter (Cost Optimization):** Implements an intelligent local gateway to catch simple greetings (*e.g., "Hola, buenos días"*), immediately marking them as fulfilled to prevent redundant LLM API calls.
* **Asynchronous Local Demo Mode:** Includes hardcoded fallback scenarios (*e.g., historical pragmatic examples in Spanish and French*) to demonstrate lightning-fast UI rendering and offline reliability.
* **Strict JSON Schema Enforcement:** Utilizes `Pydantic` structures to ensure the LLM output matches the strict, typed interface required by the frontend with 100% predictability.

---

## 🛠️ Tech Stack & Architecture

* **Backend:** Python 3, FastAPI (Asynchronous REST API)
* **AI Integration:** Google GenAI SDK (`google-genai`), Gemini 2.5 Flash
* **Data Validation:** Pydantic (Structured JSON Outputs)
* **Frontend:** Semantic HTML5, Tailwind CSS, JavaScript (Fetch API / Async-Await)



📁 Repository Structure


├── pragmalens_app.py   # FastAPI backend, local routing, and Gemini API integration
├── index.html          # Dynamic frontend UI styled with Tailwind CSS
├── requirements.txt    # Application dependencies and libraries
└── .gitignore          # Safeguard for environment files and local caches
Setup and Installation
Clone the repository:

Bash
git clone [https://github.com/jamalinu/PragmaLens-AI.git](https://github.com/jamalinu/PragmaLens-AI.git)
cd PragmaLens-AI
Install dependencies:

Bash
pip install -r requirements.txt
Set up your API Key:
The application securely fetches the Gemini API key from your environment variables. Set it up in your terminal:

Windows (PowerShell): $env:GEMINI_API_KEY="your_api_key_here"

Linux/macOS: export GEMINI_API_KEY="your_api_key_here"

Run the local server:

Bash
uvicorn pragmalens_app:app --reload
Open your browser and navigate to http://127.0.0.1:8000 to run the application.

🧠 Linguistic Context: The Gricean Framework
In linguistic pragmatics, Grice's Maxims represent the unspoken rules of cooperative human conversation:

Quantity: Make your contribution as informative as required.

Quality: Do not say what you believe to be false or lack adequate evidence for.

Relation: Be relevant.

Manner: Be perspicuous, avoid obscurity and ambiguity.

When a speaker flouts a maxim, they are not necessarily lying; they are subtly inviting the listener to look for a deeper meaning (Implicature). PragmaLens makes this intricate cognitive process visible through code.
