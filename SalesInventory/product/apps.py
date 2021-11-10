from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'

    def ready(self):
        print("ready of signal called")
        import product.signals
        pass