# -*- coding: utf-8 -*-

from django import template
from opps.core.utils import get_app_model

register = template.Library()


@register.simple_tag
def get_config(appname, key, **kwargs):
    """
    {% load config %}
    {% get_config 'polls' 'key_slug' %}
    {% get_config 'infographics' 'key_slug' %}
    {% get_config 'promos' 'key_slug' %}

    Also works
    {% get_config 'opps.polls' 'key_slug' %}
    """

    model = get_app_model(appname, "Config")
    return model and model.get_value(key, **kwargs)


@register.simple_tag
def get_configs(appname, key_group, **kwargs):
    """
    {% load config %}
    {% get_configs 'polls' 'key_group_slug' %}
    {% get_configs 'infographics' 'key_group_slug' %}
    {% get_configs 'promos' 'key_group_slug' %}

    Also works
    {% get_configs 'opps.polls' 'key_group_slug' %}
    """

    model = get_app_model(appname, "Config")
    return model and model.get_values(key_group, **kwargs)
