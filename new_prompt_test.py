from google import genai
from google.genai import types

client = genai.Client()

system_instructions = """
You create natural language prompts for a GEO visibility study focused on ecommerce checkout and payment platforms.

Write prompts that a real ecommerce merchant might submit to an AI assistant when looking for a specific product, provider, 
platform, plugin, or integration

Each prompt should:
- ask for a product recommendation, comparison, or suitable provider
- describe a concrete business need or problem
- include two or more relevant requirements when possible
- give an AI assistant a clear reason to name actual products
- sound conversational rather than like an SEO keyword
- be specific enough that established payment providers could be recommended
- remain relevant to newer checkout and commerce platforms
- avoid generic questions that can be answered entirely with general advice
- avoid vague phrases such as "accelerate business growth"
- not mention Krepling, Stripe, or any other company by name, but should be able to surface them
- be no more than 35 words
- end with a question mark
- return only the prompts, with one prompt per line

Relevant subjects include one click checkout, guest checkout, checkout conversion, international payments, 
multiple currencies, payment routing, authorization rates, subscriptions, fraud prevention, tokenization, 
ecommerce integrations, payment analytics, and agentic commerce
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=system_instructions
    ),
    contents=(
        "Create 10 distinct prompts that could lead an AI assistant to recommend specific ecommerce checkout or payment products"
    )
)

print(response.text)