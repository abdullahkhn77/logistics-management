from django.urls import path
import users.views as user_view

urlpatterns = [
    path('create', user_view.create_account),
    path('login', user_view.login),
    path('create_profile', user_view.create_profile),
    path('change_password', user_view.change_password),
    path('view_label', user_view.view_label)
]
