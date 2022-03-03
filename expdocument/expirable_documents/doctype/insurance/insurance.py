# Copyright (c) 2022, alantechnologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Insurance(Document):
	def before_insert(self):
		if self.previous_policy_number:
			frappe.db.sql("""update `tabInsurance` set `new_policy_number`='{policy_number}' where name='{previous_policy_number}' """.format(policy_number=self.policy_number, previous_policy_number=self.previous_policy_number))
			
			

