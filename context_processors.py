from django.conf import settings

def common(request):
    """
    Adds site config context variables to the context.

    """
    return {'SITE': settings.SITE_CONFIG, 
            #'MEDIA_URL': settings.MEDIA_URL,
            #'STATIC_URL': settings.STATIC_URL,
            }
