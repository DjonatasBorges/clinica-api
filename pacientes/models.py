from django.db import models


# criando modelo pacientes


class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    data_de_nasc = models.DateTimeField(null=True, blank=True)
    endereco_rua = models.CharField(max_length=300, blank=True, null=True)
    endereco_numero = models.IntegerField(null=True, blank=True)
    endereco_bairro = models.CharField(max_length=100, blank=True, null=True)
    endereco_CEP = models.IntegerField(null=True, blank=True)
    endereco_cidade = models.CharField(max_length=300, null=True, blank=True)
    DDD_telefone = models.IntegerField(null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)
    rg = models.CharField(max_length=9, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'pacientes'
