import os
from dotenv import load_dotenv
from google import genai
from ayrshare import SocialPost
import random

# Load secret keys
load_dotenv()

# 1. Initialize Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_marketing_content():
    # Sigcom's specific services from the profile
    services = [
        "Outdoor Advertising (Digital & Display Billboards)",
        "Corporate Branding (Office & Shop Branding)",
        "Premium Printing Services",
        "Tear Drop Flags & Feather Banners",
        "Professional Graphic Design",
        "Web Development Solutions",
        "Ad Placement & Management"
    ]
    
    selected_service = random.choice(services)
    
    # Sigcom Company Context for the AI
    company_info = """
    Company: Sigcom Advertising
    Tagline: 'Be Seen'
    Location: No. 13 Olympia Park, Lusaka, Zambia
    Mission: Utilizing latest technologies to tailor design and execute professional solutions that accelerate client ROI.
    USP: 'We don't do average, we do awesome.' Specialized integrated full-service branding.
    Contact: +260 960 747309 / +260 775 437 999
    """
    
    print(f"🤖 Sigcom AI is crafting an ad for: {selected_service}...")
    
    prompt = f"""
    {company_info}
    
    Task: Write a high-impact LinkedIn and Facebook post for Sigcom Advertising focusing on {selected_service}.
    
    Guidelines:
    - Start with a catchy hook related to 'Being Seen' or professional branding.
    - Emphasize how Sigcom helps businesses differentiate their brand in the marketplace.
    - Mention our location in Lusaka and our commitment to ROI.
    - End with a strong Call to Action including our phone numbers.
    - Include 3 hashtags like #SigcomAdvertising #LusakaBusiness #BrandingZambia.
    - Tone: Professional, innovative, and high-energy.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )
    return response.text

# 2. Initialize the Poster
social = SocialPost(os.getenv("AYRSHARE_API_KEY"))

def post_to_socials(text):
    print("📤 Sending to social media platforms...")
    # Update platforms as needed
    result = social.post({
        'post': text,
        'platforms': ['linkedin', 'twitter'] 
    })
    return result

if __name__ == "__main__":
    content = generate_marketing_content()
    print(f"\n📝 New Sigcom Ad:\n{content}\n")
    
    # Remove the # below to start posting live to your accounts!
    # print(post_to_socials(content))
