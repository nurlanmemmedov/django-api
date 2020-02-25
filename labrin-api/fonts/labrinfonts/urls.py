from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from labrinfonts.views import FontFamilyViewset
from labrinfonts.views import CategoryViewset
from labrinfonts.views import FontViewset
from labrinfonts.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'fontfamilies', FontFamilyViewset)
router.register(r'categories', CategoryViewset)
router.register(r'fonts', FontViewset)
router.register(r'users', UserViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]