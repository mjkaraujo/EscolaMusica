# Generated by Django 4.1.4 on 2023-02-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=150, verbose_name='Nome')),
                ('email_contato', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone_contato', models.CharField(max_length=14, verbose_name='Telefone')),
                ('mensagem_contato', models.TextField(verbose_name='Mensagem')),
            ],
        ),
    ]
