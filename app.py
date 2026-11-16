import streamlit as st
import string
import math

st.set_page_config(
    page_title="Password Security Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Checker")
st.write("Analyze password security and get improvement suggestions.")

password = st.text_input(
    "Enter a test password",
    type="password",
    placeholder="Enter your test password"
)

if password:

    score = 0
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "welcome",
        "iloveyou"
    ]

    is_common = password.lower() in common_passwords

    if is_common:
        st.error(
            "+++++++++++++++++++++++++++++++++++++++++++++ This is a commonly used password. "
            "Choose a unique password."
        )
    suggestions = []

   
    if len(password) >= 12:
        score += 2
    else:
        suggestions.append("Use at least 12 characters.")

    
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

   
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    elif score <= 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    if is_common:
        strength = "Weak"
        score = 0

    
    st.subheader("Password Analysis")
    st.write("Strength:", strength)

    st.progress(score / 6)

    # Password Entropy Calculation
    st.subheader("🔍 Password Entropy Analysis")

    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26

    if any(c.isupper() for c in password):
        charset_size += 26

    if any(c.isdigit() for c in password):
        charset_size += 10

    if any(c in string.punctuation for c in password):
        charset_size += 32

    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)

        st.metric("Estimated Entropy", f"{entropy:.2f} bits")

        st.caption(
            "This is a theoretical estimate assuming "
            "characters are selected randomly."
        )

        # Illustrative guessing-time model
        guesses_per_second = 1000

        log_seconds = (
            entropy - 1 - math.log2(guesses_per_second)
        )

        st.subheader("⏱️ Cracking-Time Estimator")

        if log_seconds < 0:
            estimated_time = "Less than 1 second"
        elif log_seconds < math.log2(60):
            estimated_time = f"{2**log_seconds:.1f} seconds"
        elif log_seconds < math.log2(3600):
            estimated_time = f"{2**log_seconds / 60:.1f} minutes"
        elif log_seconds < math.log2(86400):
            estimated_time = f"{2**log_seconds / 3600:.1f} hours"
        elif log_seconds < math.log2(31557600):
            estimated_time = f"{2**log_seconds / 86400:.1f} days"
        elif log_seconds < math.log2(31557600 * 1000):
            estimated_time = f"{2**(log_seconds - math.log2(31557600)):.1f} years"
        else:
            estimated_time = "Over 1,000 years"

        st.success(f"Estimated guessing time: {estimated_time}")

        st.caption(
            "Assumption: 1,000 guesses per second. "
            "Actual results vary with hardware, attack method "
            "and password patterns."
        )

    st.subheader("Security Suggestions")

    if suggestions:
        for suggestion in suggestions:
            st.warning(suggestion)
    else:
        st.success("Good! All basic password checks passed.")