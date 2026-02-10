from dotenv import load_dotenv
load_dotenv()
from email_sender import send_email
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

def isprime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return "Not prime"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not prime"
    return "Prime"

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny and goood in {city}!"

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
)

agent = create_agent(
    model=model,
    tools=[get_weather, isprime,send_email],
    system_prompt="You are a helpful assistant",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in Mysore and is 2001 prime? and send an email to nandishd2005@gmail.com with the subject 'Test Email from Python' and content 'Hello 👋\nThis email was sent using Python!'about the weather and result prime number"}]}
)

# Print only the final AI response
final_msg = response["messages"][-1]
if isinstance(final_msg.content, list):
    for block in final_msg.content:
        if isinstance(block, dict) and block.get("type") == "text":
            print(block["text"])
else:
    print(final_msg.content)