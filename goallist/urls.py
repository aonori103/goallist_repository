from django.urls import path
from .views import GoalListView, GoalDetailView, GoalRegistView, GoalEditView

app_name = 'goallist'
urlpatterns=[
    path('goal_list/', GoalListView.as_view(), name='goal_list'),
    path('goal_detail/<int:pk>', GoalDetailView.as_view(), name='goal_detail'),
    path('goal_regist', GoalRegistView.as_view(), name='goal_regist'),
    path('goal_edit/<int:pk>', GoalEditView.as_view(), name='goal_edit'),
]