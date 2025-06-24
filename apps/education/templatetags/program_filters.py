from django import template
from register.models.university import Specialty

register = template.Library()

@register.simple_tag
def filter_specialities(program, department):
    items = Specialty.objects.filter(program=program, department=department)
    return items
