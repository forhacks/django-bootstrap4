# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from importlib import import_module

from django.conf import settings

# Default settings

BOOTSTRAP4_DEFAULTS = {
    'base_url': None,  # '//maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/'
    'font_url': {
        'href': 'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons'
    },
    'css_url': {
        'href': 'https://unpkg.com/bootstrap-material-design@4.0.0-beta.3/dist/css/bootstrap-material-design.min.css',
        'integrity': 'sha384-k5bjxeyx3S5yJJNRD1eKUMdgxuvfisWKku5dwHQq9Q/Lz6H8CyL89KF52ICpX4cL',
        'crossorigin': 'anonymous',
    },
    'theme_url': None,
    'jquery_url': {
        'url': 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
        'integrity': 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN',
        'crossorigin': 'anonymous',
    },
    'popper_url': {
        'url': 'https://unpkg.com/popper.js@1.12.5/dist/umd/popper.js',
        'integrity': 'sha384-KlVcf2tswD0JOTQnzU4uwqXcbAy57PvV48YUiLjqpk/MJ2wExQhg9tuozn5A1iVw',
        'crossorigin': 'anonymous',

    },
    'javascript_url': {
        'url': 'https://unpkg.com/bootstrap-material-design@4.0.0-beta.3/dist/js/bootstrap-material-design.js',
        'integrity': 'sha384-hC7RwS0Uz+TOt6rNG8GX0xYCJ2EydZt1HeElNwQqW+3udRol4XwyBfISrNDgQcGA',
        'crossorigin': 'anonymous',
    },
    'javascript_in_head': False,
    'include_jquery': False,
    'horizontal_label_class': 'col-md-3',
    'horizontal_field_class': 'col-md-9',

    'set_placeholder': True,
    'required_css_class': '',
    'error_css_class': 'has-error',
    'success_css_class': 'has-success',
    'formset_renderers': {
        'default': 'bootstrap4.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap4.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap4.renderers.FieldRenderer',
        'inline': 'bootstrap4.renderers.InlineFieldRenderer',
    },
}


def get_bootstrap_setting(name, default=None):
    """
    Read a setting
    """
    # Start with a copy of default settings
    BOOTSTRAP4 = BOOTSTRAP4_DEFAULTS.copy()

    # Override with user settings from settings.py
    BOOTSTRAP4.update(getattr(settings, 'BOOTSTRAP4', {}))

    return BOOTSTRAP4.get(name, default)


def bootstrap_url(postfix):
    """
    Prefix a relative url with the bootstrap base url
    """
    return get_bootstrap_setting('base_url') + postfix


def jquery_url():
    """
    Return the full url to jQuery file to use
    """
    return get_bootstrap_setting('jquery_url')


def popper_url():
    """
    Return the full url to Popper file
    """
    return get_bootstrap_setting('popper_url')


def javascript_url():
    """
    Return the full url to the Bootstrap JavaScript file
    """
    url = get_bootstrap_setting('javascript_url')
    return url if url else bootstrap_url('js/bootstrap.min.js')


def css_url():
    """
    Return the full url to the Bootstrap CSS file
    """
    url = get_bootstrap_setting('css_url')
    return url if url else bootstrap_url('css/bootstrap.min.css')


def theme_url():
    """
    Return the full url to the theme CSS file
    """
    return get_bootstrap_setting('theme_url')


def get_renderer(renderers, **kwargs):
    layout = kwargs.get('layout', '')
    path = renderers.get(layout, renderers['default'])
    mod, cls = path.rsplit(".", 1)
    return getattr(import_module(mod), cls)


def get_formset_renderer(**kwargs):
    renderers = get_bootstrap_setting('formset_renderers')
    return get_renderer(renderers, **kwargs)


def get_form_renderer(**kwargs):
    renderers = get_bootstrap_setting('form_renderers')
    return get_renderer(renderers, **kwargs)


def get_field_renderer(**kwargs):
    renderers = get_bootstrap_setting('field_renderers')
    return get_renderer(renderers, **kwargs)
