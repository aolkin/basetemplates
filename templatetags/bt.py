from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html, conditional_escape
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.templatetags.staticfiles import static

import re, string

from .. import get_setting

register = template.Library()
    
@register.simple_tag(takes_context=True)
def setting(context, name):
    return mark_safe(get_setting(name, context))

@register.filter(name="getattr")
def getattr_filter(value, arg):
    return getattr(value, arg, "")

PUNCTUATION_RE = re.compile(r"([ .,/)\]}!@%&+=\-;:?]+)")

@register.filter(name="break_punctuation")
def break_punctuation(value):
    replaced = PUNCTUATION_RE.sub(r"\1{wbr}", value)
    return mark_safe(conditional_escape(replaced).format(wbr="<wbr>"))

@register.filter(name="order_by")
def order_by(qs, args):
    args = [x.strip() for x in args.split(',')]
    return qs.order_by(*args)

def res_extra(integrity=""):
    return integrity and format_html(
        ' integrity="{}" crossorigin="anonymous"', integrity)

@register.simple_tag
def script(src, integrity=""):
    if "//" not in src:
        src = static(src)
    return format_html('<script src="{}"' + res_extra(integrity) +
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
    if "//" not in src:
        src = static(src)
    return format_html('<link rel="stylesheet" href="{}"' +
                       res_extra(integrity) +'>', src)

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
    if match and match.app_name:
        app_name = match.app_name.replace(":", "/")
        fn = finders.find(app_name + ".css")
        if fn:
            return style(app_name + ".css")
    return ""

@register.simple_tag(takes_context=True)
def _bt_app_script(context):
    out = mark_safe("")
    match = context["request"].resolver_match
    app_name = ""
    if match and match.app_name:
        app_name = match.app_name.replace(":", "/")
        fn = finders.find(app_name + ".js")
        if fn:
            out += script(app_name + ".js")
    if match and match.url_name:
        app_path = app_name + "/" if app_name else ""
        fn = finders.find(app_path + match.url_name + ".js")
        if fn:
            out += script(app_path + match.url_name + ".js")
    return out
