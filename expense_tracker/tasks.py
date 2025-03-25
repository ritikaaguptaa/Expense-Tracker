import frappe
import os
import requests
import asyncio
from deepgram import Deepgram
# from dotenv import load_dotenv
import google.generativeai as genai
import json
import re
import time

# # Load environment variables
# load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# def monthly_pocket_money_scheduler():
#     family_members = frappe.get_all("Family Member", fields=["full_name", "telegram_id", "pocket_money", "rollover_savings", "primary_account_holder"])
    
#     for member in family_members:
#         pocket_money = member.pocket_money or 0
#         rollover_savings = member.rollover_savings or 0

#         new_roll_over = rollover_savings + pocket_money
        
#         frappe.db.set_value("Family Member", member.name, {
#             "rollover_savings": new_roll_over,
#             "pocket_money": 0
#         })

#         current_month = datetime.datetime.now().strftime("%B")

#         message = f"""
#             💰 Monthly Savings Summary\\!

#             Hey {member.full_name}, here’s your savings update for {current_month}: 

#             Keep up the good savings habits\!
#         """

#         send_telegram_message(member.telegram_id, message)
    
    # primary_accounts = frappe.get_all("Primary Account", fields=["name", "total_expense", "default_pocket_money_for_dependents"])
    
    # for account in primary_accounts:
    #     frappe.db.set_value("Primary Account", account.name, "total_expense", 0)
    
    # for account in primary_accounts:
    #     family_members = frappe.get_all("Family Member", filters={"primary_account_holder": account.name}, fields=["name"])
        
    #     for member in family_members:
    #         frappe.db.set_value("Family Member", member.name, "pocket_money", account.default_pocket_money_for_dependents)
        
    #     total_expenses = account.default_pocket_money_for_dependents * len(family_members)
    #     frappe.db.set_value("Primary Account", account.name, "total_expense", total_expenses)
    
    # frappe.db.commit()



# def monthly_savings_summary():
#     family_members = frappe.get_all(
#         "Family Member",
#         fields=["full_name", "telegram_id", "pocket_money", "primary_account_holder"],
#     )

#     current_month = datetime.datetime.now().strftime("%B")
    
#     for member in family_members:
#         chat_id = member.telegram_id.strip()
        
#         total_expenses = frappe.db.get_value(
#             "Expense Entry",
#             {"associated_account_holder": member.primary_account_holder},
#             "SUM(amount)"
#         ) or 0.0
        
#         savings = max(0, member.pocket_money - total_expenses)
        
#         message = f"""
#             💰 Monthly Savings Summary\!

#             Hey {member.full_name}, here’s your savings update for {current_month}: 

#             🏦 Pocket Money Given\: {member.pocket_money:.2f} INR  
#             💸 Total Expenses\: {total_expenses:.2f} INR  
#             💰 Savings This Month\: {savings:.2f} INR  

#             Keep up the good savings habits\!
#         """
        
#         message = message.replace(":.2f", ":\\.2f")  # Escape dots for Telegram MarkdownV2
        
#         print(message)  # Debugging
#         send_telegram_message(chat_id, message)


def get_audio_file_path():
    """Fetch the latest uploaded audio file path from File Doctype."""
    file_doc = frappe.get_list("File", 
                               filters={"file_url": "/files/food.mp4"}, 
                               fields=["file_url"], 
                               limit=1)

    if file_doc:
        file_url = file_doc[0]["file_url"]  # "/files/food.mp4"
        site_path = frappe.get_site_path("public", file_url.lstrip("/"))  # Convert to absolute path
        return site_path
    return None

