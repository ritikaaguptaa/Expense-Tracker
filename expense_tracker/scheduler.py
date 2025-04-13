import re
import frappe
import textwrap
from datetime import datetime, timedelta
from expense_tracker.tasks import send_telegram_message_with_keyboard, send_telegram_message

# @frappe.whitelist(allow_guest=True)
# def monthly_add_money_reminder():
#     primary_accounts = frappe.get_all("Primary Account", fields=["telegram_id", "full_name"])

#     for account in primary_accounts:
#         chat_id = account["telegram_id"]
#         full_name = account["full_name"]

#         message = f"""
#         🔔 *Monthly Budget Reminder* 🔔  

#         Hello {full_name},  
#         It's the start of a new month! 🚀  
#         Please ensure your budget is updated to manage your expenses smoothly.  

#         ➕ Tap below to set your budget for this month! 👇
#         """
#         message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*")

#         keyboard = [
#             [{"text": "📊 Set Monthly Budget", "callback_data": "set_monthly_budget"}]
#         ]
        
#         escaped_message = message.replace(".", "\\.").replace("!", "\\!").replace("*", "\\*").replace("_", "\\_")
#         send_telegram_message_with_keyboard(chat_id, escaped_message, keyboard)
#         frappe.logger().info(f"Sent reminder to {full_name} ({chat_id})")

#     frappe.logger().info("Monthly Budget Reminder completed.")
#     return {"status": "success", "message": "Reminders sent to all users."}

def es_markdown_v2(text):
    escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    return "".join(f"\\{char}" if char in escape_chars else char for char in text)

