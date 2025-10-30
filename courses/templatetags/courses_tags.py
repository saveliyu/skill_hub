from django import template
from .. import views

register = template.Library()

@register.simple_tag()
def count_courses_by_category(category):
    res = 0
    for course in views.courses_base:
        if course['category'] == category:
            res += 1
    return res

@register.inclusion_tag('courses/navbar.html')
def show_navbar(selected_cat=0):
    return {'cats': views.cats, 'selected_cat': selected_cat}
