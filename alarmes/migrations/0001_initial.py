# Generated by Django 4.2.1 on 2024-11-04 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('intervalo_horas', models.IntegerField(help_text='Intervalo entre doses em horas.')),
                ('duracao_dias', models.IntegerField(help_text='Duração do tratamento em dias')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicamentos.medicamento')),
            ],
        ),
    ]
