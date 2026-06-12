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

---

## 📁 Repository Structure

```text
├── pragmalens_app.py   # FastAPI backend, local routing, and Gemini API integration
├── index.html          # Dynamic frontend UI styled with Tailwind CSS
├── requirements.txt    # Application dependencies and libraries
└── .gitignore          # Safeguard for environment files and local caches
