frappe.ui.form.on("Landed Cost Voucher", {
   custom_shipment_no(frm) {
       frm.doc.purchase_receipts = [];
       frm.refresh_field("purchase_receipts");
       frm.doc.taxes = [];
       frm.refresh_field("taxes");

       if (!frm.doc.custom_shipment_no) return;

       frappe.call({
           method: "tawalasoft_cargoflow.services.landed_cost_voucher.get_shipment_data",
           args: { shipment_no: frm.doc.custom_shipment_no },
           freeze: true,
           freeze_message: "Fetching shipment data...",
           callback(r) {
               if (!r.message) return;

               (r.message.purchase_receipts || []).forEach(function (row) {
                   let d = frm.add_child("purchase_receipts");
                   d.receipt_document_type = row.receipt_document_type;
                   d.receipt_document = row.receipt_document;
                   d.supplier = row.supplier;
                   d.posting_date = row.posting_date;
                   d.grand_total = row.grand_total;
               });
               frm.refresh_field("purchase_receipts");

               (r.message.taxes || []).forEach(function (row) {
                   let a = frm.add_child("taxes");
                   a.expense_account = row.expense_account;
                   a.description = row.description;
                   a.amount = row.amount;
                   a.purchase_invoice = row.purchase_invoice;
                   a.exchange_rate = row.exchange_rate;
                   a.account_currency = row.account_currency;
               });
               frm.refresh_field("taxes");
               frm.dirty();
           },
       });
   },
});