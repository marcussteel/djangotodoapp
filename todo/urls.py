from django.urls import path
from .views import home, todo_create, todo_update
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', home, name='home'),
    path("add/", todo_create, name="add"),
    path("update/<int:id>", todo_update, name="update"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
