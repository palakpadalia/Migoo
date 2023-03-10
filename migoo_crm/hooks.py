from . import __version__ as app_version

app_name = "migoo_crm"
app_title = "Migoo CRM"
app_publisher = "Palak Padalia"
app_description = "MIGOO"
app_email = "padaliapalak19@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css ="/assets/migoo_crm/css/try.css"
# app_include_css = "/assets/migoo_crm/css/migoo_crm.css"
# app_include_js = "/assets/migoo_crm/js/custom_workspaace.js"
# app_include_js = "/assets/migoo_crm/js/custom_base_widget.js"
app_include_js = "/assets/migoo_crm/js/custom_number_card_widget.js"


# include js, css files in header of web template
# web_include_css = "/assets/migoo_crm/css/migoo_crm.css"
# web_include_js = "/assets/migoo_crm/js/migoo_crm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "migoo_crm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
page_js = {"dashboard-view": "public/js/custom_dashboard_view.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "migoo_crm.utils.jinja_methods",
#	"filters": "migoo_crm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "migoo_crm.install.before_install"
# after_install = "migoo_crm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "migoo_crm.uninstall.before_uninstall"Dashboard


# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    "User": "migoo_crm.code_override.user.User",
    "Opportunity": "migoo_crm.code_override.opportunity.Opportunity",
    "Auto Email Report": "migoo_crm.code_override.auto_email_report.AutoEmailReport",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "send_daily_mail_report": {
#         "59 18 * * *": [
#             "migoo_crm.api.send_daily_mail_report"
#         ]
#     }

#	"all": [
#		"migoo_crm.tasks.all"
#	],

# "daily": [
# 	"migoo_crm.api.send_daily_mail_report"
# ]
#	"hourly": [
#		"migoo_crm.tasks.hourly"
#	],
#	"weekly": [
#		"migoo_crm.tasks.weekly"
#	],
#	"monthly": [
#		"migoo_crm.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "migoo_crm.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "frappe.core.doctype.user.user.update_password": "migoo_crm.code_override.user.update_password",
    "erpnext.crm.doctype.lead.lead.make_opportunity": "migoo_crm.code_override.lead.make_opportunity",
    "erpnext.crm.doctype.lead.lead.make_customer": "migoo_crm.code_override.lead.make_customer",
    "erpnext.crm.doctype.opportunity.opportunity.make_customer": "migoo_crm.code_override.opportunity.make_customer",
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "migoo_crm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"migoo_crm.auth.validate"
# ]

fixtures = [
    {"dt": "Report", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},

    {"dt": "Client Script", },

    {"dt": "Server Script", },

    {"dt": "Role Profile", },

    {"dt": "Module Profile", },

    {"dt": "Number Card", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},

    {"dt": "Property Setter", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},

    {"dt": "Dashboard", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},

    {"dt": "Dashboard Chart", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},

    {"dt": "Website Script", },

    {"dt": "Dashboard Chart", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},
    
    {"dt": "Notification", "filters": [
        [
            "module", "in", [
                "Migoo CRM"
            ]
        ]
    ]},


]
