from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Comment
from .serializers import CommentSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
#@authentication_classes([SessionAuthentication])
#@permission_classes([IsAuthenticatedOrReadOnly])
def comments(req: Request, pk=None):
	if req.method == 'GET':
		if pk != None:
			try:
				queryset = Comment.objects.get(id=pk)
			except Comment.DoesNotExist:
				return Response({ 'error': 'This item doesn\'t exist.' })

			serializer = CommentSerializer(queryset)
			return Response(serializer.data)

		else:
			queryset = Comment.objects.all()
			serializer = CommentSerializer(queryset, many=True)
			return Response(serializer.data)

	elif req.method == 'POST':
		serializer = CommentSerializer(data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response({ 'error:': 'Error adding comment!' }, status=400)

	elif req.method == 'PUT':
		try:
			queryset = Comment.objects.get(id=pk)
		except Comment.DoesNotExist:
			return Response({ 'error': 'This item doesn\'t exist.' })

		serializer = CommentSerializer(instance=queryset, data=req.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response({ 'error:': 'Error updating comment!' }, status=400)

	elif req.method == 'DELETE':
		try:
			queryset = Comment.objects.get(id=pk)
		except Comment.DoesNotExist:
			return Response({ 'error': 'This item doesn\'t exist.' })
		
		queryset.delete()
		return Response({ 'message': 'Comment deleted successfully!' })


