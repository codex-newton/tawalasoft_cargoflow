import frappe


def after_install():
    invoice_types = [
        "Landed Cost Invoice",
        "Service Invoice",
        "Purchase Invoice",
    ]

    for name in invoice_types:
        if not frappe.db.exists("Purchase Invoice Type", name):
            doc = frappe.get_doc({
                "doctype": "Purchase Invoice Type",
                "name1": name,
            })
            doc.insert(ignore_permissions=True)
            frappe.db.commit()

    frappe.msgprint("Purchase Invoice Types created successfully.")