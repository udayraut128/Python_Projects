
from openai import OpenAI, APIError, RateLimitError

client = OpenAI()

print("AI Chatbot (type 'exit' to quit)")

while True:
    question = input("YOU: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("AI: Goodbye!")
        break

    if not question:
        continue

    try:
        response = client.responses.create(
            model="gpt-5",
            input=question
        )

        print("AI:", response.output_text)

    except RateLimitError as e:
        print("AI: API quota or rate limit issue.")
        print("Check your billing:", 
              "https://platform.openai.com/settings/organization/billing/")
        break

    except APIError as e:
        print("AI: OpenAI API error:", e)

