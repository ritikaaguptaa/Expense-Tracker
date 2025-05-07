# Copyright (c) 2025, Siddharth and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class PrimaryAccount(Document):
    def after_insert(self):
        self.create_user_with_role()
        self.assign_user_permission()

    def create_user_with_role(self):
        if not frappe.db.exists("User", self.email):

            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "roles": [{"role": "Expense Manager"}],
                "user_type": "System User"
            })
            user.insert(ignore_permissions=True)

    def assign_user_permission(self):
        user_permission = frappe.get_doc({
            "doctype": "User Permission",
            "user": self.email,
            "allow": "Primary Account",
            "for_value": self.name,
        })
        user_permission.insert(ignore_permissions=True)

# @frappe.whitelist()
# def send_email_to_dependent(email, name, primary_name, primary_id):
#     subject = "✨ You’ve Been Added as a Dependent on Finly!"

#     message = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <style>
#     body {{
#       margin: 0;
#       padding: 0;
#       background-color: #f2f4f8;
#       font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
#       color: #333;
#     }}
#     .container {{
#       max-width: 600px;
#       margin: 40px auto;
#       background: #ffffff;
#       border-radius: 16px;
#       overflow: hidden;
#       box-shadow: 0 8px 20px rgba(0,0,0,0.06);
#       border: 1px solid #e0e6ed;
#     }}
#     .header {{
#       background: linear-gradient(to right, #7f5af0, #6246ea);
#       text-align: center;
#       padding: 30px 20px;
#     }}
#     .header img {{
#       width: 150px;
#       margin-bottom: 10px;
#     }}
#     .header h1 {{
#       color: #ffffff;
#       font-size: 26px;
#       margin: 0;
#     }}
#     .content {{
#       padding: 30px 25px;
#     }}
#     .content h2 {{
#       color: #6246ea;
#       font-size: 22px;
#       margin-bottom: 15px;
#     }}
#     .content p {{
#       font-size: 16px;
#       line-height: 1.6;
#     }}
#     .id-box {{
#       border: 2px dotted #7f5af0;
#       background: #f9f5ff;
#       color: #3c096c;
#       font-size: 18px;
#       text-align: center;
#       padding: 14px;
#       border-radius: 10px;
#       margin: 20px 0;
#       font-weight: bold;
#     }}
#     .cta {{
#       text-align: center;
#       margin: 30px 0;
#     }}
#     .cta a {{
#       background: #6246ea;
#       color: white !important;
#       text-decoration: none;
#       padding: 14px 30px;
#       font-size: 16px;
#       border-radius: 8px;
#       font-weight: bold;
#       display: inline-block;
#       box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#       transition: background 0.3s ease;
#     }}
#     .cta a:hover {{
#       background: #7f5af0;
#     }}
#     .footer {{
#       text-align: center;
#       font-size: 12px;
#       color: #999;
#       padding: 20px;
#     }}
#     @media (max-width: 600px) {{
#       .content {{
#         padding: 20px 15px;
#       }}
#       .cta a {{
#         width: 100%;
#       }}
#     }}
#   </style>
# </head>
# <body>
#   <div class="container">
#     <div class="header">
#       <img src="https://yourdomain.com/assets/finly/logo.png" alt="Finly Logo">
#       <h1>Welcome to Finly 🎉</h1>
#     </div>
#     <div class="content">
#       <h2>Hey {name},</h2>
#       <p><strong>{primary_name}</strong> has added you as a dependent on <strong>Finly</strong>.</p>
#       <p>Here's your <strong>Parent ID</strong> (you’ll need it when starting the bot):</p>
#       <div class="id-box">{primary_id}</div>
#       <p style="color:#d7263d;"><strong>Important:</strong> Please don’t share this ID with anyone.</p>
#       <p>You're just one step away from managing your expenses with ease.</p>
#       <div class="cta">
#         <a href="http://t.me/XpenseTrackrbot" target="_blank">🚀 Start with Finly Bot</a>
#       </div>
#       <p>If you have any questions or need help, feel free to reach out. We're here for you!</p>
#       <p>Cheers,<br><strong>Team Finly 💜</strong></p>
#     </div>
#     <div class="footer">
#       &copy; 2025 Finly Inc. | Simplifying your financial life 💰
#     </div>
#   </div>
# </body>
# </html>
# """

#     try:
#         frappe.sendmail(
#             recipients=[email],
#             subject=subject,
#             message=message
#         )
#         return {"status": "success", "message": "Email sent successfully"}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}

