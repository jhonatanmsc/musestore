# Generated by Django 3.1.1 on 2020-09-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_categories',
            field=models.ManyToManyField(to='core.SubCategory', verbose_name='sub categorias'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='atualizado em'),
        ),
    ]
