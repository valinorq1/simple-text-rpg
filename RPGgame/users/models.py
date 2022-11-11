from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(default="Игрок", max_length=32, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    silver = models.IntegerField("Серебро", default=500)
    gold = models.IntegerField("Золото", default=120)
    level = models.IntegerField("Уровень", default=1)
    expirience = models.FloatField("Текущий опыт", default=0.0)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} #{self.pk}"
    
    class Meta:
        db_table = "user"
 
@receiver(post_save, sender=CustomUser)
def create_inventory_for_user(sender, instance, **kwargs):
    """receive new user and create inventory for him"""
    Inventory.objects.get_or_create(user=instance)
    
    
   
class Inventory(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cells_count = models.IntegerField(default=100)
    
    
    class Meta:
        db_table = "inventory"
        verbose_name = 'inventory'
        verbose_name_plural = 'inventory'