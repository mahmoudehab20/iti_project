from django.contrib.auth.decorators import login_required
from django.urls import path
from Admin.views import (booksListGenericView,booksDetailGenericView,DeletebookGenericView,addbookGenericView
                         ,UpdatebookGenericView,registration,usersListGenericView,bowbooks,showborrow,search,returnbookGenericView)

urlpatterns = [
    path('',booksListGenericView.as_view(),name='books'),
    path('show/<int:pk>',booksDetailGenericView.as_view(),name='book.show'),
    path('<int:pk>',login_required(DeletebookGenericView.as_view()),name='book.delete'),
    path('add/',login_required(addbookGenericView.as_view()),name='book.add'),
    path('<int:pk>/edit',login_required(UpdatebookGenericView.as_view()),name='book.edit'),
    path('signup/',registration.as_view(),name='signup'),
    path('users/',login_required(usersListGenericView.as_view()),name='user'),
    path('<int:id>/bo',bowbooks,name="borrow.book"),
    path('borrow/',showborrow,name='borrowed'),
    path('search/',search,name='search'),
    path('<int:id>',returnbookGenericView.as_view(),name='book.return')
]