# Generated by Django 3.2.16 on 2023-02-01 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0002_alter_produtos_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='nota fiscal')),
                ('movimentacao', models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], max_length=1)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('saldo', models.PositiveIntegerField()),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque_produtos.estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produtos')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