@frappe.whitelist()
def send_email_to_dependent(email, name, primary_name, primary_id):
    subject = "🎉 You're Now a Dependent on Finly – Let’s Get Started!"

    message = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #f7f9fc;
      font-family: 'Times New Roman', serif;
      color: #333;
    }}
    .container {{
      max-width: 620px;
      margin: 40px auto;
      background: #fff;
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.06);
    }}
    .header {{
      background: linear-gradient(to right, #7f5af0, #6246ea);
      padding: 20px 30px 10px;
      text-align: center;
      position: relative;
    }}
    .header::before {{
      content: "🎉";
      font-size: 38px;
      position: absolute;
      top: 18px;
      left: 20px;
    }}
    .header img {{
      width: 110px;
      margin-bottom: 8px;
    }}
    .header h1 {{
      font-size: 22px;
      color: #fff;
      margin: 0;
      font-family: 'Arpey', serif;
    }}
    .confetti-bar {{
      text-align: center;
      background-color: #fff0f6;
      padding: 8px 20px;
      font-size: 13px;
      color: #d6336c;
      font-weight: bold;
      border-top: 1px dashed #f783ac;
      border-bottom: 1px dashed #f783ac;
    }}
    .content {{
      padding: 30px 30px;
    }}
    .content h2 {{
      color: #5f3dc4;
      font-size: 20px;
      margin-top: 0;
      font-family: 'Arpey', serif;
    }}
    .content p {{
      font-size: 15px;
      line-height: 1.6;
      margin-bottom: 16px;
    }}
    .id-box {{
      background: #f0f4ff;
      border: 2px dotted #5f3dc4;
      padding: 16px;
      border-radius: 12px;
      font-size: 18px;
      font-weight: bold;
      color: #3b28cc;
      text-align: center;
      margin: 20px 0;
      box-shadow: inset 0 1px 6px rgba(95, 61, 196, 0.1);
    }}
    .cta {{
      text-align: center;
      margin-top: 32px;
    }}
    .cta a {{
      background: #5f3dc4;
      color: #fff !important;
      text-decoration: none;
      padding: 14px 26px;
      border-radius: 10px;
      font-weight: 600;
      font-size: 16px;
      display: inline-block;
      transition: all 0.3s ease-in-out;
      box-shadow: 0 5px 20px rgba(95, 61, 196, 0.25);
      position: relative;
      overflow: hidden;
    }}
    .cta a::after {{
      content: "";
      position: absolute;
      top: -100%;
      left: -100%;
      width: 200%;
      height: 200%;
      background: rgba(255, 255, 255, 0.3); /* Wave color */
      animation: wave 2s infinite; /* Animation every 2 seconds */
    }}
    @keyframes wave {{
      0% {{
        top: -100%;
        left: -100%;
      }}
      50% {{
        top: 50%;
        left: 50%;
        transform: scale(1.5);
      }}
      100% {{
        top: 100%;
        left: 100%;
      }}
    }}
    .cta a:hover {{
      background: #3b28cc;
      box-shadow: 0 6px 24px rgba(59, 40, 204, 0.4);
    }}
    .footer {{
      text-align: center;
      font-size: 12px;
      color: #888;
      background: #f1f3f5;
      padding: 18px;
    }}
    @media (max-width: 600px) {{
      .content {{
        padding: 20px;
      }}
      .cta a {{
        width: 100%;
        box-sizing: border-box;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <img src="/assets/expense_tracker/images/finly.png" alt="Finly Logo">
      <h1>Welcome to Finly</h1>
    </div>
    <div class="confetti-bar">🎉 You've been successfully added as a dependent 🎉</div>
    <div class="content">
      <h2>Hi {name},</h2>
      <p><strong>{primary_name}</strong> has just added you as a dependent in <strong>Finly</strong> — your smart finance companion.</p>
      <p>Here’s your unique <strong>Parent ID</strong>. Keep it safe, you’ll need it to get started with our Telegram bot:</p>
      <div class="id-box">{primary_id}</div>
      <p><strong style="color:#d6336c;">⚠️ Please don't share this ID</strong> with anyone to ensure your account's security.</p>
      <p>You're now ready to manage expenses like a pro. It’s fast, simple, and secure.</p>
      <div class="cta">
        <a href="http://t.me/XpenseTrackrbot" target="_blank">🔗 Start with Finly</a>
      </div>
      <p style="margin-top: 30px;">Need assistance? We’re here to help anytime.</p>
      <p>With 💜 from Team Finly</p>
    </div>
    <div class="footer">
      &copy; 2025 Finly Inc. | Simplifying your financial life 💸
    </div>
  </div>
</body>
</html>
"""

    try:
        frappe.sendmail(
            recipients=[email],
            subject=subject,
            message=message
        )

        return {"status": "success", "message": "Email sent successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
