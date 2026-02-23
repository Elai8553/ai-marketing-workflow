import os
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost

# Load secret keys
load_dotenv()

# 1. Initialize Gemini (The Copywriter)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_marketing_content(topic):
    print(f"🤖 Gemini is thinking about: {topic}...")
    prompt = f"Write a catchy LinkedIn post about {topic}. Include 3 relevant hashtags."
    
    # We use 'gemini-2.5-flash' for speed and free tier access
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    return response.text

# 2. Initialize the Poster (The Distributor)
social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text):
    print("📤 Sending to social media platforms...")
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'twitter'] 
    })
    return result

if __name__ == "__main__":
    my_topic = "How AI is changing digital marketing in 2026"
    content = generate_marketing_content(my_topic)
    print(f"\n📝 Generated Content:\n{content}\n")
    
    # print(post_to_socials(content))
