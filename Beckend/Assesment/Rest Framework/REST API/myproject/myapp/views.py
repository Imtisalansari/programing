from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from comments.serializers.json_serializer import CommentSerializer
from comments.modules import comment_logic

@api_view(['GET'])
def get_comments(request):
    comments = comment_logic.get_all_comments()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        comment_logic.create_comment(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_comment(request, pk):
    success = comment_logic.delete_comment(pk)
    if success:
        return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
