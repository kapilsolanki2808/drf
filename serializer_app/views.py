from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializer import CommentSerializer,BlogPostSerializer
from rest_framework import status

class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Validate(APIView):

    
    def post(self, request, *args, **kwargs):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
