"""Returns an element for inclusion in urlpatterns."""
from django.urls import path

from .views import (home_page, lead_detail, lead_create, lead_update, lead_delete, lead_list, 
                    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
)
app_name = "leads"
# pk -> primary key from id user from sql
urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
   
    
]