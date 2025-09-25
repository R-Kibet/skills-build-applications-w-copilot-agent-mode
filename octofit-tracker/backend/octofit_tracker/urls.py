# Restore api_activities function
def api_activities(request):
    base_url = f"https://{codespace_name}-8000.app.github.dev" if codespace_name else "http://localhost:8000"
    return JsonResponse({
        "endpoint": f"{base_url}/api/activities/",
        "message": "OctoFit activities endpoint"
    })
"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


# Get codespace name from environment variable
codespace_name = os.environ.get('CODESPACE_NAME', None)


def root(request):
    return JsonResponse({
        "message": "Welcome to OctoFit Tracker API!",
        "endpoints": ["/api/activities/"]
    })

def favicon(request):
    # Return a 204 No Content for favicon.ico requests
    from django.http import HttpResponse
    return HttpResponse(status=204)

urlpatterns = [
    path('', root),
    path('favicon.ico', favicon),
    path('admin/', admin.site.urls),
    path('api/activities/', api_activities),
]
