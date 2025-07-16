from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

from user_app.views import registration_view, logout_view, user_profile_view, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   path("login/", CustomTokenObtainPairView.as_view()),
    path("register/", registration_view),
    path("profile/", user_profile_view, name="user_profile"),

    #path("logout/", logout_view)

    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view())
]