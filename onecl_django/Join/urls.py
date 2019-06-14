from django.urls import path
from .views import (JoinList, JoinDetail, AuthLevelAPI)

urlpatterns = [
    path('', JoinList.as_view()),
    path('<int:pk>/', JoinDetail.as_view()),
    path('auth_level/', AuthLevelAPI.as_view()),
]