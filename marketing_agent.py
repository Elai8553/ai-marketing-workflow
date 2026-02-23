import os
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost
import random

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_sigcom_content():
    # Sigcom services and their matching image search terms
    service_data = [
        {"name": "Digital & Display Billboards", "img": "billboard,outdoor"},
        {"name": "Office & Shop Branding", "img": "office,reception,interior"},
        {"name": "Vehicle Branding & Wraps", "img": "car,van,wrap"},
        {"name": "Tear Drop Flags & Banners", "img": "event,banner,flag"},
        {"name": "Large Format Printing", "img": "printing,industrial"}
    ]
    
    selected = random.choice(service_data)
    # Using a stable high-quality image link
    image_url = f"https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=800&q=80"
    
    # Randomly choose between a 'Post' or a 'Flyer'
    is_flyer = random.choice([True, False])
    
    if is_flyer:
        prompt = f"""
        Create a DIGITAL FLYER for Sigcom Advertising in Lusaka.
        Topic: {selected['name']}
        Layout Style:
        - Start with a bold Header: 📢 [HEADLINE]
        - Section: 'WHY CHOOSE US?' with bullet points.
        - Include Motto: 'We don't do average, we do awesome.'
        - Location: No. 13 Olympia Park, Lusaka.
        - Contact: +260 960 747309 / +260 775 437 999.
        """
    else:
        prompt = f"""
        Write a professional LinkedIn post for Sigcom Advertising about {selected['name']}.
        Motto: 'Be Seen'. Include our Lusaka location and contact info.
        """
    
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text, image_url

social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text, image):
    print(f"📤 Posting to Sigcom Socials...")
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'facebook'],
        'mediaUrls': [image]
    })
    return result

if __name__ == "__main__":
    content, image = generate_sigcom_content()
    print(f"--- CONTENT ---\n{content}\n--- IMAGE ---\n{image}")
    
    # The line below is now LIVE (no # and correctly indented)
    print(post_to_socials(content, image))
