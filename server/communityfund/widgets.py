from django import forms
from django.utils.html import format_html


class BSTextInput(forms.TextInput):
    """ Bootstrap text input widget """

    def __init__(self, label, hide_label=False, prepended=None, appended=None, attrs={}):
        bs_init(self, super(BSTextInput, self), label, hide_label, prepended, appended, attrs)

    def render(self, name, value, attrs=None):
        return bs_render(self, super(BSTextInput, self), name, value, attrs)


class BSDecimalInput(forms.NumberInput):
    """ Bootstrap decimal input widget """

    def __init__(self, label, hide_label=False, prepended=None, appended=None, attrs={}):
        bs_init(self, super(BSDecimalInput, self), label, hide_label, prepended, appended, attrs)

    def render(self, name, value, attrs=None):
        return bs_render(self, super(BSDecimalInput, self), name, value, attrs)

class BSPasswordInput(forms.PasswordInput):
    """ Bootstrap password input widget """

    def __init__(self, label, hide_label=False, prepended=None, appended=None, attrs={}):
        bs_init(self, super(BSPasswordInput, self), label, hide_label, prepended, appended, attrs)

    def render(self, name, value, attrs=None):
        return bs_render(self, super(BSPasswordInput, self), name, value, attrs)


class BSEmailInput(forms.EmailInput):
    """ Bootstrap email input widget """

    def __init__(self, label, hide_label=False, prepended=None, appended=None, attrs={}):
        bs_init(self, super(BSEmailInput, self), label, hide_label, prepended, appended, attrs)

    def render(self, name, value, attrs=None):
        return bs_render(self, super(BSEmailInput, self), name, value, attrs)


def bs_init(widget, widget_super, label, hide_label, prepended, appended, attrs):
    """ Initializes the bootstrap widget """
    widget_super.__init__(bs_attrs(attrs, label))
    widget.label = label
    widget.hide_label = hide_label
    widget.has_addons = prepended or appended
    widget.prepended = prepended
    widget.appended = appended


def bs_render(widget, widget_super, name, value, attrs):
    """ Renders the bootstrap widget """
    rendered = widget_super.render(name, value, attrs)
    final_attrs = widget.build_attrs(attrs, type=widget.input_type, name=name)
    # Add any bootstrap input group addons
    if widget.has_addons:
        prepended_tag = addon(widget.prepended) if widget.prepended else ''
        appended_tag = addon(widget.appended) if widget.appended else ''
        rendered = '<div class="input-group">{}{}{}</div>'.format(prepended_tag, rendered, appended_tag)

    # The input label
    label_tag = '<label for="{}" {}>{}</label>'.format(final_attrs.get('id'),
                                                       'class="sr-only"' if widget.hide_label else '',
                                                       widget.label)
    rendered = label_tag + rendered
    return format_html(rendered)


def bs_attrs(attrs, label):
    """ Adds attributes to attrs dictionary """
    attrs = attrs.copy()
    if 'class' in attrs:
        attrs['class'] += ' form-control'
    else:
        attrs['class'] = 'form-control'
    attrs['placeholder'] = label
    return attrs


def addon(content):
    return '<div class="input-group-addon">{}</div>'.format(content)

def glyphicon(glyphicon_name):
    return '<span class="glyphicon glyphicon-{}" aria-hidden="true"></span>'.format(glyphicon_name)