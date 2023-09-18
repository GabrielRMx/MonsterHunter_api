from django.urls import path
from .views import MonsterView

urlpatterns = [
    path('monsters/', MonsterView.as_view(), name='monster_list'),
    path('monsters/<int:id>', MonsterView.as_view(), name='monster_info')
]
