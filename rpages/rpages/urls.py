from django.urls import path

from .views import EventListView, EventListViewD1, EventListViewD2

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('D1/', EventListViewD1.as_view(), name='D1'),
    path('D2/', EventListViewD2.as_view(), name='D2'),
]
