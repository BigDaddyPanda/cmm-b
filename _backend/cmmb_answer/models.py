from django.db import models

# Create your models here.


class Premisse(models.Model):
    english_format = models.CharField(max_length=200)
    french_format = models.CharField(max_length=200)


class Conclusion(models.Model):
    english_format = models.CharField(max_length=200)
    french_format = models.CharField(max_length=200)


class Regle(models.Model):
    cle_premisse = models.ForeignKey(Premisse, on_delete=models.CASCADE)
    cle_conclusion = models.ForeignKey(Conclusion, on_delete=models.CASCADE)
    
