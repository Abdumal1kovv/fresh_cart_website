from django import template

register = template.Library()


@register.filter(name='x_range')
def custom_range(n: int):
    return list(range(n))


@register.filter(name='check_rate')
def check_rating(n, k):
    return n >= k
