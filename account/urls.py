from django.urls import path
from .views import (
    RegistrationView,
    LoginView,
    LogoutView,
    VerificationView,
    index,
)
from django.views.decorators.csrf import csrf_exempt

app_name = 'account'

urlpatterns = [
    path('', index, name="home"),
    path('registration/', RegistrationView.as_view(),
         name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('activate/<uidb64>/<token>/',
         VerificationView.as_view(), name='activate'),
    # path('validate-email', csrf_exempt(views.EmailValidationView.as_view()),
    #      name='validate_email'),
    # path('search', csrf_exempt(views.SearchView.as_view()), name='search')
]
