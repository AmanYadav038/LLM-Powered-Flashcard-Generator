# 🧠 LLM-Powered Flashcard Generator

An intelligent tool that generates question-answer flashcards from educational content using large language models (LLMs). Paste text or upload a PDF to instantly get structured flashcards you can use for studying or revision.

![Streamlit UI Screenshot](https://via.placeholder.com/800x400.png?text=Flashcard+Generator+UI)

---

## 🚀 Features

- 📄 Accepts raw content from **PDF files** or **text input**
- 🧠 Generates meaningful **question-answer flashcards**
- 🔍 Supports **subject-based prompting**
- 🌐 Uses **T5/BART for Q-generation** and **BERT for ranking**
- 📥 Download flashcards as **CSV** or **JSON**
- 🎨 Stylish and interactive **Streamlit interface**

---

## 🛠 Setup Instructions

### 📦 Requirements

```bash
git clone https://github.com/AmanYadav038/LLM-Powered-Flashcard-Generator.git
cd LLM-Powered-Flashcard-Generator

# Set up a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt


##Run the App
streamlit run streamlit_app.py

#Example Input (PDF or Text)
Topic : Vehicles
(PDF: examples/vehicles_500_words.pdf)

Generated Flashcards Example:
[
  {
    "question": "What is a vehicle?",
    "answer": "machines that transport people or goods from one place to another"
  },
  {
    "question": "What type of vehicles are there?",
    "answer": "many"
  },
  {
    "question": "What is the most common type of vehicle?",
    "answer": "Cars"
  },
  {
    "question": "What are some of the benefits of electric vehicles?",
    "answer": "They produce zero emissions, run more quietly,\nand often require less maintenance than traditional internal combustion engine vehicles"
  }
]

#Export Options 
1.flashcards.csv
2.flashcards.json
