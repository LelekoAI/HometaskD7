from django import template


register = template.Library()


@register.filter()
def censor(value: str) -> str:
    return value.replace('text', '****')
