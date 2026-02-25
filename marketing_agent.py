import os
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost
import random

load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sigcom_content():
    service_data = [
        {"name": "Digital & Display Billboards", "img": "billboard,city"},
        {"name": "Office & Shop Branding", "img": "office,branding"},
        {"name": "Vehicle Branding & Wraps", "img": "car,wrap"},
        {"name": "Large Format Printing", "img": "printing,press"}
    ]
    selected = random.choice(service_data)
    
    # Static high-quality image link
    image_url = "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=800&q=80"
    
    prompt = f"Create a professional LinkedIn post for Sigcom Advertising, Lusaka about {selected['name']}. Motto: 'Be Seen'. Location: No. 13 Olympia Park. Contact: +260 960 747309."
    
    # FIXED MODEL NAME FOR SDK
    response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    return response.text, image_url

# Initialize Ayrshare
social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text, image):
    print("📤 Sending to Ayrshare...")
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'facebook'],
        'mediaUrls': [image]
    })
    return result

if __name__ == "__main__":
    try:
        content, image = generate_sigcom_content()
        print(f"--- CONTENT GENERATED ---\n{content}")
        
        # ACTUALLY POSTING
        status = post_to_socials(content, image)
        print(f"--- AYRSHARE RESPONSE ---\n{status}")
        
    except Exception as e:
        print(f"--- SYSTEM ERROR ---\n{e}")
