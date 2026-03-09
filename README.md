# Baadalsoft AI Assistant

This is a Flask-based AI Assistant web application using **Google Gemini API**, **TF-IDF**, and **cosine similarity** to answer user queries based on provided documents (`docs.json`).

The UI is simple, with a chatbox, input area, and thinking animation.

**Live Project:** [Baadalsoft AI Assistant](https://gen-ai-assistant-baadalsoft.vercel.app/)

---

## Folder Structure

```
gen-chat-assistant/
├─ app.py
├─ docs.json
├─ requirements.txt
├─ vercel.json
├─ static/
│  ├─ style.css
│  ├─ script.js
│  ├─ badalsoft.png
│  └─ logo.png
└─ templates/
   └─ index.html
```

---

## 1️⃣ Local Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd gen-chat-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

* **Windows BASH**

```bash
venv\Scripts\activate
```

* **Windows PowerShell**

```powershell
venv\Scripts\Activate.ps1
```

* **Mac/Linux**

```bash
source venv/bin/activate
```

### 4. Deactivate virtual environment

```bash
deactivate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Set Environment Variable

Set your **Google API key**:

* **Windows CMD**

```bash
set GOOGLE_API_KEY=your_api_key_here
```

* **Mac/Linux**

```bash
export GOOGLE_API_KEY=your_api_key_here
```

### 7. Run the application

```bash
python app.py
```

### 8. Open in browser

Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
You should see the Baadalsoft AI Assistant UI and can start chatting.

---

## 2️⃣ Deploy on Vercel (GUI)

### 1. Go to Vercel dashboard

[https://vercel.com/dashboard](https://vercel.com/dashboard)

### 2. Create a new project

* Click **New Project** → **Import Git Repository**
* Connect your GitHub / GitLab / Bitbucket repo

### 3. Configure Project

* Framework Preset: **Other**
* Root Directory: `gen-chat-assistant` (if repo has subfolder)
* Environment Variables:

  * Key: `GOOGLE_API_KEY`
  * Value: `<your_api_key_here>`
* Click **Deploy**

### 4. Wait for Deployment

* Vercel will build the project and provide a **live URL**
* Open the URL → AI Assistant will work with **full UI, images, and chat functionality**

### 5. Optional: Vercel CLI

```bash
npm i -g vercel
vercel login
vercel
```

* Choose **Other** preset when prompted.

---

## 3️⃣ Important Notes

* **Static Files**:
  Static files (CSS, JS, images) are served via `/static/<filename>` route in Flask for Vercel compatibility.

* **Locally**: `debug=True` is enabled for automatic reload and console logs.

* **Vercel**: `debug` is ignored automatically; safe for production.

* **docs.json**: Add your own documents in JSON format:

```json
[
  {
    "title": "Document 1",
    "content": "This is the content of the document."
  }
]
```

* **UI**: Fully functional and unchanged; works both locally and on Vercel.

---

## 4️⃣ Social Handles
1. https://www.linkedin.com/in/iamvikramkumar5/
2. https://www.instagram.com/thevikram_seth/

