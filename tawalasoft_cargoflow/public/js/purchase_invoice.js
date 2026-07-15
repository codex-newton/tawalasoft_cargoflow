frappe.ui.form.on("Purchase Invoice", {
   custom_purchase_invoice_type(frm) {
       frm.toggle_reqd(
           "custom_shipment_no",
           frm.doc.custom_purchase_invoice_type === "Landed Cost Invoice"
       );
   },

   refresh(frm) {
       frm.toggle_reqd(
           "custom_shipment_no",
           frm.doc.custom_purchase_invoice_type === "Landed Cost Invoice"
       );
   },
});