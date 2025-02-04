from django import template
from main.university.models import FacultySpecialty

register = template.Library()

@register.simple_tag
def filter_specialities(program, department):
    items = FacultySpecialty.objects.filter(program=program, department=department)
    return items
