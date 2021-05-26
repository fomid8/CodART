from django.shortcuts import render
from django.conf import settings


def import_refactorings():
    import sys
    import os
    sys.path.append(os.path.dirname(settings.BASE_DIR))
    module = __import__('refactorings')  # import code
    sys.path.pop()
    return module


refactorings = import_refactorings()
refactoring_map = refactorings.refactoring_map


def index(request):
    context = {
        'index': True
    }

    print(refactoring_map)

    return render(request, 'index/index.html', context)


def about_us(request):
    context = {
        'about_us': True
    }
    return render(request, 'index/about_us.html', context)
