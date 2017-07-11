from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.staticfiles import finders

from .. import get_setting

register = template.Library()
    
@register.simple_tag(takes_context=True)
def setting(context, name):
    return mark_safe(get_setting(name, context))

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
    out = mark_safe("")
    match = context["request"].resolver_match
    if match.app_name:
        fn = finders.find(match.app_name + ".js")
        if fn:
            out += script(settings.STATIC_URL + match.app_name + ".js")
        if match.url_name:
            fn = finders.find(match.app_name + "/" + match.url_name + ".js")
            if fn:
                out += script(settings.STATIC_URL + match.app_name + "/" +
                              match.url_name + ".js")
    return out
