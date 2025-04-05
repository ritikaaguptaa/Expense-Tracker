import re
import frappe
from datetime import datetime, timedelta
from expense_tracker.tasks import send_telegram_message_with_keyboard, send_telegram_message

@frappe.whitelist(allow_guest=True)
def monthly_add_money_reminder():
    primary_accounts = frappe.get_all("Primary Account", fields=["telegram_id", "full_name"])

    for account in primary_accounts:
        chat_id = account["telegram_id"]
        full_name = account["full_name"]

        message = f"""
        🔔 *Monthly Budget Reminder* 🔔  

        Hello {full_name},  
        It's the start of a new month! 🚀  
        Please ensure your budget is updated to manage your expenses smoothly.  

        ➕ Tap below to set your budget for this month! 👇
        """

        keyboard = [
            [{"text": "📊 Set Monthly Budget", "callback_data": "set_monthly_budget"}]
        ]
        
        escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_")
        send_telegram_message_with_keyboard(chat_id, escaped_message, keyboard)
        frappe.logger().info(f"Sent reminder to {full_name} ({chat_id})")

    frappe.logger().info("Monthly Budget Reminder completed.")
    return {"status": "success", "message": "Reminders sent to all users."}

@frappe.whitelist(allow_guest=True)
def send_weekly_parent_spending_summary():
    try:
        today = datetime.today()

        last_week_start = today - timedelta(days=today.weekday() + 7)
        last_week_end = last_week_start + timedelta(days=6)

        primary_accounts = frappe.get_all("Primary Account", fields=["telegram_id", "name"])

        for account in primary_accounts:
            chat_id = account["telegram_id"]

            expenses = frappe.db.sql("""
                SELECT category, SUM(amount) as total_spent
                FROM `tabExpense`
                WHERE user_id = %s
                AND date BETWEEN %s AND %s
                GROUP BY category
            """, (chat_id, last_week_start.strftime('%Y-%m-%d'), last_week_end.strftime('%Y-%m-%d')), as_dict=True)

            if not expenses:
                continue  

            spending_details = "\n".join([f"📌 *{expense['category']}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
📊 *Weekly Spending Summary* 📅  
🔹 *Period:* {last_week_start.strftime('%d %b %Y')} - {last_week_end.strftime('%d %b %Y')}  

💰 *Here's what you spent in each category:*  
{spending_details}  

🔹 *Keep track and plan ahead for next week!* 🚀
            """

            escaped_message = escape_markdown(message)
            send_telegram_message(chat_id, escaped_message)

        frappe.db.commit()

    except Exception as e:
        frappe.log_error(f"Error in Weekly Spending Summary: {str(e)}", "Weekly Spending Summary")

@frappe.whitelist(allow_guest=True)
def send_weekly_family_spending_summary():
    try:
        today = datetime.today()
        last_week_start = today - timedelta(days=today.weekday() + 7)
        last_week_end = last_week_start + timedelta(days=6)

        family_members = frappe.get_all("Family Member", fields=["telegram_id", "name"])

        for member in family_members:
            chat_id = member["telegram_id"]
            member_id = member["name"]

            member_name = frappe.get_doc("Family Member", member_id)

            expenses = frappe.db.sql("""
                SELECT category, SUM(amount) as total_spent
                FROM `tabExpense`
                WHERE user_id = %s
                AND date BETWEEN %s AND %s
                GROUP BY category
            """, (chat_id, last_week_start.strftime('%Y-%m-%d'), last_week_end.strftime('%Y-%m-%d')), as_dict=True)

            if not expenses:
                continue

            spending_details = "\n".join([f"📌 *{expense['category']}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
👨‍👩‍👦 *Weekly Spending Summary* 🧾  
👤 *User:* {member_name}  
🔹 *Period:* {last_week_start.strftime('%d %b %Y')} - {last_week_end.strftime('%d %b %Y')}  

💰 *Here's what you spent in each category:*  
{spending_details}  

            """

            escaped_message = escape_markdown(message)

            send_telegram_message(chat_id, escaped_message)

        frappe.db.commit()

    except Exception as e:
        frappe.log_error(f"Error in Weekly Family Spending Summary: {str(e)}", "Family Spending Summary")

def escape_markdown(text):
    escape_chars = r"[_*[\]()~`>#+\-=|{}.!]"
    return re.sub(f"([{escape_chars}])", r"\\\1", text)