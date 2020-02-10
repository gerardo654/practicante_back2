#servira como view - enlace entre peticion y serializador
from rest_framework.response import Response
from .serializers import UserSerializers
from rest_framework.views import APIView
from rest_framework import status

class UserAPI(APIView):
	def post(self, request):
		serializer = UserSerializers(data = request.data) #la info enviada en la info esta en request.data
		if serializer.is_valid(raise_exception=True):
			user = serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED )

