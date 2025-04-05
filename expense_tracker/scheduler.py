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
        today_india = datetime.now()

        last_week_start_india = today_india - timedelta(days=today_india.weekday()) - timedelta(days=7)
        last_week_end_india = last_week_start_india + timedelta(days=6)

        primary_accounts = frappe.get_all("Primary Account", fields=["telegram_id", "name"])

        for account in primary_accounts:
            chat_id = account["telegram_id"]

            expenses = frappe.db.sql("""
                SELECT category, SUM(amount) as total_spent
                FROM `tabExpense`
                WHERE user_id = %s
                AND `date` BETWEEN %s AND %s
                GROUP BY category
            """, (chat_id, last_week_start_india.strftime('%Y-%m-%d 00:00:00'), last_week_end_india.strftime('%Y-%m-%d 23:59:59')), as_dict=True)

            if not expenses:
                continue

            spending_details = "\n".join([f"📌 *{escape_markdown_v2(expense['category'])}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
📊 *Weekly Spending Summary* 📅
🔹 *Period:* {escape_markdown_v2(last_week_start_india.strftime('%d %b %Y'))} - {escape_markdown_v2(last_week_end_india.strftime('%d %b %Y'))}

💰 *Here's what you spent in each category:*
{spending_details}

🔹 *Keep track and plan ahead for next week!* 🚀
            """

            escaped_message = escape_markdown_v2(message)

            try:
                send_telegram_message(chat_id, escaped_message)
            except Exception as telegram_e:
                frappe.log_error(f"Error sending Telegram message to chat ID {chat_id}: {str(telegram_e)}", "Weekly Spending Summary")

        frappe.db.commit()

    except Exception as e:
        frappe.log_error(f"Error in Weekly Spending Summary: {str(e)}", "Weekly Spending Summary")

@frappe.whitelist(allow_guest=True)
def send_weekly_family_spending_summary():
    try:
        today_india = datetime.now()

        last_week_start_india = today_india - timedelta(days=today_india.weekday()) - timedelta(days=7)
        last_week_end_india = last_week_start_india + timedelta(days=6)

        family_members = frappe.get_all("Family Member", fields=["telegram_id", "name"])

        for member in family_members:
            chat_id = member["telegram_id"]
            member_id = member["name"]

            member_doc = frappe.get_doc("Family Member", member_id)
            member_name = member_doc.get("name")  # Access name from the document

            expenses = frappe.db.sql("""
                SELECT category, SUM(amount) as total_spent
                FROM `tabExpense`
                WHERE user_id = %s
                AND `date` BETWEEN %s AND %s
                GROUP BY category
            """, (chat_id, last_week_start_india.strftime('%Y-%m-%d 00:00:00'), last_week_end_india.strftime('%Y-%m-%d 23:59:59')), as_dict=True)

            if not expenses:
                continue

            spending_details = "\n".join([f"📌 *{escape_markdown_v2(expense['category'])}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
👨‍👩‍👦 *Weekly Spending Summary* 🧾
👤 *User:* {escape_markdown_v2(member_name) if member_name else 'N/A'}
🔹 *Period:* {escape_markdown_v2(last_week_start_india.strftime('%d %b %Y'))} - {escape_markdown_v2(last_week_end_india.strftime('%d %b %Y'))}

💰 *Here's what you spent in each category:*
{spending_details}
            """

            escaped_message = escape_markdown_v2(message)

            try:
                send_telegram_message(chat_id, escaped_message)
            except Exception as telegram_e:
                frappe.log_error(f"Error sending Telegram message to chat ID {chat_id} for Family Member {member_name}: {str(telegram_e)}", "Family Spending Summary")

        frappe.db.commit()

    except Exception as e:
        frappe.log_error(f"Error in Weekly Family Spending Summary: {str(e)}", "Family Spending Summary")

def escape_markdown_v2(text):
    """Escapes special characters for Telegram MarkdownV2."""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return ''.join('\\' + char if char in escape_chars else char for char in text)