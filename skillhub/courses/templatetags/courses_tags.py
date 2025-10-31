from django import template
from .. import views
from ..models import Category, Course

register = template.Library()

@register.simple_tag()
def count_courses_by_category(category):
    return len(Course.objects.filter(category=category))

@register.inclusion_tag('courses/navbar.html')
def show_navbar(selected_cat=0):
    cats = Category.objects.all()
    return {'cats': cats, 'selected_cat': selected_cat}
