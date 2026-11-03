import streamlit as st

# Set page configuration
st.set_page_config(page_title="Studio AI - Login", layout="centered")

# Custom CSS for dark background and styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1a1518;
        color: #ffffff;
    }
    .main-title {
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
    }
    .divider {
        margin-top: 2rem;
        margin-bottom: 2rem;
        border-top: 1px solid #332d30;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the logo handling
try:
    st.image("logo.png", width=120)
except FileNotFoundError:
    st.warning(
        "Logo file 'logo.png' not found. Please upload your logo to the repository."
    )

# Add some vertical space
st.write("")

# Main header
st.markdown(
    "<h2 class='main-title'>Sign In or Register</h2>", unsafe_allow_html=True
)

# Center the buttons (using columns to constrain width)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Sign In Buttons
    if st.button("🔴 Continue with Google", use_container_width=True):
        pass

    if st.button(" Sign in with Apple", use_container_width=True):
        pass

    if st.button("🔵 Continue with Facebook", use_container_width=True):
        pass

    if st.button("⚫ Sign in with X / Twitter", use_container_width=True):
        pass

    if st.button("🪟 Sign in with Microsoft", use_container_width=True):
        pass

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Email and Password fields
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    # Sign In / Register with Email button
    if st.button("Sign In / Register with Email", use_container_width=True):
        pass
