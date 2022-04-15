import pytest
from django.urls import reverse
from rest_framework.exceptions import ValidationError
from booklist_app.forms import BookModelForm, ImportBookModelForm
from booklist_app.models import Book

# Create your tests here.

@pytest.mark.django_db
def test_url_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_contact(client):
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_search(client, books):
    url = reverse('book_search')
    data = {
        'books': books
    }
    response = client.get(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_pics_view(client, book):
    url = reverse('media', args=(book.id,))
    data = {
        'book': book
    }
    response = client.get(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_book_get(client, book):
    url = reverse('add_book')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], BookModelForm)


@pytest.mark.django_db
def test_add_book_post(client, book):
    url = reverse('add_book')
    data = {
        'book': 'book'
    }
    response = client.post(url, data)
    assert Book.objects.count() == 1
    assert response.status_code == 200
    assert isinstance(response.context['form'], BookModelForm)
    redirected_url = reverse('book_search')
    response = client.post(redirected_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_book_get(client, book):
    url = reverse('edit_book', args=(book.id,))
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], BookModelForm)


@pytest.mark.django_db
def test_edit_book_post(client, book):
    url = reverse('edit_book', args=(book.id,))
    data = {
        'book': 'book'
    }
    response = client.post(url, data)
    assert Book.objects.count() == 1
    assert response.status_code == 200
    assert isinstance(response.context['form'], BookModelForm)
    redirected_url = reverse('book_search')
    response = client.post(redirected_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_book_get(client, book):
    assert Book.objects.count() == 1
    url = reverse('delete_book', args=(book.id,))
    response = client.get(url)
    assert Book.objects.count() == 0
    assert response.status_code == 302
    redirected_url = reverse('book_search')
    response = client.post(redirected_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_rest_api_booklist(client, books):
    url = reverse('export_book')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_rest_api_bookdetail(client, books):
    url = reverse('export_book')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_import_book_get(client, books):
    url = reverse('books_detail')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], ImportBookModelForm)


@pytest.mark.django_db
def test_api_import_book_post(client, book):
    url = reverse('books_detail')
    data = {
        'title': 'title',
        'author': 'author',
        'isbn': 'isbn'
    }
    response = client.get(url, data)
    assert Book.objects.count() == 1
    assert response.status_code == 200
    assert isinstance(response.context['form'], ImportBookModelForm)
    if not ('title' or 'author' or 'isbn'):
        raise ValidationError
    assert ValidationError('At least one field is needed for the search')
    redirected_url = reverse('book_search')
    response = client.post(redirected_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_pics_view(client, book):
    url = reverse('media', args=(book.id,) )
    response = client.get(url)
    assert response.status_code == 200
