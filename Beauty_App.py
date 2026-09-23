import streamlit as st
from groq import Groq

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
    text-align: center;
    color: #d63384;
    font-size: 55px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #c2185b;
    font-size: 20px;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.stButton > button {
    background: #ff4da6;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background: #e91e63;
    color: white;
}

.result-box {
    background: #fff0f5;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #ff4da6;
    color: black;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    '<h1 class="main-title">💄✨ GlamAI Beauty Assistant ✨💄</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">🌸 AI-Powered Makeup Recommendations Tailored Just For You 💖</p>',
    unsafe_allow_html=True
)

# -----------------------------
# GROQ API
# -----------------------------
api_key = st.secrets['API']

client = Groq(api_key=api_key)

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
        ["Fair", "Light", "Medium", "Olive", "Tan", "Deep"]
    )

with col2:
    concern = st.selectbox(
        "🌸 Skin Concern",
        ["Acne", "Pigmentation", "Dark Circles", "Redness", "Large Pores", "None"]
    )

    occasion = st.selectbox(
        "🎉 Occasion",
        ["Daily Wear", "Office", "Party", "Wedding", "Date Night", "Festival"]
    )

favorite_colors = st.text_input(
    "💖 Favorite Makeup Colors",
    placeholder="Pink, Nude, Peach, Rose Gold..."
)

budget = st.selectbox(
    "💰 Budget",
    ["Budget Friendly", "Mid Range", "Luxury"]
)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# GENERATE RECOMMENDATIONS
# -----------------------------
if st.button("✨ Get Makeup Recommendations"):

    with st.spinner("Creating your perfect beauty look... 💕"):

        prompt = f"""
You are an expert professional beauty consultant and makeup artist.

Provide personalized recommendations based on:

Skin Type: {skin_type}
Skin Tone: {skin_tone}
Skin Concern: {concern}
Occasion: {occasion}
Favorite Colors: {favorite_colors}
Budget: {budget}

Include:

💎 Suitable Primer
💎 Foundation Recommendation
💎 Concealer Suggestion
💎 Blush Shades
💎 Eye Makeup Ideas
💎 Lipstick Shades
💎 Highlighter Recommendation
💎 Makeup Tips
💎 Common Mistakes To Avoid
💎 Complete Final Makeup Look

Make the response attractive, detailed, feminine, easy to read, and use emojis.
"""

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional beauty and makeup advisor."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_completion_tokens=1500
            )

            result = response.choices[0].message.content

            st.markdown(
                f"""
                <div class="result-box">
                {result}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    """
    <center>
    💖 Made with Groq GPT-OSS-120B & Streamlit 💖
    </center>
    """,
    unsafe_allow_html=True
)
