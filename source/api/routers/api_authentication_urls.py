from django.urls import path
from api.views.api_authentication_views import MyTokenObtainPairView, MyTokenRefreshView
from api.views.api_protect_views import ProtectedView

urlpatterns = [
    path('v1/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('v1/protected/', ProtectedView.as_view(), name='protected_view'),
]