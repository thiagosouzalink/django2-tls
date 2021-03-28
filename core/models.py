from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

from stdimage.models import StdImageField


class Base(models.Model):
    
    created_at = models.DateField('Data de Criação', auto_now_add=True)
    updated_at = models.DateField('Data de Atualização', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):

    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Estoque')
    image = StdImageField('Imagem', upload_to='produtos',variations={'thumb':(124,124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)

signals.pre_save.connect(produto_pre_save, sender=Produto)