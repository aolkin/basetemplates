from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.staticfiles import finders

register = template.Library()

DEFAULT_SETTINGS = {
    "BT_VIEWPORT_SCALE": True,
    "BT_BOOTSTRAP_VERSION": "3.3.7",
    "BT_JQUERY_VERSION": "3.2.1",
    "BT_JQUERY_JS_INTEGRITY": "sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=",
    "BT_JS_FILES": [],
    "BT_CSS_FILES": []
}

def get_setting(name):
    if hasattr(settings, name):
        return getattr(settings, name)
    else:
        return DEFAULT_SETTINGS.get(name,"")
    
@register.simple_tag(takes_context=True)
def _bt_prep_resources(context):
    context["BT_viewport_scale"] = get_setting("BT_VIEWPORT_SCALE")
    context["BT_scripts"] = get_setting("BT_JS_FILES")
    context["BT_styles"] = get_setting("BT_CSS_FILES")
    context["BT_site_title"] = get_setting("BT_SITE_TITLE")
    return ""
    
@register.simple_tag
def setting(name):
    return mark_safe(get_setting(name))

def res_extra(src, integrity=""):
    crossorigin = (' crossorigin="anonymous"' if src.startswith("https://")
                   else '')
    if integrity:
        integrity = format_html(' integrity="{}"', integrity)
    return integrity + crossorigin

@register.simple_tag
def script(src, integrity=""):
    return format_html('<script src="{}"' + res_extra(src, integrity) +
                       '></script>', src)

@register.simple_tag
def _bt_script(src, name):
    if get_setting("BT_{}_VERSION".format(name.upper())):
        src = src.format(get_setting("BT_{}_VERSION".format(name.upper())))
        return script(src, get_setting(
            "BT_{}_JS_INTEGRITY".format(name.upper())))
    else:
        return ""

@register.simple_tag
def style(src, integrity=""):
    return format_html('<link rel="stylesheet" href="{}"' +
                       res_extra(src, integrity) +'>', src)

@register.simple_tag
def _bt_style(src, name):
    if get_setting("BT_{}_VERSION".format(name.upper())):
        src = src.format(get_setting("BT_{}_VERSION".format(name.upper())))
        return style(src, get_setting(
            "BT_{}_CSS_INTEGRITY".format(name.upper())))
    else:
        return ""

@register.simple_tag(takes_context=True)
def _bt_app_style(context):
    match = context["request"].resolver_match
    if match.app_name:
        fn = finders.find(match.app_name + ".css")
        if fn:
            return style(fn)
    return ""

@register.simple_tag(takes_context=True)
def _bt_app_script(context):
    out = ""
    match = context["request"].resolver_match
    if match.app_name:
        fn = finders.find(match.app_name + ".js")
        print(fn)
        if fn:
            out += script(fn)
        if match.url_name:
            fn = finders.find(match.app_name + "/" + match.url_name + ".js")
            if fn:
                out += script(fn)
    return out
