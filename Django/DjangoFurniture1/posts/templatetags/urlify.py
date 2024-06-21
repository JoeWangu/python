from atexit import register
# custom filter to parse urls which is better than share_string which is built in

from urllib.parse import quote_plus
from django import template

register = template.Library()

@register.filter
def urlify(value):
    return quote_plus(value)