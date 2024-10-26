from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ConferenceListView.as_view(), name='conference_list'),
    path('details/<int:pk>', ConferenceDetailView.as_view(), name='conference_details'),
    path('update/<int:pk>', ConferenceUpdateView.as_view(), name='conference_update'),
    path('delete/<int:pk>', ConferenceDeleteView.as_view(), name='conference_delete'),
    path('create/', ConferenceCreateView.as_view(), name='conference_create'),
    
]