# Deployment Guide 🚀
## CarValue Predictor (FastAPI + Streamlit)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)

---

This document explains how to deploy **CarValue Predictor** as a production-style system using:

- **FastAPI backend** → Render  
- **Streamlit frontend** → Streamlit Cloud  

This separation is **industry-standard** and scalable.

---

## 🧱 Deployment Architecture

```
User
  ↓
Streamlit UI (Streamlit Cloud)
  ↓ REST API
FastAPI Backend (Render)
  ↓
ML Model (Random Forest)
```

---

## 🔹 Backend Deployment (FastAPI on Render)

### Prerequisites
- GitHub repository pushed
- `requirements.txt` present
- `runtime.txt` present (recommended)

Example `runtime.txt`:
```txt
python-3.10.12
```

---

### Steps

1. Go to **https://render.com**
2. Click **New → Web Service**
3. Connect your GitHub repository
4. Configure the service:

| Setting | Value |
|------|------|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

5. Click **Deploy**

---

### ✅ After Deployment

Render will provide a public URL like:
```
https://carvalue-api.onrender.com
```

Available endpoints:
- `/` → Health check
- `/predict` → Price prediction
- `/docs` → Swagger UI

---

## 🔹 Frontend Deployment (Streamlit Cloud)

### Steps

1. Go to **https://share.streamlit.io**
2. Click **New App**
3. Select:
   - GitHub repository
   - Branch: `main`
   - File path:
     ```
     ui/streamlit_app.py
     ```

4. Click **Deploy**

---

### 🔧 Update API URL

In `ui/streamlit_app.py`, update:

```python
API_URL = "https://carvalue-api.onrender.com/predict"
```

Replace with your actual Render backend URL.

---

### ✅ Streamlit App URL

After deployment, Streamlit Cloud will give you a URL like:
```
https://carvalue-predictor.streamlit.app
```

---

## ⚠️ Common Deployment Issues

- Cold start delay on Render (free tier)
- Ensure `.pkl` files are committed to GitHub
- Do not hardcode `localhost` in production
- Match Python version locally and in cloud

---

## ⭐ Why This Deployment Matters

This deployment demonstrates:
- End-to-end ML system design
- Backend–frontend separation
- Real-world cloud deployment experience
- Production-ready API practices

---

## ✅ Summary

- FastAPI backend deployed on **Render**
- Streamlit UI deployed on **Streamlit Cloud**
- Clean, scalable, and recruiter-friendly setup

