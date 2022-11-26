from django import template

register = template.Library()

@register.filter(name='string_to_list')
def string_to_list(value) -> list:
    return str(value).replace(" ", "").split(",")
