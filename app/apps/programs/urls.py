from rest_framework.routers import SimpleRouter
from .views import GymFileUploadViewset
from django.urls import path

router = SimpleRouter()
router.register(r'program-management', GymFileUploadViewset)


urlpatterns = router.urls