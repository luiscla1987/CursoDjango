from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    class Meta:
        verbose_name_plural = "autores"
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome