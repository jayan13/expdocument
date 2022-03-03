import frappe

def update_insurance_status():
    units=frappe.db.sql("""select name from  `tabInsurance`   where insurance_end_date < CURDATE() and insurance_end_date <> '' and status <>'Expired'  """)
    for unt in units:
        frappe.db.sql("""update `tabInsurance` set status ='Expired'  where name=%s """,unt[0])
        
    frappe.db.commit()



        