from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from courses.models import Course, Category, TagCourse

# Create your views here.

courses_base = [
    {'id': 1, 'category': 2, 'title': 'Python', 'description': 'Python course with OOP for beginners'},
    {'id': 2, 'category': 2, 'title': 'Django', 'description': 'Backend web development with Django framework'},
    {'id': 3, 'category': 3, 'title': 'SQL', 'description': 'Learn to work with databases and write complex queries'},
]

cats = [
    {'id': 1, 'name': 'frontend'},
    {'id': 2, 'name': 'backend'},
    {'id': 3, 'name': 'database'},
    {'id': 4, 'name': 'machine learning'},
]

def index(request):
    courses = Course.published.all()
    cats = Category.objects.all()
    context = {'courses': courses, 'title': 'SkillHub Courses', 'cats': cats, 'selected_cat': 0}
    return render(request, 'courses/index.html', context)

def course(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    context = {'course': course, 'title': course.title}
    return render(request, 'courses/course.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.published.filter(category__id=category.pk)

    context = {
        'title': f'SkillHub Courses: {category.name}',
        'courses': courses,
        'selected_cat': category_slug
    }
    return render(request, 'courses/index.html', context)

def show_by_tag(request, tag_slug):
    tag = get_object_or_404(TagCourse, slug=tag_slug)
    courses = tag.courses.filter(is_published=Course.Status.PUBLISHED)
    context =  {
        'title': f'SkillHub Courses with "{tag.tag}" tag',
        'courses': courses,
        'selected_cat': None,
    }
    return render(request, 'courses/index.html', context)