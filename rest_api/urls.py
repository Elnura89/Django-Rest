from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from app import views
from django.conf import settings
from app.views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'students', views.StudentsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('index-rest', indexRest, name='index'),
]

urlpatterns += router.urls
