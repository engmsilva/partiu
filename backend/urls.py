from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views as user_views
from account import views as account_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'accounts', account_views.AccountViewSet)
router.register(r'transactions', account_views.TransactionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
