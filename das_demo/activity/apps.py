from django.apps import AppConfig


class ActivityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'das_demo.activity'

    def ready(self):
        from actstream import registry
        from das_demo.user.models import User
        registry.register(User)
