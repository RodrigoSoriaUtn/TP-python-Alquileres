from django import template

register = template.Library()

@register.filter
def modulo(num, divisor) :
    return num % divisor