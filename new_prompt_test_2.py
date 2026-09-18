from google import genai
from google.genai import types

client = genai.Client()

system_instructions = """
You create prompts written by a non-technical human for a GEO visibility study focused on ecommerce checkout and payment platforms.

Write prompts that a real ecommerce merchant might submit to an AI assistant when looking for a specific product, provider, 
platform, plugin, or integration

*Important*:
- do not be too verbose
- do not make the prompts too specific. here as an example:
    bad prompt: "We're seeing too many false declines on international transactions. What payment platforms support smart routing between multiple acquirers to automatically boost authorization rates?"
    good prompt: "What payment platforms prevent false declines for international transactions?"
- make the prompts sound human, for example:
    these prompts here:
        bad prompt: Can you recommend payment processors with built-in fraud prevention that won't block legitimate orders for high-ticket products?
        bad prompt: Which checkout platforms offer fully customizable, headless checkout experiences that integrate smoothly with existing ecommerce backends?
    Feedback: a human would not use phrases such as "high-ticket products" or "headless checkout experiences that integrate smoothly with existing backends" when prompting a system
    We want prompts that use day-to-day conversational wording

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
    model="gemini-3.8-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instructions
    ),
    contents=(
        "Create 10 distinct prompts that could lead an AI assistant to recommend specific ecommerce checkout or payment products"
    )
)

print(response.text)