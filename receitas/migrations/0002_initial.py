# Generated by Django 4.2.1 on 2024-11-05 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receitas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='medico',
            field=models.ForeignKey(help_text='Médico que irá preescrever a receita', on_delete=django.db.models.deletion.CASCADE, to='usuarios.medico'),
        ),
        migrations.AddField(
            model_name='receita',
            name='paciente',
            field=models.ForeignKey(help_text='Paciente que irá receber a receita', on_delete=django.db.models.deletion.CASCADE, to='usuarios.paciente'),
        ),
    ]
