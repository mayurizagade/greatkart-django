# this is python function it takes request as an argument and it will return the dictonary of data as a context

from .models import Category

def menu_links(request):
    links = Category.objects.all() # bcoz we need all category 
    return dict(links=links)  # it will bring all categories list stor them into vrcha links


