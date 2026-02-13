from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "webhooks.log"

@app.route("/webhook", methods=["POST"])
def webhook():
    """Receives webhooks and saves to file"""
    
    # Get the data
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log to console
    print(f"\n[{timestamp}] Webhook received:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    
    # Save to file
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
        f.write("\n")
    
    return {"status": "ok"}, 200

@app.route("/", methods=["GET"])
def home():
    return "Webhook bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)