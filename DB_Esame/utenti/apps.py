from django.apps import AppConfig


class UtentiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utenti'
    
def ready(self):
    import utenti.models
