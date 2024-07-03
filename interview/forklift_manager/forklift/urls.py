from django.urls import path
from forklift import views

app_name = 'forklift'
urlpatterns = [
    path('', views.overview, name='overview'),
    
    path('Permission/', views.allow_operator, name='allow_operator'),
    path('Permission2/', views.can_operate, name='can_operate'),
    path('Permission3/', views.update_hours, name='update_hours'),
    path('Add/', views.add_partner, name='add_partner'),
    path('Add2/', views.add_reparatur, name='add_reparatur'),
    path('get-partners/', views.get_partners, name='get_partners'),
    path('get-forklifts/', views.get_forklifts, name='get_forklifts'),
]