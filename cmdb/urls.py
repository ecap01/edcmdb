from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'server',views.ServerIPViewSet)
router.register(r'serverip',views.ServerIPViewSet)
