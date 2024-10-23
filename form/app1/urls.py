from django.urls import path
from app1 import views
urlpatterns=[
    path("wish",views.fun1, name="p1"),
    path("even",views.fun2,name="p2"),
    path("fact",views.fun3,name="p3"),
    path("greater",views.fun4,name="p4"),
    path("result",views.fun5,name="p5"),
    path("arm",views.fun6,name="p6"),
    path("prime",views.fun7,name="p7")
]