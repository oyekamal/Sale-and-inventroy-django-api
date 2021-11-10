from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from cmdbox.profiles.models import Profile


# Create your models here.
class Log(models.Model):
    request_username  = models.CharField(max_length=200)
    request_method = models.CharField(max_length=50)
    request_url = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)
    request_data = models.JSONField(default=dict)
    response_data = models.JSONField(default=dict)

    class Meta:
        verbose_name = ("Log")
        verbose_name_plural = ("Logs")

        permissions = [
            ("can_search", "Can search the web"),
        ]

    def __str__(self):
        return self.request_username

    

    # def get_absolute_url(self):
    #     return reverse("Log_detail", kwargs={"pk": self.pk})

# @receiver(post_save, sender=Log)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         # Profile.objects.create(user=instance)
#         print("yes log is save ")
