from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_superuser(self, email, nombres, apellidos, password):
        if not email:
            return ValueError("El usuario debe tener un correo")
        
        email_personalizado = self.normalize_email(email)
        
        nuevo_usuario = self.model(email=email_personalizado, nombres=nombres, apellidos=apellidos)
        nuevo_usuario.set_password(password)
        
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True
        
        nuevo_usuario.save()