from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('',views.posts_list,name='list'),
    # 在html中可以通过{% url 'list'%}访问这个链接
    path('new-post/',views.post_new,name='new-post'),
    path('<slug:slug>',views.post_page,name='page'),
    path('<int:pk>/delete',views.post_delete,name='post-delete'),
    path("<int:pk>/edit",views.post_edit,name='post-edit'),
]