from google import genai
import os

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents="Explain Generative AI in 5 lines."
)

print(response.text)
