import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("⚠️ **Password should be at least 8 characters long.**")

    # Uppercase, lowercase, and digit check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("⚠️ **Password should contain at least one uppercase letter.**")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("⚠️ **Password should contain at least one lowercase letter.**")
    
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("⚠️ **Password should contain at least one digit.**")

    # Special characters check
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("⚠️ **Password should contain at least one special character (e.g. @, #, $, %, etc.).**")

    # Feedback and strength rating with emojis
    if strength == 5:
        return "💪 **Very Strong!**", feedback
    elif strength == 4:
        return "🔒 **Strong!**", feedback
    elif strength == 3:
        return "⚖️ **Moderate!**", feedback
    else:
        return "❌ **Weak!**", feedback

# Streamlit app
st.title("🔐 **Password Strength Checker** 💻")

# Heading with emojis and instructions
st.markdown("""
    <h2 style='text-align: center;'>💪 **Secure Your Accounts with a Strong Password!** 🔒</h2>
    <p style='text-align: center;'>🌟 **Enter a password below to check its strength!** 🛡️</p>
""", unsafe_allow_html=True)

password = st.text_input("🔑 **Enter your password:**", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    st.subheader(f"Password Strength: {strength}")
    
    # Display the feedback with emoji emphasis
    for line in feedback:
        st.write(line)
else:
    st.write("📝 **Please enter a password to check its strength.**")


