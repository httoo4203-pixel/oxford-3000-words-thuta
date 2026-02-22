import streamlit as st
import spacy
import pyinflect # ဒါကို import လုပ်ထားရုံနဲ့ spacy token ထဲမှာ inflect ပေါ်လာပါလိမ့်မယ်

# Load grammar model
@st.cache_resource
def load_nlp():
    # model မရှိရင် auto download လုပ်မယ့် logic
    try:
        return spacy.load("en_core_web_sm")
    except:
        import os
        os.system("python -m spacy download en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_nlp()

st.title("📖 Thuta's Oxford 3000 Master")

v1 = st.text_input("V1 (Base Form) ကို ရိုက်ထည့်ပါ:").strip().lower()

if v1:
    doc = nlp(v1)
    if len(doc) > 0:
        token = doc[0]
        
        # ._.inflect ဆိုတာ pyinflect က ပေးတဲ့ function ပါ
        v2 = token._.inflect("VBD") # Past
        v3 = token._.inflect("VBN") # Participle
        ving = token._.inflect("VBG") # Continuous

        st.success(f"'{v1}' Forms Found!")
        col1, col2, col3 = st.columns(3)
        col1.metric("V2 (Past)", v2 if v2 else "N/A")
        col2.metric("V3 (Participle)", v3 if v3 else "N/A")
        col3.metric("V-ing", ving if ving else "N/A")
    else:
        st.error("စကားလုံး ရိုက်ထည့်ပေးပါ")
