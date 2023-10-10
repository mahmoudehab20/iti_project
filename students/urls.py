from django.urls import path
from students.views import (returnbookGenericView,showborrow,bowbooks)

urlpatterns = [
    path('<int:id>',returnbookGenericView.as_view(),name='book.return'),
    path('borrow/',showborrow,name='borrowed'),
    path('<int:id>/bo',bowbooks,name="borrow.book"),
]