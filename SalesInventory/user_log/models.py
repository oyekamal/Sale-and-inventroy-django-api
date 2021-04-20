from django.db import models

# Create your models here.
class Log(models.Model):
    request_username  = models.CharField(max_length=200)
    request_method = models.CharField(max_length=50)
    request_url = models.CharField(max_length=255)
    request_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = ("Log")
        verbose_name_plural = ("Logs")

    def __str__(self):
        return self.request_username

    def get_absolute_url(self):
        return reverse("Log_detail", kwargs={"pk": self.pk})
