from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Authentication'
    def ready(self):
        import Authentication.signals 
