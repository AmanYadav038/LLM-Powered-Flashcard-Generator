import streamlit as st
from main import generate_flashcards
from utils import extract_text_from_pdf
import pandas as pd
import json

# Set up page config
st.set_page_config(page_title="🧠 Flashcard Generator", layout="centered")

# Main title
st.markdown("""
    <h1 style='text-align: center; color: #1E90FF;'>🧠 Flashcard Generator</h1>
    <p style='text-align: center;'>Upload educational content (PDF) or paste text to generate useful flashcards automatically.</p>
""", unsafe_allow_html=True)

# PDF Upload or Text Area
st.markdown("### 📂 Upload Content")
uploaded_file = st.file_uploader("Upload a PDF file:", type=["pdf"])
text_input = ""

if uploaded_file:
    st.info("📖 Extracting text from uploaded PDF...")
    text_input = extract_text_from_pdf(uploaded_file)
    st.success("✅ Text successfully extracted from PDF.")
else:
    st.markdown("Or paste your educational content manually 👇")
    text_input = st.text_area("📚 Enter educational content", height=300)

# Flashcard settings
st.markdown("### ⚙️ Settings")
col1, col2 = st.columns(2)
with col1:
    num = st.slider("Number of flashcards to generate", min_value=1, max_value=20, value=5)
with col2:
    subject = st.selectbox(
        "Select Subject (optional)",
        options=["General", "Biology", "History", "Physics", "Chemistry", "Mathematics", "Geography", "Computer Science"]
    )


# Generate flashcards button
st.markdown("### 🚀 Generate")
if st.button("⚡ Generate Flashcards") and text_input.strip():
    with st.spinner("Generating flashcards..."):
        flashcards = generate_flashcards(text_input, num)
    st.success("🎉 Flashcards generated!")

    # Display flashcards
    st.markdown("### 📝 Generated Flashcards")
    for i, card in enumerate(flashcards, 1):
        st.markdown(f"""
        <div style='background-color:#e6f0ff; color:#003366; padding:15px; border-radius:10px; border:1px solid #b3d1ff; margin-bottom:15px;'>
            <p><strong>Q{i}:</strong> {card['question']}</p>
            <p><strong>A{i}:</strong> {card['answer']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Prepare downloads
    df = pd.DataFrame(flashcards)
    json_data = json.dumps(flashcards, indent=2)

    # Export section
    st.markdown("### 📤 Export Flashcards")
    st.download_button("⬇️ Download as CSV", df.to_csv(index=False), file_name="flashcards.csv", mime="text/csv")
    st.download_button("⬇️ Download as JSON", json_data, file_name="flashcards.json", mime="application/json")

else:
    st.info("💡 Tip: Upload a PDF or paste content above, then click 'Generate Flashcards'!")
