import streamlit as st
import spacy
import pyinflect

# Load grammar engine
@st.cache_resource
def load_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except:
        import os
        os.system("python -m spacy download en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_nlp()

# UI Design
st.set_page_config(page_title="Thuta's Verb Morph", page_icon="📖")
st.title("📖 Thuta's Oxford 3000 Master")

# Input Section
v1 = st.text_input("V1 (Base Form) ကို ရိုက်ထည့်ပါ:", placeholder="ဥပမာ- think, go, observe...").strip().lower()

if v1:
    doc = nlp(v1)
    if len(doc) > 0:
        token = doc[0]
        
        # Verb Forms Generation
        v2 = token._.inflect("VBD") # Past
        v3 = token._.inflect("VBN") # Participle
        ving = token._.inflect("VBG") # Continuous

        st.success(f"'{v1}' ရဲ့ Form တွေကို ရှာတွေ့ပါပြီ!")
        
        # Display Result
        col1, col2, col3 = st.columns(3)
        col1.metric("V2 (Past)", v2)
        col2.metric("V3 (Participle)", v3)
        col3.metric("V-ing", ving)

        st.info(f"Keep going, Thuta! You're learning {v1} today.")
    else:
        st.error("စကားလုံး မှန်ကန်စွာ ရိုက်ထည့်ပါ!")
