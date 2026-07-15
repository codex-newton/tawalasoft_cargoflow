import frappe


@frappe.whitelist()
def get_shipment_data(shipment_no):
    return {
        "purchase_receipts": _get_purchase_receipts(shipment_no),
        "taxes": _get_landed_cost_invoices(shipment_no),
    }


def before_save(doc, method=None):
    _sync_tax_details(doc)


def _get_purchase_receipts(shipment_no):
    rows = frappe.db.sql(
        """
        SELECT name, posting_date, base_rounded_total, base_grand_total, supplier
        FROM `tabPurchase Receipt`
        WHERE docstatus = 1 AND custom_shipment_no = %s
        ORDER BY posting_date, name
        """,
        (shipment_no,),
        as_dict=True,
    )

    return [
        {
            "receipt_document_type": "Purchase Receipt",
            "receipt_document": r.name,
            "supplier": r.supplier,
            "posting_date": r.posting_date,
            "grand_total": r.base_rounded_total or r.base_grand_total,
        }
        for r in rows
    ]


def _get_landed_cost_invoices(shipment_no):
    rows = frappe.db.sql(
        """
        SELECT
            p.name,
            p.conversion_rate,
            p.currency,
            c.expense_account,
            c.net_amount,
            c.base_net_amount
        FROM `tabPurchase Invoice` p
        INNER JOIN `tabPurchase Invoice Item` c ON p.name = c.parent
        WHERE p.docstatus = 1
            AND p.custom_shipment_no = %s
            AND p.custom_purchase_invoice_type = 'Landed Cost Invoice'
            AND c.expense_account NOT LIKE '%%Stock Received But Not Billed%%'
        ORDER BY p.posting_date, p.name, c.idx
        """,
        (shipment_no,),
        as_dict=True,
    )

    return [
        {
            "expense_account": r.expense_account,
            "description": r.expense_account,
            "amount": r.net_amount,
            "purchase_invoice": r.name,
            "exchange_rate": r.conversion_rate or 1,
            "account_currency": r.currency,
        }
        for r in rows
    ]

def _sync_tax_details(doc):
    invoice_cache = {}

    for row in doc.taxes:
        if hasattr(row, "custom_purchase_invoice") and row.custom_purchase_invoice:
            if row.custom_purchase_invoice not in invoice_cache:
                invoice_cache[row.custom_purchase_invoice] = frappe.db.get_value(
                    "Purchase Invoice",
                    row.custom_purchase_invoice,
                    ["conversion_rate", "currency"],
                    as_dict=True,
                )

            pi = invoice_cache[row.custom_purchase_invoice]
            if pi:
                if not row.exchange_rate:
                    row.exchange_rate = pi.conversion_rate or 1
                if not row.account_currency:
                    row.account_currency = pi.currency

        if row.expense_account and not row.description:
            row.description = row.expense_account