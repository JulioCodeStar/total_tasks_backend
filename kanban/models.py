from django.db import models
from users.models import UsersModel

# Create your models here.
class project(models.Model):
    name        = models.CharField(max_length=255, blank=False, null=False)
    status      = models.CharField(max_length=50, blank=False, null=False, choices=[
        ('Sin Empezar', 'Sin Empezar'),
        ('En Cursor', 'En Cursor'),
        ('Listo', 'Listo'),
        ('Archivado', 'Archivado')
    ])
    priory      = models.CharField(max_length=255, blank=False, null=False)
    init_date   = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Foreign Key constraints
    user_id = models.ForeignKey(UsersModel, on_delete=models.CASCADE, verbose_name='user_id')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'


class task(models.Model):
    name        = models.CharField(max_length=255, blank=False, null=False)
    status      = models.CharField(max_length=50, blank=False, null=False, choices=[
        ('Sin Empezar', 'Sin Empezar'),
        ('En Curso', 'En Curso'),
        ('Listo', 'Listo'),
        ('Archivado', 'Archivado')
    ])
    description = models.TextField(blank=True, null=True)
    finish_date = models.DateField(null=True, blank=True)

    # Foreign Key constraints
    user_id     = models.ForeignKey(UsersModel, on_delete=models.CASCADE, verbose_name='user_id')
    project_id  = models.ForeignKey(project, on_delete=models.CASCADE, verbose_name='project_id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='tasks'


class subtask(models.Model): 
    name        = models.CharField(max_length=255, blank=False, null=False)
    status      = models.CharField(max_length=50, blank=False, null=False, choices=[
        ('Sin Empezar', 'Sin Empezar'),
        ('En Curso', 'En Curso'),
        ('Listo', 'Listo'),
        ('Archivado', 'Archivado')
    ])
    description = models.TextField(blank=True, null=True)
    finish_date = models.DateField(null=True, blank=True)

    # Foreign Key constraints
    user_id     = models.ForeignKey(UsersModel, on_delete=models.CASCADE, verbose_name='user_id')
    task_id  = models.ForeignKey(task, on_delete=models.CASCADE, verbose_name='task_id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table ='sub_tasks'