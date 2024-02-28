from django.urls import path

from .views import get_library_page, get_book_library, add_book

urlpatterns = [
    path('', get_library_page, name='libraries'),
    path('books/<int:id>/', get_book_library, name="books"),
    path('add_book/', add_book, name="add_book")
]