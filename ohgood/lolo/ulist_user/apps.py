from django.apps import AppConfig


class UlistUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ulist_user'

    def ready(self):
        import ulist_user.signals
