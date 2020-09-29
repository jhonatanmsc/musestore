import datetime

from django.db import models


class SubCategory(models.Model):
    title = models.CharField(u'título', max_length=120)

    class Meta:
        verbose_name = 'Sub categoria'
        verbose_name_plural = 'Sub categorias'

    def __str__(self):
        return f'Produto: {self.name}, criado em: {self.created_at.strftime("%d/%m%Y")}'


class Product(models.Model):
    name = models.CharField(u'nome', max_length=120)
    description = models.TextField(u'descrição', max_length=254, null=True, blank=True)
    price = models.DecimalField(u'preço', max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField(u'foto', upload_to='product', max_length=254, null=True, blank=True)
    category = models.CharField(u'categoria', max_length=100)
    sub_categories = models.ManyToManyField(SubCategory, verbose_name=u'sub categorias')
    created_at = models.DateTimeField(u'criado em', auto_now=True)
    updated_at = models.DateTimeField(u'atualizado em', auto_now_add=True)
    is_active = models.BooleanField(u'ativo', default=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'Produto: {self.name}, criado em: {self.created_at.strftime("%d/%m%Y")}'
