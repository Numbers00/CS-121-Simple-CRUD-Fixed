from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class AlphabeticalAuthorsList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()[0:99]
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        authors = Author.objects.all()
        authors.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            country_of_origin=request.data['country_of_origin'],
            image=request.data['image'],
            slug=request.data['slug']
        )
        return Response({"Authors": []})

    def delete(self, request, format=None):
        authors = Author.objects.all()
        authors.filter(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            country_of_origin=request.data['country_of_origin']
        ).delete()
        return Response({"Authors": []})

    def put(self, request, format=None):
        authors = Author.objects.all()
        target_author = authors.get(
            first_name=request.data['target_first_name'],
            last_name=request.data['target_last_name'],
            country_of_origin=request.data['target_country_of_origin']
        )
        target_author.first_name = request.data['first_name']
        target_author.last_name = request.data['last_name']
        target_author.country_of_origin = request.data['country_of_origin']
        target_author.image = request.data['image']
        target_author.slug = request.data['slug']
        target_author.save()
        return Response({"Books": []})

class AlphabeticalBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        targetAuthor = Author.objects.filter(Q(first_name=request.data['author_first_name']))
        books = Book.objects.all()
        books.create(
            author=targetAuthor[0], 
            book_title=request.data['book_title'], 
            category=request.data['category'], 
            price=request.data['price'],
            number_of_pages=request.data['number_of_pages'],
            language=request.data['language'],
            slug=request.data['slug']
        )
        return Response({"Books": []})

    def delete(self, request, format=None):
        books = Book.objects.all()
        books.filter(
            book_title=request.data['book_title']
        ).delete()
        return Response({"Books": []})
    
    def put(self, request, format=None):
        books = Book.objects.all()
        target_book = books.get(
            book_title=request.data['target_book_title']
        )
        target_book.author = Author.objects.get(Q(first_name=request.data['author_first_name']))
        target_book.category = request.data['category']
        target_book.book_title = request.data['book_title']
        target_book.price = request.data['price']
        target_book.number_of_pages = request.data['number_of_pages']
        target_book.language = request.data['language']
        target_book.slug = request.data['slug']
        target_book.save()
        return Response({"Books": []})

class BookDetail(APIView):
    def get_object(self, author_slug, book_slug):
        try:
            return Author.objects.filter(author__slug=author_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, author_slug, book_slug, format=None):
        book = self.get_object(author_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get_object(self, author_slug):
        try:
            return Author.objects.get(slug=author_slug)
        except Author.DoesNotExist:
            raise Http404
    
    def get(self, request, author_slug, format=None):
        author = self.get_object(author_slug)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

@api_view(['POST'])
def author_search(request):
    query = request.data.get('query', '')

    if query:
        authors = Author.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response({"Authors": []})

@api_view(['POST'])
def book_search(request):
    query = request.data.get('query', '')

    if query:
        books = Book.objects.filter(Q(book_title__icontains=query))
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({"Books": []})