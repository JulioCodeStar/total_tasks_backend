from .models import UsersModel
from rest_framework.serializers import ModelSerializer, CharField

class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    
    class Meta:
        model = UsersModel
        fields = ['email', 'nombres', 'apellidos', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
            'nombres': {'required': True},
            'apellidos': {'required': True},
        }
        
        def create(self, validate_data):
            userRegister = UsersModel.objects.create(
                email = validate_data['email'],
                nombres = validate_data['nombres'],
                apellidos = validate_data['apellidos']
            )
            
            userRegister.set_password(validate_data['password'])
            userRegister.save()
            
            return userRegister