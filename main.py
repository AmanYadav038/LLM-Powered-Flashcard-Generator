import torch
import nltk
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForQuestionAnswering


# Download necessary NLTK resources
nltk.download('all')

# Load BART model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("valhalla/bart-large-finetuned-squadv1")
model = AutoModelForQuestionAnswering.from_pretrained("valhalla/bart-large-finetuned-squadv1")

pipe = pipeline("text2text-generation", 'lmqg/t5-large-squad-qg')

# Load Sentence-BERT model
sentence_bert_model = SentenceTransformer('average_word_embeddings_glove.6B.300d')

# Define the event handler for the button click
def generate_flashcards(text, num_flashcards=10, subject="General"):
    # Step 1: Tokenize text into sentences
    sentences = sent_tokenize(text)

    chunk_size = 1
    chunks = [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]

    # Step 3: Generate questions from chunks
    questions = []
    for chunk in chunks:
        prompt = f"generate a {subject.lower()} question from: {chunk}"
        try:
            result = pipe(prompt, max_length=64, do_sample=True, top_p=0.95)[0]['generated_text']
            questions.append(result)
        except Exception:
            continue

    # Step 4: Rank questions using Sentence-BERT embeddings
    if not questions:
        return []

    question_embeddings = sentence_bert_model.encode(questions)
    ranking_scores = question_embeddings.dot(question_embeddings.T).mean(axis=1)

    # Step 5: Select top N unique questions
    seen = set()
    sorted_indices = ranking_scores.argsort()[::-1]
    selected_questions = []
    for idx in sorted_indices:
        q = questions[idx].strip()
        if q not in seen and len(selected_questions) < num_flashcards:
            selected_questions.append(q)
            seen.add(q)

    # Step 6: Find answers using QA model
    answers = []
    for question in selected_questions:
        inputs = tokenizer.encode_plus(question, text, return_tensors="pt", add_special_tokens=True)
        input_ids = inputs["input_ids"].tolist()[0]

        with torch.no_grad():
            outputs = model(**inputs)

        start = torch.argmax(outputs.start_logits)
        end = torch.argmax(outputs.end_logits) + 1

        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[start:end]))
        answer = answer.replace("#", "").strip()
        if not answer:
            answer = "Answer not found clearly in the text."
        answers.append(answer)

    # Step 7: Bundle as flashcards
    flashcards = [{"question": q, "answer": a} for q, a in zip(selected_questions, answers)]
    return flashcards
