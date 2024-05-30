from django.shortcuts import render
from items.models import Item, Category
from .forms import LoginForm
# Create your views here.
def index(request):
    items =  Item.objects.all
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def login(request):
    form = LoginForm()
    return render(request, 'core/login.html', {
        'form': form,
    })
