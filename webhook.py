import os
import requests
from dotenv import load_dotenv # type: ignore

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_URL = "https://two-korecent.frappe.cloud/api/method/expense_tracker.tasks.telegram_webhook"

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook",
    json={"url": WEBHOOK_URL}
)
