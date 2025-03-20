import asyncio
import os
import json
import requests
import google.generativeai as genai
import frappe
from deepgram import Deepgram
from dotenv import load_dotenv

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

AUDIO_FILE_PATH = "expense_tracker/food.mp4"


def send_telegram_notification():

    bot_token = BOT_TOKEN
    # chat_id = self.telegram_id.strip()

    # if not bot_token or not chat_id:
    #     frappe.logger().error("Telegram bot token or chat ID is missing.")
    #     return

    # merchant = expense_data.get("merchant", "Unknown Merchant")
    # category = expense_data.get("category", "General")
    # amount = expense_data.get("amount", 0.00)
    # currency = expense_data.get("currency", "INR")

    # message = f"""
    # *🛒 Expense Alert!* 💸

    # You have spent *{currency} {amount:.2f}* at *{merchant}*
    # 📌 *Category:* {category}

    # _Track your expenses wisely! 📊_
    # """

    # url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # payload = {
    #     "chat_id": chat_id,
    #     "text": message,
    #     "parse_mode": "MarkdownV2"
    # }

    # try:
    #     response = requests.post(url, json=payload)
    #     response_data = response.json()

    #     if not response_data.get("ok"):
    #         frappe.logger().error(f"Failed to send Telegram notification: {response_data}")
    # except Exception as e:
    #     frappe.logger().error(f"Error sending Telegram message: {str(e)}")


def transcribe_audio_sync():
    """Runs async transcription function in a synchronous wrapper."""
    return asyncio.run(transcribe_audio())


async def transcribe_audio():
    """Asynchronous function to transcribe audio using Deepgram API."""
    try:
        deepgram = Deepgram(DEEPGRAM_API_KEY)

        with open(AUDIO_FILE_PATH, "rb") as audio:
            buffer_data = audio.read()

        options = {
            "punctuate": True,
            "model": "nova",
            "language": "en",
        }

        response = await deepgram.transcription.prerecorded(
            {"buffer": buffer_data, "mimetype": "audio/mp4"}, options
        )

        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        print("Transcription:", transcript)
        return transcript

    except Exception as e:
        print(f"Error in transcription: {e}")
        return None


@frappe.whitelist(allow_guest=True)
def extract_details_from_text(text):
    """Uses Gemini AI to extract structured details from text."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)

        prompt = f"""
        Extract structured details from the following text:
        "{text}"

        Output the details in valid JSON format with keys:
        - amount (numeric)
        - category (string, like Food, Transport, etc.)
        - merchant (string, store or service name)

        Example output:
        {{
            "amount": 120.50,
            "category": "Food",
            "merchant": "Dominos"
        }}
        """

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)

        extracted_data = response.text

        # Convert response to JSON
        details = json.loads(extracted_data)
        print("Extracted Details:", details)
        return details

    except Exception as e:
        print(f"Error in extracting details: {e}")
        return None


@frappe.whitelist(allow_guest=True)
def create_expense_in_frappe(details):
    """Creates a new expense entry in Frappe."""
    try:
        doc = frappe.get_doc(
            {
                "doctype": "Expense",
                "amount": details["amount"],
                "category": details["category"],
                "merchant": details["merchant"],
                "status": "Pending",
            }
        )
        doc.insert(ignore_permissions=True)
        frappe.db.commit()  # Ensure changes are saved
        print("Expense entry created successfully!")

    except Exception as e:
        print(f"Error in creating expense entry: {e}")


@frappe.whitelist(allow_guest=True)
def main():
    """Runs the entire pipeline synchronously."""
    try:
        frappe.init("project-bench", sites_path="sites")  # added sites_path
        frappe.connect("expensetracker.localhost")  # added site name
        transcript = transcribe_audio_sync()  # Run async function synchronously
        if transcript:
            details = extract_details_from_text(transcript)
            if details:
                create_expense_in_frappe(details)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        frappe.destroy()  # close frappe connection.


if __name__ == "__main__":
    main()
