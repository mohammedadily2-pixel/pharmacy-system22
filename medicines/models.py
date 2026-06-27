from django.db import models
from django.utils import timezone
from datetime import timedelta

class Medicine(models.Model):
    CATEGORY_CHOICES = [
        ('antibiotic', 'Antibiotic'),
        ('painkiller', 'Painkiller'),
        ('vitamin', 'Vitamin'),
        ('syrup', 'Syrup'),
        ('tablet', 'Tablet'),
        ('injection', 'Injection'),
        ('other', 'Nyingine'),
    ]

    name            = models.CharField(max_length=200, verbose_name="Jina la Dawa")
    category        = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Aina")
    quantity        = models.IntegerField(verbose_name="Idadi")
    price           = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Bei (TZS)")
    manufacture_date = models.DateField(verbose_name="Tarehe ya Kuzalishwa")
    expiry_date     = models.DateField(verbose_name="Tarehe ya Kuisha")
    supplier        = models.CharField(max_length=200, verbose_name="Msambazaji")
    description     = models.TextField(blank=True, verbose_name="Maelezo")
    date_added      = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.expiry_date < timezone.now().date()

    def is_expiring_soon(self):
        # Dawa zinazokwisha ndani ya siku 30
        soon = timezone.now().date() + timedelta(days=30)
        return self.expiry_date <= soon and not self.is_expired()

    def days_until_expiry(self):
        delta = self.expiry_date - timezone.now().date()
        return delta.days

    def status(self):
        if self.is_expired():
            return 'expired'
        elif self.is_expiring_soon():
            return 'expiring_soon'
        return 'good'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['expiry_date']
        verbose_name = "Dawa"
        verbose_name_plural = "Dawa"
# Create your models here.
