# Generated by Django 3.2.3 on 2021-05-26 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historicos',
            fields=[
                ('id_historico', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('aparecimento_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('duracao_sintomas', models.CharField(blank=True, max_length=100, null=True)),
                ('local_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_dor', models.CharField(blank=True, max_length=100, null=True)),
                ('conclusao', models.TextField(blank=True, null=True)),
                ('id_agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicos', to='agendamentos.agendamentos')),
            ],
            options={
                'db_table': 'historicos',
                'managed': True,
            },
        ),
    ]
