from django import forms
from booklist_app.models import Book


class BookModelForm(forms.ModelForm):
    """
    form that allows to add a book manually
    """
    class Meta:
        model = Book
        labels = {
            'title': "",
            'author': "",
            'publishing_year': "",
            'ISBN_number': "",
            'number_of_pages': "",
            'language': "",
            'book_cover': 'Upload book\'s cover'
        }
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author'}),
            'ISBN_number': forms.TextInput(attrs={'placeholder': 'ISBN number'}),
            'publishing_year': forms.TextInput(attrs={'placeholder': 'Publishing year (YYYY)'}),
            'number_of_pages': forms.TextInput(attrs={'placeholder': 'Number of pages'}),
            'language': forms.TextInput(attrs={'placeholder': 'Language'}),
            # 'book_cover': forms.ClearableFileInput()
        }


class ImportBookModelForm(forms.Form):
    """
    form that allows to search for books in 'www.googleapis.com/books/v1/volumes'
    """
    title = forms.CharField(
        max_length=128,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Title   *hint: join keywords with "+" sign'}),
        required=False
    )
    author = forms.CharField(
        max_length=64,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Author   *hint: if both name and surname, join with "+" sign'}),
        required=False
    )
    isbn = forms.CharField(
        min_length=10,
        max_length=13,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'ISBN   *hint: must have either 10 or 13 digits (no hyphens)'}),
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        isbn = cleaned_data.get('isbn')

        if not (title or author or isbn):
            raise forms.ValidationError('At least one field is needed for the search')