async def transcribe_audio_async():
    """Asynchronous function to transcribe audio using Deepgram API."""
    try:
        audio_path = get_audio_file_path()
        if not audio_path:
            print("No audio file found.")
            return None

        deepgram = Deepgram(DEEPGRAM_API_KEY)

        with open(audio_path, "rb") as audio:
            buffer_data = audio.read()

        options = {
            "punctuate": True,
            "model": "nova",
            "language": "en",
        }

        response = await deepgram.transcription.prerecorded(
            {"buffer": buffer_data, "mimetype": "audio/mp4"},
            options
        )

        transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        # print("Transcription:", transcript)

        escaped_transcript = transcript.replace(".", "\\.").replace("!", "\\!")

        message = """
        ⏳ *Processing...* 🎙️  
  
Hold tight! We're transcribing your audio...   
        """

        message = message.replace(".", "\\.").replace("!", "\\!")

        send_telegram_message("6155394022", message)
        time.sleep(2)
        message1 = """
Almost Done\!
"""
        send_telegram_message("6155394022", message1) 
        time.sleep(4)
        extract_and_notify(transcript, escaped_transcript, "6155394022") 
        return transcript

    except Exception as e:
        print(f"Error in transcription: {e}")
        return None

def extract_details_from_text(text):
    """Uses Gemini AI to extract structured details from text."""
    try:
        genai.configure(api_key=GEMINI_API_KEY)

        prompt = f"""
        Extract structured details from the following text:
        "{text}"

        Output the details in **strict** JSON format with these keys:
        - amount (numeric, float)
        - category (string, like Food, Transport, etc.)
        - merchant (string, store or service name)

        Example output (no additional text, just JSON):
        {{
            "amount": 120.50,
            "category": "Food",
            "merchant": "Dominos"
        }}
        """

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt)

        # Ensure response is in JSON format
        extracted_data = response.text.strip()

        # Debugging: Print the raw response
        print("Raw Gemini Response:", extracted_data)

        # Remove backticks and unnecessary formatting
        cleaned_json = re.sub(r"```json|```", "", extracted_data).strip()

        # Try parsing JSON safely
        try:
            details = json.loads(cleaned_json)
        except json.JSONDecodeError:
            print("Error: Gemini response is not valid JSON")
            return None

        print("Extracted Details:", details)
        return details

    except Exception as e:
        print(f"Error in extracting details: {e}")
        return None

    
def transcribe_audio():
    """Wrapper to run async function in sync mode using asyncio.run()"""
    return asyncio.run(transcribe_audio_async())

@frappe.whitelist(allow_guest=True)
def process_and_notify():
    """Transcribe audio and send it as a Telegram message."""
    return transcribe_audio()  

def escape_markdown_v2(text):
    """Escapes special characters for Telegram MarkdownV2."""
    if text is None:
        return "Unknown"  # Ensure None values are converted to safe text
    
    escape_chars = r"_*[]()~`>#+-=|{}.!"
    return re.sub(r"([" + re.escape(escape_chars) + r"])", r"\\\1", str(text))  # Ensure conversion to string

def extract_and_notify(text, escaped_transcript, chat_id):
    """Extract details from text and send as a Telegram notification."""
    extracted_details = extract_details_from_text(text)
    
    if extracted_details:
        # Ensure values are escaped properly
        amount = escape_markdown_v2(f"{extracted_details.get('amount', 'N/A'):.2f}")  # Force two decimal places for consistency
        category = escape_markdown_v2(extracted_details.get("category", "N/A"))
        merchant = escape_markdown_v2(extracted_details.get("merchant", "N/A"))  # Handle None safely
        
        message = f"""
    🎙️ *Transcription Complete\!*

*{escaped_transcript}*

💡 *Expense Details Extracted* 💡

💰 *Amount:* {amount}  
📂 *Category:* {category}  
🏪 *Merchant:* {merchant}  

✅ *This record has been automatically saved in the Expense Doctype\!*

📊 _Effortless tracking for smarter spending\!_ 
        """

        send_telegram_message(chat_id, message)

        expense = frappe.get_doc({
            "doctype": "Expense",
            "user_id": chat_id,
            "amount": extracted_details.get("amount", 0.0),
            "category": category,
            "merchant": merchant,  # Handling None case
            "date": frappe.utils.now_datetime(),
            "description": text,
            "payment_mode": "Cash",
            "source": "Telegram Bot"
        })
            
        expense.insert(ignore_permissions=True)
        frappe.db.commit()
    else:
        send_telegram_message(chat_id, "❌ Sorry, we couldn't extract the details from the text provided.")

# def weekly_spending_summary():

#     family_members = frappe.get_all(
#         "Family Member",
#         fields=["full_name", "telegram_id", "pocket_money", "primary_account_holder"],
#     )

