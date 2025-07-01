import google.generativeai as genai

#  Configure your API key
genai.configure(api_key="insret key")  # Replace with your actual key

#  Use the recommended fast model
model = genai.GenerativeModel("models/gemini-2.5-flash")

#  Generate content
response = model.generate_content("Give me a funny roast in Hinglish for a lazy friend.")

# Output
print("Gemini says:\n")
print(response.text)

