from django.template import Library
from django.utils.html import format_html

register = Library()

@register.simple_tag(takes_context=True)
def copy_button(context, order_id):
    return format_html(
        '<input type="text" value="{}" id="order_id_input" readonly style="display: none;">'
        '<button onclick="copyToClipboard(\'order_id_input\')">Copy</button>',
        order_id
    )