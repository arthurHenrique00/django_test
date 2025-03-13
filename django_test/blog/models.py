from django.db import models

class Projeto(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