@frappe.whitelist(allow_guest=True)
def monthly_add_money_reminder():
    primary_accounts = frappe.get_all("Primary Account", fields=["telegram_id", "full_name"])

    for account in primary_accounts:
        chat_id = account.get("telegram_id")
        full_name = account.get("full_name")

        if not chat_id:
            frappe.logger().warning(f"Skipping user {full_name} due to missing Telegram ID")
            continue

        message = textwrap.dedent(f"""
        🔔 *Monthly Budget Reminder* 🔔  

        Hello {full_name},  
        It's the start of a new month! 🚀  
        Please ensure your budget is updated to manage your expenses smoothly.  

        ➕ Tap below to set your budget for this month! 👇
        """)
        escaped_message = es_markdown_v2(message)

        keyboard = [
            [{"text": "📊 Set Monthly Budget", "callback_data": "set_monthly_budget"}]
        ]
        
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

            spending_details = "\n".join([f"📌 *{es_markdown_v2(expense['category'])}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
📊 *Weekly Spending Summary* 📅
🔹 *Period:* {es_markdown_v2(last_week_start_india.strftime('%d %b %Y'))} - {es_markdown_v2(last_week_end_india.strftime('%d %b %Y'))}

💰 *Here's what you spent in each category:*
{spending_details}

🔹 *Keep track and plan ahead for next week!* 🚀
            """

            escaped_message = es_markdown_v2(message)

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
            member_name = member_doc.get("full_name") 

            expenses = frappe.db.sql("""
                SELECT category, SUM(amount) as total_spent
                FROM `tabExpense`
                WHERE user_id = %s
                AND `date` BETWEEN %s AND %s
                GROUP BY category
            """, (chat_id, last_week_start_india.strftime('%Y-%m-%d 00:00:00'), last_week_end_india.strftime('%Y-%m-%d 23:59:59')), as_dict=True)

            if not expenses:
                continue

            spending_details = "\n".join([f"📌 *{es_markdown_v2(expense['category'])}*: ₹{expense['total_spent']}" for expense in expenses])

            message = f"""
👨‍👩‍👦 *Weekly Spending Summary* 🧾
👤 *User:* {es_markdown_v2(member_name) if member_name else 'N/A'}
🔹 *Period:* {es_markdown_v2(last_week_start_india.strftime('%d %b %Y'))} - {es_markdown_v2(last_week_end_india.strftime('%d %b %Y'))}

💰 *Here's what you spent in each category:*
{spending_details}
            """

            escaped_message = es_markdown_v2(message)

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

@frappe.whitelist(allow_guest=True)
def notify_family_on_low_pocket_money():
    family_members = frappe.get_all(
        "Family Member", fields=["name", "full_name", "pocket_money", "telegram_id", "primary_account_holder"]
    )

    for member in family_members:
        member_full_name = member.get("full_name")
        member_telegram_id = member.get("telegram_id")
        member_pocket_money = member.get("pocket_money")
        primary_account_holder = member.get("primary_account_holder")

        if not member_telegram_id or member_pocket_money is None:
            frappe.logger().warning(f"Skipping {member_full_name} due to missing Telegram ID or pocket money")
            continue

        primary_account = frappe.get_value(
            "Primary Account", 
            {"name": primary_account_holder}, 
            "default_pocket_money_for_dependents"
        )

        if not primary_account:
            frappe.logger().warning(f"No primary account found for {member_full_name}")
            continue

        default_pocket_money = primary_account
        low_pocket_money_threshold = default_pocket_money * 0.2  

        if member_pocket_money < low_pocket_money_threshold:
            message = f"""
            ⚠️ *Low Pocket Money Alert* ⚠️

            Hello {member_full_name},  
            Your remaining pocket money is {member_pocket_money}, which is below the threshold.  

            Please make sure to manage your expenses or reach out to your primary account holder to update your pocket money.
            """
            escaped_message = message.replace(".", "\\.").replace("!", "\\!")
            
            send_telegram_message(member_telegram_id, escaped_message)
            frappe.logger().info(f"Sent low pocket money alert to {member_full_name} ({member_telegram_id})")

    frappe.logger().info("Low Pocket Money Notification completed.")
    return {"status": "success", "message": "Low pocket money reminders sent to all family members."}


@frappe.whitelist(allow_guest=True)
def notify_dependents_about_savings():
    family_members = frappe.get_all(
        "Family Member", fields=["name", "full_name", "pocket_money", "telegram_id", "rollover_savings"]
    )

    for member in family_members:
        member_name = member.get("name")
        member_full_name = member.get("full_name")
        member_telegram_id = member.get("telegram_id")
        member_pocket_money = member.get("pocket_money", 0)
        # member_total_expense = member.get("total_expense", 0)
        member_rollover_savings = member.get("rollover_savings", 0)

        if not member_telegram_id:
            frappe.logger().warning(f"Skipping {member_full_name} due to missing Telegram ID")
            continue

        # remaining_pocket_money = max(0, member_pocket_money - member_total_expense)
        new_rollover_savings = member_rollover_savings + member_pocket_money

        frappe.db.set_value("Family Member", member_name, "rollover_savings", new_rollover_savings)

        message = f"""
        🏦 *Monthly Savings Update* 🏦

        Hello {member_full_name},  
        At the end of this month, you have saved {member_pocket_money} from your pocket money.  
        Your total savings now stand at {new_rollover_savings}. 🎉

        Keep up the good work in managing your expenses!
        """
        escaped_message = message.replace(".", "\\.").replace("!", "\\!")

        send_telegram_message(member_telegram_id, escaped_message)
        frappe.logger().info(f"Sent savings update to {member_full_name} ({member_telegram_id})")

    frappe.logger().info("Savings Notification completed.")
    return {"status": "success", "message": "Savings notifications sent to all dependents."}

@frappe.whitelist(allow_guest=True)
def budget_health_checker():
    low_threshold = 500  
    critical_threshold = 100 

    categories = frappe.get_all("Expense Category", fields=["name", "budget", "associated_account_holder"])

    for category in categories:
        remaining = category.budget or 0

        if remaining > low_threshold:
            continue  

        telegram_id = frappe.db.get_value("Primary Account", category.associated_account_holder, "telegram_id")
        if not telegram_id:
            continue

        level = "critical" if remaining <= critical_threshold else "warning"
        message = get_alert_message(category.name, remaining, level).replace(".", "\\.").replace("!", "\\!")

        send_telegram_message(telegram_id, message)

def get_alert_message(category_name, remaining, level):
    emoji = "🚨" if level == "critical" else "⚠️"
    title = "Budget Critically Low!" if level == "critical" else "Budget Running Low"

    return f"""
*{emoji} {title}*

*Category:* `{category_name}`
*Remaining Budget:* ₹{remaining:,.2f}

_{'Please avoid further expenses in this category.' if level == 'critical' else 'Keep an eye on your spending here.'}_
    """.strip()