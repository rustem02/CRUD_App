from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.draw_menu),
    path('index/', views.index),
    path('index/<slug:post_slug>', views.show_detail, name='news-detail'),
]
