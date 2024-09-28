from django.urls import path
from . import views

app_name='users'
urlpatterns = [

    path('register/',views.register_view,name="register"),
    # 在html中可以通过{% url '<name>'%}访问这个链接
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('profile/',views.profile_view,name="profile")
    
]