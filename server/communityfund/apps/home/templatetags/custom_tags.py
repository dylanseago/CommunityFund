from django.template import Library
import locale

locale.setlocale(locale.LC_ALL, '')
register = Library()


@register.filter(name='currency')
def currency_filter(value):
    return locale.currency(value, grouping=True)


@register.filter(name='range')
def range_filter(value):
    """
    Filter - returns a sequence containing range made from given value

    Example:
    {% for i in 3|range %}
        {{ i }}
    {% endfor %}

    Result:
    0
    1
    2

    Example:
    {% for i in (0,10,2)|range %}
        {{ i }}
    {% endfor %}

    Result:
    0
    2
    4
    6
    8
    """
    return range(*value) if isinstance(value, tuple) else range(value)