# BookList

PROJECT AVAILABLE HERE: https://booklist-torres.herokuapp.com/


MODEL:
Book
- title
- author
- publishing_year
- ISBN_number
- number_of_pages
- language
- book_cover


URLs:
- ''
- 'contact/'
- 'search-book/'
- 'add_book/'
- 'delete_book/<id>/'
- 'edit_book/<id>/'
- 'rest_api/'
- 'booklist/'
- 'media/<id>/'

  
FORMS:
- BookModelForm (ModelForm)   : adds books (manually)
- ImportBookModelForm (Form)  : imports books from google API

  
VIEWS:
- IndexView (View)              : homepage
- ContactView (View)            : show's contact form and location map
- book_search                   : shows all books (table) - search: title / author / year / language
- PicsView (View)               : shows book covers
- AddBookView (View)            : adds books (manually) through form
- EditBookView (View)           : edit book function (button)
- DeleteBookView (View)         : delete book function (button)
- BookList (ListCreateAPIView)  : offers collection in API
- ApiImportBookView (View)      : imports books from google API
- validate_isbn

  
RESOURCES:
- python
- django
- html
- css
- pytest
- PEP8
