from django.urls import path
from .views import UserCreateView, CustomLoginView, CustomLogoutView,reserve_conference


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('<int:conference_id>/reserve/', reserve_conference, name='reserve_conference'),
]