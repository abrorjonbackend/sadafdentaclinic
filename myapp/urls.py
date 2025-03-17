from django.urls import path
from .views import SardorPostView, ZoirPostView, JasurPostView, GeneralPostListView, GeneralPostUpdateDeleteView

urlpatterns = [
    path('sardor/', SardorPostView.as_view(), name='sardor_posts'),
    path('zoir/', ZoirPostView.as_view(), name='zoir_posts'),
    path('jasur/', JasurPostView.as_view(), name='jasur_posts'),
    path('general/', GeneralPostListView.as_view(), name='general_posts'),
    path('general/<int:pk>/', GeneralPostUpdateDeleteView.as_view(), name='general_post_update_delete'),
]
