import os
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost
import random

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sigcom_content():
    service_data = [
        {"name": "Digital & Display Billboards", "img": "billboard,outdoor"},
        {"name": "Office & Shop Branding", "img": "office,reception"},
        {"name": "Vehicle Branding & Wraps", "img": "car,wrap"},
        {"name": "Tear Drop Flags & Banners", "img": "event,banner"},
        {"name": "Large Format Printing", "img": "printing"}
    ]
    selected = random.choice(service_data)
    image_url = "https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=800&q=80"
    
    is_flyer = random.choice([True, False])
    
    if is_flyer:
        prompt = f"Create a DIGITAL FLYER for Sigcom Advertising in Lusaka. Topic: {selected['name']}. Include Motto: 'Be Seen', Location: No. 13 Olympia Park, and Contacts: +260 960 747309 / +260 775 437 999. Use bullet points."
    else:
        prompt = f"Write a high-energy LinkedIn post for Sigcom Advertising about {selected['name']}. Mention 'Be Seen' and our Lusaka location."
    
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text, image_url

social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text, image):
    print("📤 Attempting to post to Ayrshare...")
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'facebook'],
        'mediaUrls': [image]
    })
    return result

if __name__ == "__main__":
    content, image = generate_sigcom_content()
    # This block must have NO LEADING SPACES before 'content' and 'print'
    print(f"--- CONTENT ---\n{content}")
    status = post_to_socials(content, image)
    print(f"--- AYRSHARE RESPONSE ---\n{status}")
