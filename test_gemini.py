from google import genai

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=(
        "Which checkout platforms are best for a growing ecommerce company"
    ),
)

print(response.output_text)