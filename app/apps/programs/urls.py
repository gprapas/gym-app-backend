from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path

router = SimpleRouter()
router.register(r'program-management', GymFileUploadViewset)
router.register(r'program', ProgramViewset)


urlpatterns = router.urls