from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.


class StockQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class StockManager(models.Manager):

    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, my_id):
        qs = self.get_queryset().filter(id=my_id)
        if qs.exists() and qs.count() == 1:
            return qs.first()
        else:
            return None


class Stock(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField(default='No description is available.')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=20, blank=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StockManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('stocks_url:stock_detail_slug', kwargs={'slug': self.slug})


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    order_id = models.CharField(max_length=120, blank=True, unique=True)
    stocks = models.ManyToManyField(Stock, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'''{self.__dict__}'''
