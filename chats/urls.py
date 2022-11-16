
from django.urls import path

# from flipbook.views import BookApiView, BookDetailApiView
from .views import UserList, UserDetail, ChatList, ChatDetail
urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<str:phone_no>/', UserDetail.as_view()),

    path('chats/', ChatList.as_view()),
    path('chats/<str:phone_no>/', ChatDetail.as_view()),



    # path('users/<str:id>/', views.detail, name='detail'),
    # path('users', views.users, name='view-users'),
    # path('', views.view_messages, name='view-messages'),

    # path('books/', BookApiView.as_view()),
    # path('books/<int:book_id>/', BookDetailApiView.as_view()),
]