#     current_week = datetime.datetime.now().isocalendar()[1]
#     total_weeks = 4

#     remaining_weeks = total_weeks - ((current_week - 1) % total_weeks)

#     for member in family_members:

#         chat_id = member.telegram_id.strip()

#         categories = frappe.get_all(
#             "Expense Category",
#             filters={"associated_account_holder": member.primary_account_holder},
#             fields=["category_type"],
#         )

#         category_names = [cat["category_type"] for cat in categories]

#         weekly_budget = member.pocket_money / remaining_weeks

#         def escape_dots(text):
#             return str(text).replace(".", "\\.")

#         suggestions = [f"Consider spending around *{weekly_budget:.2f}* per week."]
#         if "Food" in category_names:
#             suggestions.append("🍽️ Prioritize meals over snacks to save more!")
#         if "Entertainment" in category_names:
#             suggestions.append(
#                 "🎬 Keep entertainment spending within limits for a balanced budget."
#             )
#         if "Transport" in category_names:
#             suggestions.append("🚖 Use public transport or pooling to save costs.")

#         name = member.full_name
#         pockey_money_left = member.pocket_money

#         message = f"""
#             *📊 Weekly Spending Summary\\!*

#             Hey {name}, here’s your spending insight for the remaining {remaining_weeks} weeks:

#             🏦 *Pocket Money Left\\:* {pockey_money_left:.2f} INR  
#             📌 *Remaining Weeks\\:* {remaining_weeks}  
#             🔖 *Allowed Categories\\:* {', '.join(category_names)}

#             🔹 {suggestions[0]}
#             🔹 {suggestions[1] if len(suggestions) > 1 else ''}

#             _Plan wisely and make the most out of your budget\\!_
#         """

#         message = message.replace(":.2f", ":\\.2f") #escape the dot here.

#         print(message)

#         send_telegram_message(chat_id, message)


def send_telegram_message(chat_id, message):

    bot_token = os.getenv("BOT_TOKEN")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "MarkdownV2"}

    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        print(response_data)

        if not response_data.get("ok"):
            frappe.logger().error(f"Failed to send Telegram notification: {response_data}")
    except Exception as e:
        frappe.logger().error(f"Error sending Telegram message: {str(e)}")

def send_telegram_message_with_keyboard(chat_id, message, keyboard):
    bot_token = os.getenv("BOT_TOKEN")

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "MarkdownV2",
        "reply_markup": json.dumps({"inline_keyboard": keyboard}) 
    }

    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        print(response_data)

        if not response_data.get("ok"):
            frappe.logger().error(f"Failed to send Telegram notification: {response_data}")
    except Exception as e:
        frappe.logger().error(f"Error sending Telegram message: {str(e)}")

# @frappe.whitelist(allow_guest=True)  
# def telegram_webhook():
#     try:
#         data = frappe.request.get_data(as_text=True)
#         data = json.loads(data)

#         if "message" in data:
#             chat_id = data["message"]["chat"]["id"]
#             text = data["message"].get("text", "")

#             if text == "/start":
#                 send_telegram_message(chat_id, "Hello you are now registered for updates")

#         return {"ok": True}
    
#     except Exception as e:
#         frappe.log_error(f"Telegram Webhook Error: {str(e)}")
#         return {"ok": False, "error": str(e)}

