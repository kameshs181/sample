import streamlit as st

# Dummy credentials (you can later connect to database)
USER_CREDENTIALS = {"admin": "1234", "kamesh": "password"}

# Page config
st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")

# Title
st.markdown("<h2 style='text-align: center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

# Login form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.form_submit_button("Login")

if login_btn:
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.success(f"✅ Welcome, {username}!")
        st.balloons()
        st.write("You are now logged in. (Here you can redirect to dashboard)")
    else:
        st.error("❌ Invalid Username or Password")

# Extra links
st.markdown("---")
st.write("Forgot Password? [Click Here](#)")
st.write("Don't have an account? [Sign Up](#)")
