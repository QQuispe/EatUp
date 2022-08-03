from django.conf import settings


def global_settings(request):
    return {
        'GOOGLE_MAPS_KEY': settings.GOOGLE_MAPS_KEY
    }