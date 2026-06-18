from django.conf import settings
from ehardware.cards.views import CardViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from ehardware.products.api.views import ProductViewSet
from ehardware.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("products", ProductViewSet)
router.register("users", UserViewSet)
router.register("cards", CardViewSet)


app_name = "api"
urlpatterns = router.urls
