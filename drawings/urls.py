from django.urls import path
from . import views

urlpatterns = [
    path('', views.drawing_gallery, name='drawing_gallery'),  # Gallery view (default home)
    path('category/<int:category_id>/', views.drawing_gallery, name='drawings_by_category'),
    path('drawing/<int:pk>/', views.drawing_detail, name='drawing_detail'),  # Detail page for each drawing
]
