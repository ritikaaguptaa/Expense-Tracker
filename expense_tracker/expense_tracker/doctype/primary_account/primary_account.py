# Copyright (c) 2025, Siddharth and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

class PrimaryAccount(Document):
    def validate(self):
        if self.telegram_id:
            self.telegram_id = self.telegram_id.strip()  
            if not self.telegram_id.isdigit() or not (9 <= len(self.telegram_id) <= 12):
                frappe.throw("Telegram ID must be a numeric value between 9 and 12 digits.")
