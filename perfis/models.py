from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    # email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil')
    
    @property
    def email(self):
        return self.usuario.email

    def convidar(self, p_convidado):
        Convite(solicitante=self, convidado=p_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()
   