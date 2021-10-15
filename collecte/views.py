from django.shortcuts import render
from .models import Photo, Category

# Create your views here.


def index(request):
    cate = Category.objects.all()
    photo = Photo.objects.all()
    base_data = {'cate':cate,'photo':photo}
    return render(request,'collecte/index.html',base_data)

def category(request,id):
    cat = Category.objects.all()
    categorys = Category.objects.get(pk=id)
    photo = Photo.objects.filter(cat=categorys)
    base_data = {'cat':cat,'photo':photo}
    return render(request, 'collecte/category.html',base_data)