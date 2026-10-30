from datetime import datetime

def  global_site_info(request):

    return{
        'site_name': 'coffelito',
        'current_year': datetime.now().year,
        }
