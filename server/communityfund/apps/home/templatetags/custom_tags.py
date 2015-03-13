from django.template import Library
import locale
from django.core.urlresolvers import reverse
from django.utils.timesince import timeuntil

locale.setlocale(locale.LC_ALL, '')
register = Library()


def get_next_param(context):
    request = context['request']
    if 'next' in request.GET:
        next_param = request.GET['next']
    else:
        next_param = request.path
    if next == reverse('login') or next == reverse('signup'):
        next_param = ''
    else:
        next_param = '?next=' + next_param
    return next_param


@register.inclusion_tag("fragments/link.html", name="login_link", takes_context=True)
def login_link_tag(context, *args):
    title = args[0] if len(args) != 0 else 'Login'
    return {
        'url': reverse('login') + get_next_param(context),
        'title': title
    }


@register.inclusion_tag("fragments/link.html", name="signup_link", takes_context=True)
def login_link_tag(context, *args):
    title = args[0] if len(args) != 0 else 'Sign Up'
    return {
        'url': reverse('signup') + get_next_param(context),
        'title': title
    }


@register.filter("timeleft", is_safe=False)
def timeleft_filter(value, arg=None):
    """ Formats a date as the time until that date (i.e. "4 days, 6 hours left")."""
    if not value:
        return ''
    try:
        return timeuntil(value, arg) + ' left'
    except (ValueError, TypeError):
        return ''


@register.filter(name='currency', is_safe=False)
def currency_filter(value):
    """
    Filter - returns the currency format of the input number
    """
    if value is None:
        return ''
    try:
        return locale.currency(value, grouping=True)
    except ValueError:
        try:
            return "${:,.2f}".format(value)
        except ValueError:
            return ''


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