"""The automatic Django administrative interface."""
from django.contrib import admin
"""This settings import is a package level object created in django/conf/__init__.py . 
The settings object has attributes added to it from two primary sources. """
from django.conf import settings
"""These are your CSS stylesheets, JavaScript files, fonts, and images. Since there's no processing involved, 
these files are very energy efficient since they can just be served up as is."""
from django.conf.urls.static import static
""" include() adds urls from your app directory's urls.py to the main urls.py (in memory)."""
from django.urls import path, include
from leads.views import landing_page, SignupView
"""from Django authentication system create default view"""
from django.contrib.auth.views import LoginView, LogoutView

# cretae home page url

urlpatterns = [
    path('admin/', admin.site.urls), #this urls handling with request
    # for landing
    path('', landing_page, name='landing-page'), #for landing page
    path('leads/', include('leads.urls', namespace='leads')), #leads page
    path('signup/', SignupView.as_view(), name='signup'), #signup page
    path('login/', LoginView.as_view(), name='login'), #login page
    path('logout/', LogoutView.as_view(), name='logout'), #logout page
]

"""for static file, css style"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

