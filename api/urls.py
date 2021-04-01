# api/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'magnitudes', views.MagnitudeViewSet)
router.register(r'measure_units', views.MeasureUnitViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'value_logs', views.ValueLogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/logs/', views.event_value_log, name="create"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]