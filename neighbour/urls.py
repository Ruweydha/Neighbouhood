from unicodedata import name
from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/occupants', views.register_occupant, name = 'registerOccupants'),
    path('view/neighborhood/<int:id>', views.view_neighborhood, name = 'neighbourhood'),
    path('post/', views.create_post, name = 'post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)