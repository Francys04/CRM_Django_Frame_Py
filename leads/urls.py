from django.urls import path

from .views import home_page, lead_detail, lead_create, lead_update, lead_delete

app_name = "leads"
# pk -> primary key from id user from sql
urlpatterns = [
    path('', home_page, name='lead-list'), 
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/update/', lead_update, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('create/', lead_create, name='lead-create'),
   
    
]