from django import template

register = template.Library()

@register.simple_tag
def my_function_tag():
    return "Hello from my custom template tag!"
from django import template

register = template.Library()

@register.simple_tag
def my_function_tag():
    return "Hello from my custom template tag!"
