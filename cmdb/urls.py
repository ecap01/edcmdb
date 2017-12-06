from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'servers',views.ServerViewSet)
router.register(r'serverips',views.ServerIPViewSet)
router.register(r'hrbl_apps',views.HRBL_AppViewSet)
router.register(r'server_apps',views.Server_AppViewSet)
router.register(r'users',views.UserViewSet)