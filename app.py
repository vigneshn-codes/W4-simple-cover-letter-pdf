import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader

# LangChain (latest imports)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load env
load_dotenv()

# Page Config
st.set_page_config(
    page_title="🚀 AI Cover Letter Generator",
    page_icon="📄",
    layout="wide"
)

# ----------- PREMIUM UI -----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #2c5364);
}
.title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card {
    background: rgba(255,255,255,0.06);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
}
.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-weight: bold;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚀 AI Cover Letter Generator</div>', unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.header("⚙️ Settings")
tone = st.sidebar.selectbox("Tone", ["Professional", "Confident", "Enthusiastic"])
length = st.sidebar.slider("Length (words)", 150, 400, 250)

# ----------- PDF READER FUNCTION -----------
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Layout
col1, col2 = st.columns(2)

with col1:
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    
    resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    job_title = st.text_input("💼 Job Title")
    company_name = st.text_input("🏢 Company Name")
    extra_context = st.text_area("✍️ Additional Info (optional)")
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📄 Generated Cover Letter")
    output_placeholder = st.empty()
    st.markdown('</div>', unsafe_allow_html=True)

# API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ Please set OPENAI_API_KEY in .env file")
    st.stop()

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert career coach and professional writer."),
    
    ("human",
     """Write a {tone} cover letter.

Job Title: {job_title}
Company: {company_name}

Candidate Resume:
{resume_text}

Additional Info:
{extra_context}

Length: {length} words

Make it compelling, ATS-friendly, and tailored to the company.
Include introduction, skills alignment, and strong closing.""")
])

# Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser

# Generate Button
if st.button("🚀 Generate Cover Letter"):
    if resume_file and job_title and company_name:
        with st.spinner("Analyzing resume & generating..."):
            try:
                resume_text = extract_text_from_pdf(resume_file)

                response = chain.invoke({
                    "tone": tone,
                    "job_title": job_title,
                    "company_name": company_name,
                    "resume_text": resume_text[:3000],  # limit tokens
                    "extra_context": extra_context,
                    "length": length
                })

                output_placeholder.success(response)

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("⚠️ Please upload resume and fill all required fields")