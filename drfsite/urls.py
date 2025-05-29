
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from women.views import WomenApiView
# from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', WomenApiView.as_view()),
    path('api/delete/<int:id>/', WomenApiView.as_view()),

    # path("api/", WomenAPIList.as_view()),
    # path('api/women/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/delete/<int:pk>', WomenAPIDestroy.as_view()),


    # for JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
