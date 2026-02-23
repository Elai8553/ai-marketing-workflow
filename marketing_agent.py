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
    image_url = f"https://source.unsplash.com/featured/800x600?{selected['img']}"
    
    # Randomly choose between a 'Post' or a 'Flyer'
    is_flyer = random.choice([True, False])
    
    if is_flyer:
        # Flyer Prompt: Focused on structured layout and urgency
        prompt = f"""
        Create a DIGITAL FLYER for Sigcom Advertising in Lusaka.
        Topic: {selected['name']}
        
        Layout Style:
        - Start with a bold Header using emojis: 📢 [HEADLINE]
        - Use a section called 'WHY CHOOSE US?' with bullet points.
        - Include 'Our Motto: We don't do average, we do awesome.'
        - Emphasize our location: No. 13 Olympia Park, Lusaka.
        - Contact Footer: +260 960 747309 / +260 775 437 999.
        """
    else:
        # Post Prompt: Focused on engagement and branding
        prompt = f"""
        Write a professional LinkedIn/Facebook post for Sigcom Advertising.
        Service: {selected['name']}
        Motto: 'Be Seen'
        Tone: Innovative, high-energy.
        Include our Lusaka location and contact info at the end.
        """
    
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text, image_url

social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text, image):
    print(f"📤 Posting to Sigcom Socials...")
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'facebook', 'twitter'],
        'mediaUrls': [image]
    })
    return result

if __name__ == "__main__":
    content, image = generate_sigcom_content()
    print(f"--- CONTENT ---\n{content}\n--- IMAGE ---\n{image}")
    
    # REMOVE THE '#' BELOW TO GO LIVE
    # print(post_to_socials(content, image))
