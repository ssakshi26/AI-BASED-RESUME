# AI-based Resume Screening system 🤖

An intelligent resume screening system using NLP and Machine Learning to automatically rank job candidates based on skill match, relevance, and job similarity.

## 🌟 Features
- **AI-Powered Matching**: Uses Sentence Transformers (`all-MiniLM-L6-v2`) for semantic similarity.
- **Hybrid Scoring**: Combines vector embeddings with rule-based skill density analysis.
- **Multi-Format Parsing**: Supports both **PDF** and **DOCX** resumes.
- **Premium Dashboard**: Professional dark-mode interface with interactive analytics.
- **AI Insights**: Automated strengths and gaps analysis for every candidate.

## 🛠️ Tech Stack
- **Language**: Python
- **Frontend**: Streamlit
- **NLP**: spaCy, Sentence-Transformers, Scikit-Learn
- **Visualization**: Plotly, Pandas
- **Parsing**: PyMuPDF, Python-Docx

## 🚀 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-resume-screening.git
   cd ai-resume-screening
   ```

2. **Install dependencies**:
   ```bash
   py -m pip install -r requirements.txt
   ```

3. **Download NLP Model**:
   ```bash
   py -m spacy download en_core_web_sm
   ```

4. **Run the application**:
   ```bash
   py -m streamlit run app.py
   ```

## 📁 Project Structure
```text
AI_Resume_Screening/
├── data/
│   └── resumes/          # Uploaded resumes stored here
├── src/
│   ├── ai_engine.py      # Mimicked AI reasoning logic
│   ├── matcher.py        # Scoring and matching logic
│   ├── parser.py         # PDF/DOCX text extraction
│   ├── ranker.py         # Ranking algorithms
│   ├── skill_extractor.py# NLP-based skill extraction
│   └── vectorizer.py     # Sentence embeddings
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 📊 How it Works
1. **Resume Upload**: User uploads multiple resumes (PDF/DOCX).
2. **Job Description**: User pastes the JD in the text area.
3. **Parsing & Cleaning**: System extracts raw text and normalizes it.
4. **Vectorization**: Both JD and Resumes are converted into high-dimensional embeddings.
5. **Scoring**: Cosine similarity is calculated and boosted by skill-match density.
6. **Ranking**: Candidates are ranked and visualized on the dashboard with AI-generated insights.

---
Built for the Mini Capstone Project.
