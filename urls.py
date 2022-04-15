from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from .views import IndexView, AddBookView, EditBookView, DeleteBookView, ContactView, \
    book_search, PicsView, BookList, ApiImportBookView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search-book/', book_search, name='book_search'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('delete_book/<int:book_id>/', DeleteBookView.as_view(), name='delete_book'),
    path('edit_book/<int:book_id>/', EditBookView.as_view(), name='edit_book'),
    path('rest_api/', BookList.as_view(), name='export_book'),
    path('booklist/', ApiImportBookView.as_view(), name='books_detail'),
    path('media/<int:book_id>/', PicsView.as_view(), name='media'),

] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)
