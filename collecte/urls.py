from django.urls import path, include

from.views import index, category


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:id>/', category, name="category")
]
