
import streamlit as st
import spacy
import os

# Cloud ပေါ်မှာ Model မရှိရင် ဒေါင်းခိုင်းတဲ့ Logic
@st.cache_resource
def load_nlp():
    model_name = "en_core_web_sm"
    try:
        return spacy.load(model_name)
    except OSError:
        os.system(f"python -m spacy download {model_name}")
        return spacy.load(model_name)

nlp = load_nlp()

st.title("📖 Thuta's Oxford 3000 Master")

v1 = st.text_input("V1 (Base Form) ကို ရိုက်ထည့်ပါ:").strip().lower()

if v1:
    doc = nlp(v1)
    token = doc[0]
    
    # Form ထုတ်ခြင်း
    v2 = token._.inflect("VBD")
    v3 = token._.inflect("VBN")
    ving = token._.inflect("VBG")

    st.success(f"'{v1}' Forms Found!")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("V2 (Past)", v2)
    col2.metric("V3 (Participle)", v3)
    col3.metric("V-ing", ving)
