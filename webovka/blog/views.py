from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def post_list(request):
    random_number = random.randint(1, 100)
    return render(request, 'blog/post_list.html', {random_number})