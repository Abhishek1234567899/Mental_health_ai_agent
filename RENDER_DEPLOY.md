# Render Deployment Instructions for Abhishek AI Mental Health Assistant

This file contains the essential steps and files needed to deploy your Streamlit + FastAPI app on Render.com.

## 1. Required Files

- `frontend.py` (Streamlit app)
- `backend/` (FastAPI backend, e.g., `main.py`, `ai_agent.py`, etc.)
- `pyproject.toml` (project dependencies)
- `requirements.txt` (for Render compatibility)
- `render.yaml` (Render build and service configuration)

## 2. Create requirements.txt
Render needs a `requirements.txt` for Python web services. Generate it from your current environment:

```
uv pip freeze > requirements.txt
```
Or manually add main dependencies:
```
streamlit
fastapi
uvicorn
requests
pydantic
# Add any other packages you use (e.g., google-generativeai, twilio, etc.)
```

## 3. Create render.yaml
This file tells Render how to build and run your services.

```
services:
  - type: web
    name: backend
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn backend.main:app --host 0.0.0.0 --port 8000"
    plan: free
    envVars:
      - key: OPENAI_API_KEY
        value: <your-openai-api-key>
      - key: GEMINI_API_KEY
        value: <your-gemini-api-key>

  - type: web
    name: frontend
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "streamlit run frontend.py --server.port 10000 --server.address 0.0.0.0"
    plan: free
    envVars:
      - key: BACKEND_URL
        value: "https://<your-backend-service-name>.onrender.com/ask"
```

## 4. Environment Variables
- Never hardcode API keys in code. Use Render's dashboard or `render.yaml` to set them.

## 5. Steps to Deploy
1. Push your code to GitHub.
2. Connect your repo to Render.com.
3. Render will auto-detect `render.yaml` and set up both services.
4. Set your environment variables in the Render dashboard if not in `render.yaml`.
5. Access your frontend and backend via the URLs Render provides.

---

For more details, see: https://render.com/docs/deploy-fastapi, https://render.com/docs/deploy-streamlit

