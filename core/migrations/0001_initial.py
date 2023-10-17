# Generated by Django 4.2.6 on 2023-10-17 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=2000)),
                ('codigo', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=5000)),
                ('horario_inicio', models.TimeField()),
                ('horario_fim', models.TimeField()),
                ('local', models.CharField(max_length=5000)),
                ('ativo', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.participacao')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala')),
            ],
        ),
        migrations.AddField(
            model_name='participacao',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sala'),
        ),
    ]