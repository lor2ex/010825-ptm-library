from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views.borrows import BorrowViewSet
from library.views.event import EventViewSet
from library.views.libraries import LibraryViewSet
from library.views.posts import PostViewSet
from library.views.users import UserViewSet, RegisterUserView, LogoutUser, LoginUser
from library.views.authors import AuthorViewSet


default_router = DefaultRouter()
default_router.register('posts', PostViewSet, basename='posts')
default_router.register('events', EventViewSet, basename='events')
default_router.register('authors', AuthorViewSet, basename='authors')
default_router.register('users', UserViewSet, basename='users')
default_router.register('borrows', BorrowViewSet, basename='borrows')
default_router.register('libraries', LibraryViewSet, basename='libraries')


urlpatterns = [
    path('auth-login/', LoginUser.as_view()),
    path('auth-logout/', LogoutUser.as_view()),
    path('auth-register/', RegisterUserView.as_view()),

    path('categories/', include('library.urls.categories')),
    path('books/', include('library.urls.books')),
]

urlpatterns += default_router.urls