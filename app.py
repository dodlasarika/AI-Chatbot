import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load API keys from .env file
load_dotenv()
API_KEYS = [
    os.getenv("PRIMARY_API_KEY"),  # First API key
    os.getenv("BACKUP_API_KEY")    # Backup API key
]

# Function to configure API with backup support
def configure_gemini():
    for key in API_KEYS:
        if key:  # Check if key is not None
            try:
                genai.configure(api_key=key)
                # Test if the key works
                model = genai.GenerativeModel("gemini-1.5-flash-latest")
                response = model.generate_content("Hello!")
                if response:
                    print(f"Using API Key: {key[:10]}...")  # Show only part of the key for security
                    return
            except Exception as e:
                print(f"API Key failed: {key[:10]}..., trying next key.")

# Call the function to configure the working API key
configure_gemini()

# Initialize Flask app
app = Flask(__name__)

# Route for chatbot page
@app.route("/")
def home():
    return render_template("index.html")

# API route to get chatbot response
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(user_input)
    return response.text

# ✅ ADD THIS PART TO RUN FLASK PROPERLY
if __name__ == "__main__":
    app.run(debug=True)
