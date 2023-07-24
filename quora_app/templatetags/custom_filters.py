# custom_filters.py
from django import template

register = template.Library()

@register.filter
def read_more(content, max_length):
    '''
        this is user to hide the full contain
        and display content on bases of length passed.
    '''
    if len(content) <= max_length:
        return content
    return f"{content[:max_length]}"
