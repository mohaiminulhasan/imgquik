from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('<int:width>x<int:height>/<str:bg>/<str:fg>/', views.generate_image, name='generate_image_two'),
    path('<int:width>x<int:height>/<str:bg>/', views.generate_image, name='generate_image_one'),
    path('<int:width>x<int:height>/', views.generate_image, name='generate_image'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)