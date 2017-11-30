from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'server',views.ServerViewSet)
router.register(r'serverip',views.ServerIPViewSet)
router.register(r'hrbl_app',views.HRBL_AppViewSet)
router.register(r'server_app',views.Server_AppViewSet)
