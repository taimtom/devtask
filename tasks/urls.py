from django.urls import path
from .views import TaskList, TaskDetail, UncompletedTaskList, CompletedTaskList
urlpatterns = [
    path('tasks/',TaskList.as_view(), name="task-list-create" ),
    path('completed-tasks/',CompletedTaskList.as_view(), name="task-list-create" ),
    path('uncompleted-tasks/',UncompletedTaskList.as_view(), name="task-list-create" ),
    path('tasks/<int:pk>/',TaskDetail.as_view(),  name="task-detail-update" ),
]