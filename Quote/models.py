from django.db import models
from django.shortcuts import reverse


class Quote(models.Model):
    company_name = models.CharField(max_length=100)
    attention = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    date = models.DateField()
    site = models.CharField(max_length=100)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.company_name + '-' + str(self.date)

    def get_absolute_url(self):
        return reverse('add_item', kwargs={'pk': self.id})


class Item(models.Model):
    HEAVY_DUTY_CUPLOCK = 'HDC'
    ALUMINIUM = 'AL'
    CORE_CUTTING = 'CRC'
    CONCRETE_CUTTING = 'CTC'
    SCAFFOLDING = 'SF'
    ITEM_CHOICES = (
        (HEAVY_DUTY_CUPLOCK, 'Heavy Duty Cuplock'),
        (ALUMINIUM, 'Aluminium'),
        (CORE_CUTTING, 'Core Cutting'),
        (CONCRETE_CUTTING, 'Concrete Cutting'),
        (SCAFFOLDING, 'Scaffolding'),
    )
    item = models.CharField(choices=ITEM_CHOICES, max_length=3, null=True)
    description = models.CharField(max_length=200)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    hiring_days = models.IntegerField(null=True)
    total = models.FloatField()
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.total:
            self.total = self.unit_price * self.quantity
        self.quote.total += self.total
        self.quote.save()
        return super(Item, self).save()

    def delete(self, using=None, keep_parents=False):
        self.quote.total -= self.total
        self.quote.save()
        return super(Item, self).delete()

    def get_absolute_url(self):
        return reverse('add_item', kwargs={'pk': self.quote.id})


class Terms(models.Model):
    terms = models.TextField(max_length=5000)

    def __str__(self):
        return self.terms
