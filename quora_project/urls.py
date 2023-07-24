"""
URL configuration for quora_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from auth_app.urls import auth_patterns
from quora_app.urls import questions_patterns, answers_patterns, index_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    # Index Page
    path('', include((index_patterns, 'quora_app'), namespace="index")),

    # Auth Patters
    path('auth/', include((auth_patterns, 'auth_app'))),

    # Questions Patterns
    path('questions/', include((questions_patterns, 'quora_app'), namespace="questions")),

    # Answer Patterns
    path('answers/', include((answers_patterns, 'quora_app'), namespace="answers")),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
