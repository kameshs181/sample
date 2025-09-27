import streamlit as st
import json
import os

# ---------------- HELPER FUNCTIONS ---------------- #
USER_FILE = "users.json"

def load_users():
    """Load users from JSON file."""
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    else:
        # Default user for first time
        return {"admin": "1234"}

def save_users(users):
    """Save users to JSON file."""
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# ---------------- SESSION INIT ---------------- #
if "users" not in st.session_state:
    st.session_state["users"] = load_users()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- PAGES ---------------- #
def login_page():
    st.markdown("<h2 style='text-align: center;'>🔐 Login</h2>", unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.success(f"✅ Welcome, {username}!")
            st.session_state.logged_in = True
            st.session_state.current_user = username
            st.balloons()
        else:
            st.error("❌ Invalid Username or Password")

    st.markdown("---")
    if st.button("Don't have an account? Sign Up"):
        st.session_state.page = "signup"


def signup_page():
    st.markdown("<h2 style='text-align: center;'>📝 Sign Up</h2>", unsafe_allow_html=True)

    with st.form("signup_form"):
        new_user = st.text_input("Choose a Username")
        new_pass = st.text_input("Choose a Password", type="password")
        confirm_pass = st.text_input("Confirm Password", type="password")
        signup_btn = st.form_submit_button("Sign Up")

    if signup_btn:
        if new_user in st.session_state["users"]:
            st.error("⚠️ Username already exists. Try another.")
        elif new_pass != confirm_pass:
            st.error("⚠️ Passwords do not match.")
        elif len(new_user) < 3 or len(new_pass) < 3:
            st.warning("⚠️ Username & Password must be at least 3 characters long.")
        else:
            st.session_state["users"][new_user] = new_pass
            save_users(st.session_state["users"])
            st.success("✅ Account created successfully! Please login.")
            st.session_state.page = "login"

    st.markdown("---")
    if st.button("Already have an account? Login"):
        st.session_state.page = "login"


def dashboard():
    st.markdown(f"<h2>👋 Hello, {st.session_state.current_user}</h2>", unsafe_allow_html=True)
    st.success("You are logged in!")
    st.write("👉 Here you can show your app dashboard (charts, data, etc.).")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"

# ---------------- APP FLOW ---------------- #
if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.logged_in:
    dashboard()
else:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()
