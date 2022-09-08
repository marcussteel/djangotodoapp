from django.urls import path
from .views import home, todo_create
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', home, name='home'),
    path("add/", todo_create, name="add"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
