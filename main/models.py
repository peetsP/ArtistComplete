from django.db import models

# Create your models here. img, name, header, desc


class Music(models.Model):
    music_img = models.ImageField(blank = False)
    music_name = models.CharField(max_length = 20)
    prod_name = models.CharField(max_length = 20)
    music_desc = models.TextField(max_length = 150)

    def __str__(self):
        return self.music_name

