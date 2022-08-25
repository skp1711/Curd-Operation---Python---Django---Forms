from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_data, name='add-data'),
    path('update/<int:pk>', views.update_data, name='update-data'),
    path('delete/<int:pk>', views.delete_data, name='delete-data'),

]
