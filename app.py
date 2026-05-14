from flask import Flask, render_template, jsonify, Response
import random
import requests

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "Life is what happens to you while you're busy making other plans. - John Lennon",
    "The mind is everything. What you think you become. - Buddha",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "The only impossible journey is the one you never begin. - Tony Robbins"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({
        'quote': quote,
        'total_quotes': len(quotes)
    })

@app.route('/generated-image')
def generated_image():
    image_url = (
        "https://image.pollinations.ai/prompt/"
        "A%20beautiful%20inspirational%20quote%20background"
        "?width=1024&height=576"
    )

    response = requests.get(
        image_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=60,
        verify=False,
        proxies={"http": "", "https": ""}
    )
    response.raise_for_status()

    if not response.content:
        return Response("Generated image is empty", status=502)

    return Response(response.content, content_type=response.headers.get("Content-Type", "image/jpeg"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
