import google.generativeai as ai
import time

# API Key
API_KEY = 'AIzaSyDcKN3SOfcAdHPI1A1hvlSGHR2tHk73PBw'

# Configure the API
ai.configure(api_key=API_KEY)

# Create two AI instances
model = ai.GenerativeModel("gemini-1.5-flash")
chat1 = model.start_chat()
chat2 = model.start_chat()

# Start AI-to-AI conversation
message = "Hello, AI!"
while True:
    response1 = chat1.send_message(message)
    print("AI 1:", response1.text)
    
    time.sleep(1)  # Wait 1 second
    
    response2 = chat2.send_message(response1.text)
    print("AI 2:", response2.text)
    
    time.sleep(1)  # Wait 1 second
    
    message = response2.text  # Continue the conversation
