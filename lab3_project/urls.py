from django.urls import  path
from.import views

urlpatterns=[
    path('', views.p2),

    path('post/<int:post_id>/', views.show_post, name='post'),
    path('post/<slug:post_slug>/', views.show_slug, name='post'),

    path('send/', views.send_message, name='send')
]
