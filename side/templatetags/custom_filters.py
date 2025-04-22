from django import template
import re

register = template.Library()

@register.filter()
def highlight(text, query):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(lambda m: f'<mark>{m.group(0)}</mark>', text)
