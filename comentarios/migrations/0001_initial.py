# Generated by Django 4.1.4 on 2023-02-04 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150, verbose_name='Nome')),
                ('email_comentario', models.EmailField(max_length=254, verbose_name='email')),
                ('comentario', models.TextField(verbose_name='comentario')),
                ('data_comentario', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('publicado_comentario', models.BooleanField(default=False, verbose_name='Publicado')),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post')),
                ('usuario_comentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
