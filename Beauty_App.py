import streamlit as st
import google.generativeai as genai
from datetime import datetime

GEMINI_API_KEY = ""

 
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

import streamlit as st
import google.generativeai as genai

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="💄 GlamAI",
    page_icon="💖",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ffe6f2, #ffd6eb);
}

.main-title {
    text-align:center;
    color:#d63384;
    font-size:50px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#c2185b;
    font-size:18px;
    margin-bottom:20px;
}

.card {
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

.stButton > button {
    background:#ff4da6;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px 25px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

.stButton > button:hover {
    background:#e91e63;
    color:white;
}

.result-box {
    background:#fff0f5;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #ff4da6;
    color:black;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<h1 class="main-title">💄 GlamAI Beauty Assistant</h1>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="subtitle">AI Powered Makeup Recommendations Based On Your Skin ❤️</p>',
    unsafe_allow_html=True,
)

# -----------------------------
# GEMINI API KEY
# -----------------------------
GEMINI_API_KEY = ""

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-flash-lite-latest")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    skin_type = st.selectbox(
        "✨ Skin Type",
        ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
    )

    skin_tone = st.selectbox(
        "🎨 Skin Tone",
        [
            "Fair",
            "Light",
            "Medium",
            "Olive",
            "Tan",
            "Deep"
        ]
    )

with col2:

    concern = st.selectbox(
        "🌸 Skin Concern",
        [
            "Acne",
            "Pigmentation",
            "Dark Circles",
            "Redness",
            "Large Pores",
            "None"
        ]
    )

    occasion = st.selectbox(
        "🎉 Occasion",
        [
            "Daily Wear",
            "Office",
            "Party",
            "Wedding",
            "Date Night",
            "Festival"
        ]
    )

favorite_colors = st.text_input(
    "💖 Favorite Makeup Colors",
    placeholder="Pink, Nude, Peach, Rose Gold..."
)

budget = st.selectbox(
    "💰 Budget",
    [
        "Budget Friendly",
        "Mid Range",
        "Luxury"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# BUTTON
# -----------------------------
if st.button("✨ Get Makeup Recommendations"):

    with st.spinner("Creating your beauty look... 💕"):

        prompt = f"""
        You are a professional beauty consultant.

        Recommend makeup products and techniques based on:

        Skin Type: {skin_type}
        Skin Tone: {skin_tone}
        Skin Concern: {concern}
        Occasion: {occasion}
        Favorite Colors: {favorite_colors}
        Budget: {budget}

        Give:

        1. Suitable primer
        2. Foundation recommendation
        3. Concealer suggestion
        4. Blush shades
        5. Eye makeup ideas
        6. Lipstick shades
        7. Highlighter recommendation
        8. Makeup tips
        9. Common mistakes to avoid
        10. A complete final makeup look

        Format nicely with emojis.
        """

        try:
            response = model.generate_content(prompt)

            st.markdown(
                f"""
                <div class="result-box">
                {response.text}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    "<center>💖 Made with Gemini AI & Streamlit 💖</center>",
    unsafe_allow_html=True
)