from catalog.views import author_info, authors_list, book_info, books_list, index, publisher_info, publishers_list, \
    stores_info, stores_list

from django.urls import path

app_name = 'catalog'
urlpatterns = [
    path('catalog/', index, name="index"),
    path('books/', books_list, name='books'),
    path('books/<int:id>/', book_info, name='books_info'),
    path('authors/', authors_list, name="authors"),
    path('authors/<int:id>/', author_info, name='author_info'),
    path('stores/', stores_list, name="stores"),
    path('stores/<int:id>', stores_info, name="stores_info"),
    path('publishers/', publishers_list, name='publishers'),
    path('publishers/<int:pk>', publisher_info, name='publisher_info')
]
