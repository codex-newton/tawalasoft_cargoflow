app_name = "tawalasoft_cargoflow"
app_title = "Tawalasoft Cargoflow"
app_publisher = "Tawalasoft Solutions Limited"
app_description = "ERPNext app for managing shipments, supplier invoicing, freight charges, customs costs, and landed cost allocation."
app_email = "tawalasoftsolutions@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tawalasoft_cargoflow",
# 		"logo": "/assets/tawalasoft_cargoflow/logo.png",
# 		"title": "Tawalasoft Cargoflow",
# 		"route": "/tawalasoft_cargoflow",
# 		"has_permission": "tawalasoft_cargoflow.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tawalasoft_cargoflow/css/tawalasoft_cargoflow.css"
# app_include_js = "/assets/tawalasoft_cargoflow/js/tawalasoft_cargoflow.js"

# include js, css files in header of web template
# web_include_css = "/assets/tawalasoft_cargoflow/css/tawalasoft_cargoflow.css"
# web_include_js = "/assets/tawalasoft_cargoflow/js/tawalasoft_cargoflow.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tawalasoft_cargoflow/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

after_install = "tawalasoft_cargoflow.install.after_install"

doctype_js = {
    "Landed Cost Voucher": "public/js/landed_cost_voucher.js",
    "Purchase Invoice": "public/js/purchase_invoice.js",
}

doc_events = {
    "Landed Cost Voucher": {
        "before_save": "tawalasoft_cargoflow.services.landed_cost_voucher.before_save",
    },
    "Purchase Invoice": {
        "validate": "tawalasoft_cargoflow.services.purchase_invoice.validate",
    },
}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tawalasoft_cargoflow/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tawalasoft_cargoflow.utils.jinja_methods",
# 	"filters": "tawalasoft_cargoflow.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tawalasoft_cargoflow.install.before_install"
# after_install = "tawalasoft_cargoflow.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tawalasoft_cargoflow.uninstall.before_uninstall"
# after_uninstall = "tawalasoft_cargoflow.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tawalasoft_cargoflow.utils.before_app_install"
# after_app_install = "tawalasoft_cargoflow.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tawalasoft_cargoflow.utils.before_app_uninstall"
# after_app_uninstall = "tawalasoft_cargoflow.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tawalasoft_cargoflow.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tawalasoft_cargoflow.tasks.all"
# 	],
# 	"daily": [
# 		"tawalasoft_cargoflow.tasks.daily"
# 	],
# 	"hourly": [
# 		"tawalasoft_cargoflow.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tawalasoft_cargoflow.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tawalasoft_cargoflow.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tawalasoft_cargoflow.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tawalasoft_cargoflow.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tawalasoft_cargoflow.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tawalasoft_cargoflow.utils.before_request"]
# after_request = ["tawalasoft_cargoflow.utils.after_request"]

# Job Events
# ----------
# before_job = ["tawalasoft_cargoflow.utils.before_job"]
# after_job = ["tawalasoft_cargoflow.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tawalasoft_cargoflow.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Landed Cost Voucher-custom_shipment_no",
                    "Purchase Invoice-custom_shipment_no",
                    "Purchase Invoice-custom_purchase_invoice_type",
                    "Purchase Receipt-custom_shipment_no",
                    "Purchase Order-custom_shipment_no",
                    "Landed Cost Taxes and Charges-custom_purchase_invoice",
                ],
            ]
        ],
    },
]