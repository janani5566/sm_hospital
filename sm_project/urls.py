from django.contrib import admin
from django.urls import path,include
from sm_app.views import showexp

from sm_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sm_app.urls')),

]