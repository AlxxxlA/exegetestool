from django import template

register = template.Library()

@register.filter(name="supp")
def supp(value):
    return value.replace('^', '<sup>')
