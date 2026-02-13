from flask import Flask, request
import json
import logging
import sys
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('webhooks.log')
    ]
)

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    """Receives webhooks and saves to file"""
    
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    logger.info(f"Webhook received at {timestamp}")
    logger.info(f"Data: {json.dumps(data, indent=2, ensure_ascii=False)}")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- {timestamp} ---\n")
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
        f.write("\n")
    
    return {"status": "ok"}, 200

@app.route("/", methods=["GET"])
def home():
    logger.info("Home page accessed")
    return "Webhook bot is running!"

if __name__ == "__main__":
    logger.info("Starting webhook bot...")
    app.run(host="0.0.0.0", port=5000, debug=True)