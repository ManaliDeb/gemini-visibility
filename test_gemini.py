from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Which checkout platforms are best for a growing ecommerce company",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ],
        temperature=1.0,
        max_output_tokens=2048,
    ),
)

print(response.text)
print(response.model_version)
print(response.usage_metadata)