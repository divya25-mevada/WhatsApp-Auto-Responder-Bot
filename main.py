import pyautogui
import time
import pyperclip
import google.generativeai as genai

# ✅ Configure Gemini API key
genai.configure(api_key="Apikey Insert")  # Replace with your actual key

# ✅ Use fast Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

def is_last_message_from_sender(chat_log, sender_name="Rishi"):
    # Get the last message and check sender
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

def get_gemini_reply(chat_history):
    try:
        prompt = (
    "You are a polite and professional virtual assistant. "
    "You read the last message from the user and reply in a respectful, helpful, and clear tone. "
    "Always keep the response short, professional, and relevant. "
    "Avoid using slang, emojis, or informal language. "
    "Maintain a calm and professional attitude in all replies.\n\n"
    f"{chat_history}\n\n"
    "Reply with ONE short, professional message."
)
       
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("❌ Gemini Error:", e)
        return "API Error: Unable to generate reply."

# Step 1: Click Chrome icon (your location)
pyautogui.click(1291, 1044)
time.sleep(1)

while True:
    try:
        time.sleep(2)

        # Step 2: Select message
        pyautogui.moveTo(670, 203)
        pyautogui.dragTo(1876, 925, duration=2.0, button='left')

        # Step 3: Copy message
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.click(856, 966)

        # Step 4: Get clipboard chat history
        chat_history = pyperclip.paste()
        print("📩 Copied:", chat_history)
        print("🔍 From Rishi CE*:", is_last_message_from_sender(chat_history))

        if is_last_message_from_sender(chat_history):
            # Step 5: Get reply from Gemini
            reply = get_gemini_reply(chat_history)
            pyperclip.copy(reply)

            # Step 6: Paste and send
            pyautogui.click(856, 966)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
            print("🤖 Replied:", reply)

    except KeyboardInterrupt:
        print("🛑 Bot stopped by user.")
        break

    except Exception as e:
        print("⚠️ Error:", e)
        time.sleep(1) 
