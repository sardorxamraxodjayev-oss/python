from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import render

# --- Charts ---
def charts_chartjs(request):
    return render(request, template_name='charts-chartjs.html')

def charts_flot(request):
    return render(request, template_name='charts-flot.html')

def charts_peity(request):
    return render(request, template_name='charts-peity.html')

# --- Fonts ---
def font_fontawesome(request):
    return render(request, template_name='font-fontawesome.html')

def font_themify(request):
    return render(request, template_name='font-themify.html')

# --- Forms ---
def forms_advanced(request):
    return render(request, template_name='forms-advanced.html')

def forms_basic(request):
    return render(request, template_name='forms-basic.html')

# --- Dashboard / Main ---
def index(request):
    return render(request, template_name='index.html')

# --- Maps ---
def maps_gmap(request):
    return render(request, template_name='maps-gmap.html')

def maps_vector(request):
    return render(request, template_name='maps-vector.html')

# --- Pages / Auth ---
def page_login(request):
    return render(request, template_name='page-login.html')

def page_register(request):
    return render(request, template_name='page-register.html')

def pages_forget(request):
    return render(request, template_name='pages-forget.html')

# --- Tables ---
def tables_basic(request):
    return render(request, template_name='tables-basic.html')

def tables_data(request):
    return render(request, template_name='tables-data.html')

# --- UI Elements ---
def ui_alerts(request):
    return render(request, template_name='ui-alerts.html')

def ui_badges(request):
    return render(request, template_name='ui-badges.html')

def ui_buttons(request):
    return render(request, template_name='ui-buttons.html')

def ui_cards(request):
    return render(request, template_name='ui-cards.html')

def ui_grids(request):
    return render(request, template_name='ui-grids.html')

def ui_modals(request):
    return render(request, template_name='ui-modals.html')

def ui_progressbar(request):
    return render(request, template_name='ui-progressbar.html')

def ui_switches(request):
    return render(request, template_name='ui-switches.html')

def ui_tabs(request):
    return render(request, template_name='ui-tabs.html')

def ui_typography(request):
    return render(request, template_name='ui-typgraphy.html')

# --- Widgets ---
def widgets(request):
    return render(request, template_name='widgets.html')








 











# def index_html(request):
#     return render(request, template_name='index.html')

# def charts_chartjs(request):
#     return render(request, template_name='charts-chartjs.html')

# def charts_flot(request):
#     return render(request, template_name='charts-flot.html')

# def charts_peity(request):
#     return render(request, template_name='charts-peity.html')

# def font_fonteawesome(request):
#     return render(request, template_name='font-fonteawesome.html')

# def font_themify(request):
#     return render(request, template_name='font_themify.html')

# def forms_advanced(request):
#     return render (request, template_name='forms_advanced.html')

# def  forms_basic(request):
#     return render(request, template_name='forms_basic.html')

# def maps_gmap(request):
#     return render(request, template_name='maps_gmap')


# def maps_vector(request):
#     return render(request, template_name= 'maps_vector')

# def page_login(request):
#     return render (request, template_name='page_login')



#TEMPLATE_NAME DAGI HAMMI PASTGI _ CHIZIQLANI - GA OTQAZISH KERAK VA HAMMASIGA .HTML QOSHOSH KERAK #