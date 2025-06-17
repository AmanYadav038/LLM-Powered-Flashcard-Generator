
# 🧠 LLM-Powered Flashcard Generator

The **LLM-Powered Flashcard Generator** is a modern, intelligent study tool that allows students, educators, and content creators to generate **question-answer flashcards** automatically from educational text or PDF files. It uses advanced NLP models like **T5** for question generation and **BART** for answer extraction, wrapped inside an intuitive **Streamlit web app**.

---

## 💡 How It Works

### 🔧 Core Logic (`main.py`)

The core functionality involves:

1. **Sentence Tokenization** using NLTK to divide content into logical units.
2. **Question Generation** using the `lmqg/t5-large-squad-qg` model.
3. **Relevance Ranking** of questions via **Sentence-BERT embeddings**.
4. **Answer Extraction** using the `valhalla/bart-large-finetuned-squadv1` model.
5. **PDF support**: Users can also upload educational PDFs — text is extracted using `PyMuPDF`.
6. **Flashcard Packaging**: Q&A pairs are combined and returned for display or download.

---

### 🖥️ User Interface (`streamlit_app.py`)

- Paste educational content or upload a `.pdf`
- Choose how many flashcards to generate
- Optional: Select a **subject type** to guide the prompt
- View generated flashcards in a styled UI
- Export to **CSV** or **JSON**

---

## 📦 Installation & Setup

### 🔁 Clone the Repository

```bash
git clone https://github.com/AmanYadav038/LLM-Powered-Flashcard-Generator.git
cd LLM-Powered-Flashcard-Generator
```

### 🐍 Set Up Environment

(Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate  # On Linux/macOS
```

### 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

Then open the app in your browser at:  
📍 `http://localhost:8501`

---

## 📄 Example API Input/Output (Internally)

```json
{
  "question": "What is the primary function of vehicles?",
  "answer": "To transport people or goods from one place to another."
}
```

---

## ✨ Features

- 📄 **Upload PDFs** and extract text
- 📚 **Paste raw educational content**
- 🎯 Generate **flashcards based on subject relevance**
- 💾 Export to **CSV** or **JSON**
- 💬 Clean and interactive **Streamlit interface**

---

## 🧪 Example Run

![App Screenshot](https://via.placeholder.com/800x400?text=Streamlit+Flashcard+App)

You can try it with `examples/vehicles_500_words.pdf` or paste your own text.

---

## 🛣️ Future Improvements

- ✅ Add support for **multi-language flashcards**
- ✅ Fine-tune custom models on educational corpora
- 🔄 Feedback mechanism for students
- 🔖 Export flashcards to **Anki/Quizlet** formats
- ⚡ Add **parallel processing** to speed up generation

---

## 📤 Exports

- `flashcards.csv` — for spreadsheets or sharing
- `flashcards.json` — for developer use or integration

---
