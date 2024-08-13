from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from .auth_manager import UsuarioManager

# Create your models here.
class UsersModel(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Si queremos ingresar al panel administrativo que atributo utilizara para pedirle al usuario
    USERNAME_FIELD = 'email'

    # Cuando queremos crear un super usuario por la terminal que atributos nos debe pedir
    REQUIRED_FIELDS = ['nombres', 'apellidos']
    
    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'