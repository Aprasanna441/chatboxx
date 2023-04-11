
from django.urls import path
from . import views
from .views import GroupChatView,IndividualChatView

urlpatterns = [
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path('signout',views.signout,name='signout'),


    path('',views.welcome,name="welcome"),
    path('<str:group_name>/',views.index),
    path('groupchat/<str:groupname>',GroupChatView.as_view(),name="groupchat"),

    path('individualchat',IndividualChatView.as_view(),name="individualchat")


]
