"""aaa"""

from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """bbb"""
    return HttpResponse("Hello, I love Django!")

def hzx_howsgoing(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )