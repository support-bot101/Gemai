from google import genai

from google.genai import types

import os

os.environ["API_KEY"] = '929971453993'

client = genai.Client(api_key=os.environ["API_KEY"])
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='what does pandas package do?'
)
print(response.text)



