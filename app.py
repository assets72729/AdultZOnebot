'''
Smile, please... 😊
Goodbye forever.

Thank you all for your care and support throughout this journey.

Unfortunately, my @dypixx account has been hacked. The hacker is now using it to promote unknown content. Please be cautious, stay alert, and don’t fall for anything they post.

Take care, stay safe — and once again, thank you for everything.
Goodbye.

— Dypixx
'''

from flask import Flask, Response
import requests
app = Flask(__name__)

@app.route('/')
def show_github_html():
    response = requests.get('https://raw.githubusercontent.com/Dypixx/live/main/index.html')
    return Response(response.text, mimetype='text/html') if response.status_code == 200 else ("Bot is LIVE", 500)

if __name__ == "__main__":
    app.run()
