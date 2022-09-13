from django.urls import path
from .views import home, todo_create, todo_update, todo_delete
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', home, name='home2'),
    path("add/", todo_create, name="add"),
    path("update/<int:id>", todo_update, name="update"),
    path("delete/<int:id>", todo_delete, name="delete"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
