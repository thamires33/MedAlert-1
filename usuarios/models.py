from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from usuarios.constants import ESTADOS_BRASIL, ESPECIALIDADES

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, help_text="E-mail do usuário")
    username = models.CharField(max_length=150, unique=True, help_text="Nome de usuário")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    

    def __str__(self):
        return self.email

class Medico(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, help_text="Usuário que é médico")
    crm = models.CharField(max_length=10, help_text="Número do CRM do médico")
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASIL, help_text="Sigla do estado onde o médico atua")
    especialidade = models.CharField(max_length=3, choices=ESPECIALIDADES, help_text="Número da especialidade do médico")

    class Meta:
        unique_together = ('crm', 'estado')

    def __str__(self):
        return f'CRM/{self.estado} {self.crm}'
    
class Paciente(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, help_text="Usuário que é paciente")
    idade = models.IntegerField(help_text="Idade do paciente")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - ({self.user.email})"