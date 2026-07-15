import frappe


def validate(doc, method=None):
    if doc.custom_purchase_invoice_type == "Landed Cost Invoice" and not doc.custom_shipment_no:
        frappe.throw(
            "Shipment No is mandatory when Purchase Invoice Type is <b>Landed Cost Invoice</b>.",
            title="Missing Shipment No",
        )