import google.generativeai as ai

# API Key
API_KEY = 'AIzaSyDcKN3S0fcAdHPI1A1hvlSGHR2tHk73PBW'

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Start a conversation
while True:
    message = input('You: ')
    if message.lower() == 'bye':
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('Chatbot:', response.text)
