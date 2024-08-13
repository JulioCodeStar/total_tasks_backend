from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import UsersModel

# Create your views here.
class UserRegisterView(ModelViewSet):
    queryset = UsersModel.objects.all()  # Define el conjunto de datos
    serializer_class = UserSerializer  # Asigna el serializador

    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)