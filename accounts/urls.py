from django.urls import path
from accounts import views

urlpatterns = [
    path('registration/',views.Registration,name='registration'),
    path('login/',views.Signin,name='login'),
    path('logout/',views.Signout,name='logout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('forgetpassword/',views.ForgetPassword,name='forgetpassword'),
    path('check_passwordreset/<uidb64>/<token>',views.CheckPasswordReset,name='check_passwordreset'),
    path('resetpassword/',views.ResetPassword,name='resetpassword'),
]