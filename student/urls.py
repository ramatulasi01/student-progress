from django.urls import path
from student import views

urlpatterns = [
    path('<int:pk>/',views.student_detail,name='student_detail'),
]
