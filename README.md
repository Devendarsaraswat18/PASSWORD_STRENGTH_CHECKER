 Password Strength Checker with Cracking-Time Estimator

 Project Overview

Password Strength Checker is a Python-based cybersecurity project developed using Streamlit. It analyzes password strength and provides useful security recommendations to help users understand how secure their passwords are.

The application checks different password characteristics and provides a theoretical password entropy and guessing-time estimate.

 Objectives

- Analyze password strength.
- Identify commonly used passwords.
- Calculate estimated password entropy.
- Estimate theoretical password guessing time.
- Provide suggestions to improve password security.

 Features

- Password Strength Analysis: Classifies passwords as Weak, Medium, Strong, or Very Strong.
- Common Password Detection: Identifies selected commonly used passwords.
- Entropy Calculation: Estimates password entropy in bits.
- Cracking-Time Estimator: Provides a theoretical guessing-time estimate.
- Security Recommendations: Suggests ways to improve password strength.
- Interactive Dashboard: Simple and user-friendly interface.

Technologies Used

- Python 3
- Streamlit
- Math Module
- String Module

 Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/Password-Strength-Checker.git

2. Open the project folder

cd Password-Strength-Checker

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py

 How It Works

1. User enters a test password.
2. The application checks password length and character types.
3. It calculates a basic strength score.
4. It checks whether the password matches selected common passwords.
5. It estimates theoretical entropy and guessing time.
6. It displays security suggestions.

 Security Note

This project is designed for educational purposes. Entropy and guessing-time results are theoretical estimates, not guarantees of actual password security. The current implementation uses a simplified character-set model and a configurable assumed guessing rate.

Users should only enter dummy or test passwords. The application is not intended to store or transmit passwords.

 Future Improvements

- Expanded common-password detection.
- Detection of repeated and predictable patterns.
- More advanced password analysis.
- Improved dashboard design.
- Additional security recommendations.

Author

Devendar Saraswat

B.Tech Computer Science and Engineering

 License

This project is created for educational and internship purposes.
