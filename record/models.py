from django.db import models

# Create your models here.
# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nama_lengkap = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=50, null=True)
    pendidikan = models.CharField(max_length=150, null=True)
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap
    class Meta:
        verbose_name_plural = "Records"