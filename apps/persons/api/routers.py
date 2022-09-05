from rest_framework.routers import DefaultRouter

from apps.persons.api.views import PersonsViewSet

router = DefaultRouter()

router.register(r'persons',PersonsViewSet,basename = 'persons')


urlpatterns = router.urls