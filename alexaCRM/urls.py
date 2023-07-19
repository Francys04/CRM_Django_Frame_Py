from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from leads.views import landing_page, SignupView
from django.contrib.auth.views import LoginView, LogoutView

# cretae home page url

urlpatterns = [
    path('admin/', admin.site.urls), #this urls handling with request
    # for landing
    path('', landing_page, name='landing-page'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

