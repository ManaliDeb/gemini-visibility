from google import genai

client = genai.Client()

models = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash-lite",
]

for model in models:
    print(f"\nTesting {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Write one short question about ecommerce checkout.",
        )

        print("SUCCESS")
        print(response.text)

    except Exception as error:
        print("FAILED")
        print(type(error).__name__, error)