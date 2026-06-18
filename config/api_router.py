from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from ehardware.products.api.views import ProductViewSet
from ehardware.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("products", ProductViewSet)
router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
