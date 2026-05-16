import streamlit as st
import pandas as pd
import os
import time
from src.parser import ResumeParser
from src.skill_extractor import SkillExtractor
from src.vectorizer import Vectorizer
from src.ai_engine import AIEngine
from src.matcher import Matcher
from src.ranker import Ranker
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Resume Screener", page_icon="🤖", layout="wide")

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        color: #e0e0e0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        padding: 0.6rem 2rem;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .highlight {
        color: #00d4ff;
        font-weight: bold;
    }
    .insight-box {
        background: rgba(0, 212, 255, 0.1);
        border-left: 5px solid #00d4ff;
        padding: 15px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE ENGINES (Cached) ---
@st.cache_resource
def get_tools():
    parser = ResumeParser()
    extractor = SkillExtractor()
    vectorizer = Vectorizer()
    ai_engine = AIEngine()
    matcher = Matcher(vectorizer, extractor, ai_engine)
    ranker = Ranker()
    return parser, extractor, matcher, ranker

parser, extractor, matcher, ranker = get_tools()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.title("AI Settings")
    threshold = st.slider("Similarity Threshold (%)", 0, 100, 30)
    st.info("Adjust the threshold to filter candidates based on match confidence.")
    
    st.markdown("---")
    st.markdown("### System Status")
    st.success("NLP Core: Active")
    st.success("Vector Engine: Ready")

# --- MAIN UI ---
st.title("🚀 AI-based Resume Screening system")
st.markdown("Automate your recruitment with deep semantic analysis and skill-gap insights.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Job Description")
    jd_text = st.text_area("Paste the Job Description here...", height=300, placeholder="Required skills, experience, and responsibilities...")

with col2:
    st.subheader("📄 Upload Resumes")
    uploaded_files = st.file_uploader("Upload PDF or DOCX resumes", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Start AI Analysis"):
    if not jd_text:
        st.warning("Please provide a Job Description first.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        results = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for idx, file in enumerate(uploaded_files):
            # Simulated delay for "AI Processing" look
            status_text.markdown(f"🔍 Analyzing **{file.name}**...")
            time.sleep(0.5)
            
            # Save temporary file to parse
            temp_path = os.path.join("data/resumes", file.name)
            with open(temp_path, "wb") as f:
                f.write(file.getbuffer())
            
            # 1. Parse
            resume_text = parser.extract_text(temp_path)
            
            # 2. Match
            match_data = matcher.process(resume_text, jd_text)
            match_data['name'] = file.name
            
            results.append(match_data)
            
            # Update progress
            progress_bar.progress((idx + 1) / len(uploaded_files))
            
        status_text.success("Analysis Complete!")
        
        # 3. Rank
        ranked_results = ranker.rank_resumes(results)
        
        # Filter by threshold
        filtered_results = [r for r in ranked_results if r['score'] >= threshold]
        
        # --- RESULTS DISPLAY ---
        st.markdown("---")
        st.header("📊 Screening Results")
        
        if not filtered_results:
            st.error("No candidates met the minimum threshold. Try lowering the threshold or refining the JD.")
        else:
            # Summary Table
            df = pd.DataFrame([
                {"Candidate": r['name'], "Match Score (%)": r['score'], "Top Skills": ", ".join(r['matched_skills'][:3])}
                for r in filtered_results
            ])
            st.table(df)
            
            # Detailed Breakdown
            for r in filtered_results:
                with st.expander(f"Detailed Analysis: {r['name']} ({r['score']}%)"):
                    c1, c2 = st.columns([2, 1])
                    with c1:
                        st.markdown(f"**AI Reasoning:**")
                        st.markdown(f"<div class='insight-box'>{r['insight']}</div>", unsafe_allow_html=True)
                        
                        st.markdown("---")
                        st.markdown("**Skill Match Details:**")
                        sc1, sc2 = st.columns(2)
                        with sc1:
                            st.success(f"Matched Skills: {', '.join(r['matched_skills']) if r['matched_skills'] else 'None'}")
                        with sc2:
                            st.warning(f"Missing Skills: {', '.join(r['missing_skills']) if r['missing_skills'] else 'None'}")
                    
                    with c2:
                        # Simple Gauge Chart using Plotly
                        fig = px.pie(values=[r['score'], 100-r['score']], names=['Match', 'Gap'], 
                                     color_discrete_sequence=['#00d4ff', '#333'], hole=0.7)
                        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), height=200)
                        st.plotly_chart(fig, use_container_width=True)
                        st.markdown(f"<center><h2 style='color:#00d4ff'>{r['score']}%</h2></center>", unsafe_allow_html=True)

            # --- ANALYTICS ---
            st.markdown("---")
            st.subheader("📈 Group Analytics")
            fig_bar = px.bar(df, x="Candidate", y="Match Score (%)", color="Match Score (%)", 
                             color_continuous_scale='Bluered_r', title="Candidate Comparison")
            st.plotly_chart(fig_bar, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<center>Built with ❤️ by AI-Resume-Screener Team</center>", unsafe_allow_html=True)
