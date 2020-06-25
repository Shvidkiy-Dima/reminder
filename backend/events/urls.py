from rest_framework.routers import SimpleRouter
from .views import EventView


router = SimpleRouter()

router.register('event', EventView)

urlpatterns = router.urls
