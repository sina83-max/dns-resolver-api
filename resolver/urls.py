
from django.urls import path
from resolver import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('resolve', views.DnsResolveApiView, basename='dns-resolve')

urlpatterns = [
    path('api/resolve/', views.DnsResolveApiView.as_view(), name='dns-resolve-api'),
    path('api/reverse-resolve/', views.ReverseDnsResolveApiView.as_view(), name='rdns-resolve-api')
]
