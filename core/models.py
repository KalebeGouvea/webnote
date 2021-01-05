from django.db import models

class Nota(models.Model):
    texto = models.CharField(max_length=1000, blank=False, null=False)
    data_edicao = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=254, blank=False, null=False)

    def __str__(self):
        return self.texto