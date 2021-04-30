from django.core.signals import request_finished
from django.core.signals import request_finished
from django.dispatch import receiver



@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished.................!")



request_finished.connect(my_callback)


