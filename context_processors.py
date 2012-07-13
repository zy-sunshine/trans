from django.conf import settings

def common(request):
    """
    Adds site config context variables to the context.

    """
    return {'SITE_CONFIG': settings.SITE_CONFIG, 
            'IMAGES_URL': settings.IMAGES_URL,
            }
