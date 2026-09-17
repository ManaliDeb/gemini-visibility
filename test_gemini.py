from google import genai

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.8-flash",
    input=(
        "Which checkout platforms are vest for a growing ecommerce company"
    ),
)

print(response.output_text)