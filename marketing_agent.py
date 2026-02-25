import os
import random
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost

# 1. Load Environment Variables
load_dotenv()

# 2. Setup Gemini (Using Gemini 3 Flash for 2026 stability)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sigcom_content():
    service_data = [
        {"name": "Digital & Display Billboards"},
        {"name": "Office & Shop Branding"},
        {"name": "Vehicle Branding & Wraps"},
        {"name": "Large Format Printing"}
    ]
    selected = random.choice(service_data)
    
    # Official business details for Sigcom
    prompt = (
        f"Create a professional social media post for Sigcom Advertising, Lusaka. "
        f"Topic: {selected['name']}. "
        f"Include our Motto: 'Be Seen'. "
        f"Address: No. 13 Olympia Park. "
        f"Contact: +260 960 747309. "
        f"Keep it energetic and use emojis."
    )
    
    # UPDATED MODEL NAME TO PREVENT 404 ERROR
    print("🤖 Generating content with Gemini...")
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    
    # Static image for branding
    image_url = "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=800&q=80"
    
    return response.text, image_url

# 3. Setup Ayrshare
social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text, image):
    print("📤 Sending to Ayrshare...")
    payload = {
        'post': text,
        'platforms': ['linkedin', 'facebook'],
        'mediaUrls': [image]
    }
    return social.post(payload)

# 4. Main Execution Logic
if __name__ == "__main__":
    try:
        # Step A: Generate Content
        content, image = generate_sigcom_content()
        print(f"✅ CONTENT GENERATED:\n{content}\n")
        
        # Step B: Post to Socials
        print("🚀 Starting post sequence...")
        result = post_to_socials(content, image)
        print(f"📢 AYRSHARE RESPONSE: {result}")
        
    except Exception as e:
        print(f"❌ SYSTEM ERROR: {e}")
