
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from women.views import WomenApiView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', WomenApiView.as_view()),
    path('api/<int:id>/', WomenApiView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenObtainPairView.as_view(), name='token_verify'),
]
