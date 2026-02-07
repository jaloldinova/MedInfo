from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=200, verbose_name="Dori nomi")
    description = models.TextField(verbose_name="Dori haqida")
    usage = models.TextField(verbose_name="Nimaga ishlatiladi")
    side_effects = models.TextField(verbose_name="Nojo'ya ta'siri")
    image = models.ImageField(upload_to="images/", verbose_name="Dori image",blank=True,null=True)
    def __str__(self):
        return self.name

