from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from books.serializers import BookSerializer
from rest_framework import generics, status
from books.models import Book

from rest_framework import viewsets


# Functions APIViews.
# Class APIViews.
# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookListAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)


class BookDetailAPIView(APIView):

    def get(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
                "status": f"Successful",
                "books": serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": "False",
                    "message": "Book is not found",
                },
                status=status.HTTP_404_NOT_FOUND
            )


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateAPIView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response(
                {
                    'status': True,
                    'message': f"Book {book_saved} updated successfully"
                }
            )


class BookDeleteAPIView(APIView):

    # delete file with get_object_or_404
    # def delete(self, request, pk):
    #     book = get_object_or_404(Book,pk=pk)
    #     book.delete()
    #     return Response(
    #         {
    #             'status': True,
    #             'message': 'Successfully deleted'
    #
    #         }
    #     )

    # delete file with get_object_or_404

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    'status': True,
                    'message': 'Successfully deleted'

                }
            )
        except Exception as err:
            print(err)
            return Response(
                {
                    'status': False,
                    'message': 'Book is not found'
                }
            )


# class BookDestroyAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookCreateAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        # print(data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': f"books are saved to the database",
                'books': data
            }
            return Response(response_data)


# class BookListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
