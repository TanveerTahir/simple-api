from fastapi import FastAPI
import random

app = FastAPI()

# we will build two simple endpoints
# side hustles
# money quotes

side_hustles = [
    "Freelancing - start offering your skills on platforms like Upwork, Fiverr, and Freelancer",
    "Dropshipping - start an online store without having to hold inventory",
    "Stocl Market - start investing in the stock market",
    "Affiliate Marketing - start promoting products and earn a commission for every sale you make",
    "Crypto Trading - start trading cryptocurrencies",
    "Online Courses - start creating and selling online courses",
    "Print on Demand - start selling custom products with your designs",
    "Blogging - start a blog and monetize it with ads, sponsored posts, and affiliate marketing",
    "YouTube Channel - start a YouTube channel and monetize it with ads and sponsored content",
    "Social Media Management - start managing social media accounts for businesses",
    "App Development - start developing mobile apps for clients",
    "Web Development - start building websites for clients",
    "Graphic Design - start offering graphic design services",
    "Virtual Assistant - start offering virtual assistant services",
    "Ebook Writing - start writing and selling ebooks",
    "Podcasting - start a podcast and monetize it with ads and sponsorships",
    "Online Tutoring - start offering online tutoring services",
    "SEO Consulting - start offering SEO consulting services",
    "Copywriting - start offering copywriting services",
    "Photography - start selling your photos online",
    "Ecommerce Store - start an online store selling physical products",
    "Online Coaching - start offering online coaching services",
    "Webinar Hosting - start hosting webinars and monetize them with ads and sponsorships",
    "Membership Site - start a membership site and charge a monthly fee for access to premium content",
    "Online Store - start an online store selling physical products",
    "Online Courses - start creating and selling online courses",
]


money_quotes = [
    "The best way to predict the future is to create it.",
    "Don't let the fear of losing be greater than the excitement of winning",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The best investment you can make is in yourself.",
    "The only way to do great work is to love what you do.",
    "The future belongs to those who believe in the beauty of their dreams.",
    
]

@app.get("/")
def read_root():
    return{
        "message" : "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote."
    }

@app.get("/side_hustles")
def get_side_hustles(): # insid (apikey: str) pass this apikey: str
    """Returns a random side hustle idea"""
    # if apikey != "1234567890":
        # return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(): # inside (apikey: str) pass this apikey: str
    """Returns a random money quote"""
    # if apikey != "1234567890":
        # return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}




