from django.db import models
from django.core.validators import MinLengthValidator
class NewsUsers(models.Model):
    name = models.CharField(max_length = 60, blank=False, null=False)
    email = models.EmailField(blank=False,null=False)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "NewsUser"
        verbose_name_plural = "NewsUsers"

    def __str__(self):
        return self.email
