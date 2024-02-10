from django import template

register = template.Library()

@register.filter
def increment(value):
    return value + 1
