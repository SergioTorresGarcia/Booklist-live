import json
from rest_framework import generics
from urllib.request import urlopen

from django.views import View
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from booklist_app.models import Book
from booklist_app.forms import BookModelForm, ImportBookModelForm
from booklist_app.serializers import BookSerializer

# Create your views here.
class IndexView(View):
    """
    Homepage
    """
    def get(self, request):
        return render(request, 'base.html')


class ContactView(View):
    """
    Displays contact form and location
    """
    def get(self, request):
        return render(request, 'contact.html')


def book_search(request):
    """
    Default mode shows complete book collection (ordered by title) as an easy-to-read table.
    Thumbnail pictures open on click with big resolution.

    Searching fields (title, author, isbn and year (from and to)) allow to filter the collection.
    Each filter shows results organized by its own property.

    Pagination limits 4 results per page.
    """
    queryset = Book.objects.all().order_by('title')
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    page_queryset = paginator.get_page(page_number)

    title = request.POST.get('title')
    if title:
        page_queryset = queryset.filter(title__icontains=title).order_by('title')

    author = request.POST.get('author')
    if author:
        page_queryset = queryset.filter(author__icontains=author).order_by('author')

    language = request.POST.get('language')
    if language:
        page_queryset = queryset.filter(language__istartswith=language)

    year_from = request.POST.get('year_from')
    if year_from:
        page_queryset = queryset.filter(publishing_year__gte=year_from).order_by('publishing_year')

    year_to = request.POST.get('year_to')
    if year_to:
        page_queryset = queryset.filter(publishing_year__lte=year_to).order_by('-publishing_year')

    return render(request, 'book_search.html', {'books': page_queryset, 'search_data': request.POST})


class PicsView(View):
    """
    Displays book-covers in big resolution
    (after clicking on the table thumbnails)
    """
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        return render(request, 'pics.html', {'book':book})


class AddBookView(View):
    """
    Opens form to manually add a book to the collection.
    """
    def get(self, request):
        form = BookModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_search')
        return render(request, 'form.html', {'form': form})


class EditBookView(View):
    """
    On click, filled form opens
    allowing to edit data of a particular book in the collection
    """
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        form = BookModelForm(instance=book)
        return render(request, 'form.html', {'form': form})

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_search')
        return render(request, 'form.html', {'form': form})


class DeleteBookView(View):
    """
    On click, button deletes book from the collection
    """
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        book.delete()
        return redirect('book_search')


class BookList(generics.ListCreateAPIView):
    """
    Makes local collection available - REST API
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ApiImportBookView(View):
    """
    Allows to import items from an external source.
    If the item exists, it is automatically added to the collection.
    """
    def get(self, request):
        title = "Search for books on the 'google api' database through these filters"
        form = ImportBookModelForm()
        return render(request, 'form.html', {'form':form, 'title':title})

    def post(self, request):
        form = ImportBookModelForm(request.POST, request.FILES)
        url = f'https://www.googleapis.com/books/v1/volumes?q='
        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            isbn = form.cleaned_data.get('isbn')
            if title:
                url += f'intitle:{title}'
            elif author:
                url += f'inauthor:{author}'
            elif isbn:
                url += f'isbn:{isbn}'
            resp = urlopen(url)
            book_data = json.load(resp)
            print('data', book_data)
            collection = book_data['items']
            for books in collection:
                book = books.get('volumeInfo')
                title = book.get('title')
                authors = book.get('authors')
                author = authors[0]
                publishedDate = book.get('publishedDate')[:4]
                isbns = book.get('industryIdentifiers')
                isbn = isbns[0]['identifier']
                pages = book.get('pageCount')
                book_cover = book.get('imageLinks') #[0]['medium']
                if book_cover:
                    book_cover = book_cover.get('medium')

                language = book.get('language')
                Book.objects.create(title=title, language=language, number_of_pages=pages, author=author, publishing_year=publishedDate, ISBN_number=isbn, book_cover=book_cover)
                return render(request, 'uploaded.html')
        else:
            return render(request, 'form.html', {'form': form})


def validate_isbn(value):
    """
    General validation.
    The number entered must be integer.
    Its length needs to be either 10 or 13 digits.
    """
    value = value.strip()
    not_int = False
    try:
        int(value)
    except ValueError:
        not_int = True
    if not_int or len(value) != 10 or len(value) != 13:
        raise ValidationError(
            ('%(value)s cannot be a proper ISBN number'),
            params={'value': value},
        )
