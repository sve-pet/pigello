from django.urls import path, include

from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'planets', views.PlanetViewSet)
router.register(r'moons', views.MoonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reset/', views.reset_space),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]