import google.generativeai as genai  

# Set your Gemini API key
genai.configure(api_key="AIzaSyCUlTRqd-_T_dRXNheFYEEA2cAdrs5i3WA")  # Replace with your actual API key

def chatbot(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
 # Or use "gemini-1.5-flash-latest"
  # Using Gemini-Pro model
    response = model.generate_content(prompt)
    return response.text

# Chat loop
print("AI Chatbot is ready! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