@frappe.whitelist(allow_guest=True)  
def telegram_webhook():
    try:
        data = frappe.request.get_data(as_text=True)
        data = json.loads(data)

        if "callback_query" in data:
            callback_query = data["callback_query"]
            chat_id = callback_query["message"]["chat"]["id"]
            callback_data = callback_query["data"]

            frappe.cache().set_value(f"callback_{chat_id}", callback_data)

            if callback_data == "role_parent":
                message = "Please enter your **Parent ID** to continue."
                escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                send_telegram_message(chat_id, escaped_message)

            elif callback_data == "role_dependent":
                message = "Please enter your **Parent ID** for verification."
                escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                send_telegram_message(chat_id, escaped_message)

            return {"ok": True}

        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            first_name = data["message"]["from"].get("first_name", "User")
            last_name = data["message"]["from"].get("last_name", "")
            text = data["message"].get("text", "")

            if text == "/start":
                welcome_message = (
                    "👋 Welcome to **ExpenseTrackerBot**! 📊💰\n\n"
                    "To get started, please select your role:\n\n"
                    "👨‍👩‍👧‍👦 **Are you a Parent or a Dependent?**"
                )

                keyboard = {
                    "inline_keyboard": [
                        [{"text": "Parent", "callback_data": "role_parent"}],
                        [{"text": "Dependent", "callback_data": "role_dependent"}]
                    ]
                }

                escaped_message = welcome_message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                send_telegram_message_with_keyboard(chat_id, escaped_message, keyboard)

            elif "voice" in data["message"]:
                voice_file_id = data["message"]["voice"]["file_id"]
                file_url = get_telegram_file_url(voice_file_id)

                if file_url:
                    file_doc = frappe.get_doc({
                        "doctype": "File",
                        "file_name": f"voice_{chat_id}.ogg",
                        "file_url": file_url,
                        "is_private": 1
                    })
                    file_doc.insert(ignore_permissions=True)

                    process_and_notify(file_doc.file_url) # type: ignore

            else:

                user_role = frappe.cache().get_value(f"callback_{chat_id}")
                
                if user_role is None:
                    prompt = f"""
                    You are an AI assistant managing a Telegram Expense Tracker bot. 
                    A user has sent the following message: "{text}"

                    1️⃣ **If the message contains personal information** (like phone numbers, emails, addresses, etc.), 
                    reply: "🚨 Please avoid sharing personal information. This bot is only for tracking expenses."
                    
                    2️⃣ **If the message contains abusive or inappropriate language**, 
                    reply: "⚠️ Please maintain respectful communication. Let's keep this space friendly."
                    
                    3️⃣ **If it's a general query**, provide a polite response explaining the bot’s features and how it can help.
                    """

                    genai.configure(api_key=GEMINI_API_KEY)
                    model = genai.GenerativeModel("gemini-1.5-pro-latest")

                    ai_response = model.generate_content(prompt).text
                    send_telegram_message(chat_id, ai_response)
                else:
                    parent_exists = frappe.db.exists("Primary Account", text)

                    if not parent_exists:
                        message = "❌ Invalid Parent ID. Please try again."
                        escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                        send_telegram_message(chat_id, escaped_message)
                        return {"ok": False, "error": "Invalid Parent ID"}
                    
                    if user_role == "role_parent":
                        message = "🎉 **You are verified as a Parent!** Now, track your expenses daily! 💳"
                        escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                        send_telegram_message(chat_id, escaped_message)
                    
                    else:  
                        if frappe.db.exists("Family Member", {"telegram_id": chat_id}):
                            message = "✅ **You're already registered!** Start tracking your expenses now. 📊"
                            escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                            send_telegram_message(chat_id, escaped_message)
                            return {"ok": True}
                        
                        main_user = frappe.get_doc("Primary Account", text)

                        family_member_doc = frappe.get_doc({
                            "doctype": "Family Member",
                            "primary_account_holder": text,  
                            "full_name": f"{first_name} {last_name}",  
                            "pocket_money": main_user.default_pocket_money_for_dependents,   
                            "telegram_id": chat_id
                        })
                        family_member_doc = frappe.get_doc({
                            "doctype": "Family Member",
                            "parent_id": text,
                            "telegram_id": chat_id
                        })
                        family_member_doc.insert(ignore_permissions=True)

                        main_user.salary -= main_user.default_pocket_money_for_dependents
                        main_user.save(ignore_permissions=True)

                        message = "🎉 **You are verified as a Dependent!** Now, track your expenses daily! 🏦"
                        escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_") 
                        send_telegram_message(chat_id, escaped_message)

                    frappe.cache().delete_value(f"callback_{chat_id}")

                    return {"ok": True}

        return {"ok": True}
    
    except Exception as e:
        frappe.log_error(f"Telegram Webhook Error: {str(e)}")
        return {"ok": False, "error": str(e)}
    
def get_telegram_file_url(file_id):
    bot_token = os.getenv("BOT_TOKEN")  
    api_url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    
    response = requests.get(api_url).json()
    
    if response.get("ok"):
        file_path = response["result"]["file_path"]
        return f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
    
    return None