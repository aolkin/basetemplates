from django.conf import settings

DEFAULT_SETTINGS = {
    "BT_VIEWPORT_SCALE": True,
    "BT_BOOTSTRAP_VERSION": "3.3.7",
    "BT_JQUERY_VERSION": "3.2.1",
    "BT_JQUERY_JS_INTEGRITY": "sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=",
    "BT_TYPEAHEAD_VERSION": "4.0.2",
    "BT_SELECT2_VERSION": "4.0.3",
    "BT_SCROLLTO_VERSION": "2.1.0",
    "BT_FONTAWESOME_VERSION": "4.7.0",
    "BT_FONTAWESOME_CSS_INTEGRITY": "sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN",
    "BT_JS_FILES": [],
    "BT_CSS_FILES": [],
    "BT_CONTAINER_FLUID": False,
    "BT_INCLUDE_MESSAGES": True,
    "BT_MESSAGES_COLUMN_SPEC": "col-md-6",
    "BT_FAVICON_URL": "/favicon.ico"
}

def get_setting(name, context={}):
    if context.get(name, None):
        return context[name]
    if hasattr(settings, name):
        return getattr(settings, name)
    elif hasattr(settings, name[3:]):
        return getattr(settings, name[3:])
    else:
        return DEFAULT_SETTINGS.get(name,"")

def context_processor(request):
    context = {}
    context["BT_viewport_scale"] = get_setting("BT_VIEWPORT_SCALE")
    context["BT_scripts"] = get_setting("BT_JS_FILES")
    context["BT_styles"] = get_setting("BT_CSS_FILES")
    context["BT_site_title"] = (" | " + get_setting("BT_SITE_TITLE") if
                                get_setting("BT_SITE_TITLE") else "")
    context["BT_BS_container_fluid"] = get_setting("BT_CONTAINER_FLUID")
    context["BT_header_url"] = get_setting("BT_HEADER_URL")
    context["BT_header_image"] = get_setting("BT_HEADER_IMAGE")
    context["BT_footer_site"] = get_setting("BT_FOOTER_SITE")
    context["BT_user_logout"] = get_setting("LOGOUT_URL")
    context["BT_include_messages"] = get_setting("BT_INCLUDE_MESSAGES")
    context["SETTINGS"] = settings
    return context
