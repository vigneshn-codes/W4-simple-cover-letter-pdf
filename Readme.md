# 🚀 AI Cover Letter Generator (Premium UI)

Generate personalized, ATS-friendly cover letters using AI.

---

## ✨ Features

- Upload Resume (PDF)
- Extracts resume content automatically
- Tailors cover letter to:
  - Job Title
  - Company Name
- Multiple tones
- Adjustable length
- Premium modern UI

---

## 🧠 Architecture

Resume PDF → Text Extraction → Prompt → LLM → Output

**LangChain Flow:**

prompt | llm | parser

---

## 📦 Installation

### 1. Clone Repo 
```bash
git clone <repo-url>
cd ai-cover-letter
```

---

### 2. Setup Environment 
```bash
ython -m venv venv 
source venv/bin/activate
```

---

### 3. Install Dependencies 
```bash
pip install -r requirements.txt
```
🔐 **API Setup**
Create `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

---

▶️ **Run App** 
```bash
treamlit run app.py

```

---

🧪 **Example Use Case**
- Upload your resume 
- Enter job title (e.g., Full Stack Developer) 
- Enter company (e.g., Google) 
- Click Generate 
- Get tailored cover letter instantly 