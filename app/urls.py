from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import index, ui_badges, ui_tabs, ui_cards, ui_alerts, ui_progressbar, ui_modals, ui_switches, ui_grids, ui_typography, tables_basic, tables_data, forms_basic, forms_advanced, font_fontawesome, font_themify, charts_chartjs, charts_flot, charts_peity, maps_gmap, maps_vector, page_login, page_register, pages_forget
from .views import charts_chartjs, ui_badges, ui_tabs, ui_cards, ui_alerts, ui_progressbar, ui_modals, ui_switches, ui_grids, ui_typography, tables_basic, tables_data, forms_basic, forms_advanced, font_fontawesome, font_themify, charts_chartjs, charts_flot, charts_peity, maps_gmap, maps_vector, page_login, page_register, pages_forget
from .views import charts_flot,  ui_badges, ui_tabs, ui_cards, ui_alerts, ui_progressbar, ui_modals, ui_switches, ui_grids, ui_typography, tables_basic, tables_data, forms_basic, forms_advanced, font_fontawesome, font_themify, charts_chartjs, charts_flot, charts_peity, maps_gmap, maps_vector, page_login, page_register, pages_forget

urlpatterns = [

    path('', views.index, name='index'),

    path('ui-badges/', ui_badges, name = 'ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name = 'ui_cards'),
    path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
    path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/',ui_switches,name='ui_switches'),
    path('ui-grids/',ui_grids,name='ui_grids'),
    path('ui_typography/',ui_typography,name='ui_typography'),
    path('tables-basic/',tables_basic,name='tables_basic'),
    path('tables_data/',tables_data,name='tables_data'),
    path('forms_basic/',forms_basic,name='forms_basic'),
    path('forms_advanced/',forms_advanced,name='forms_advanced'),
    path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
    path('font_themify/',font_themify, name ='font_themify'),
    path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
    path('charts_flot/',charts_flot, name ='charts_flot'),
    path('charts_peity/',charts_peity, name ='charts_peity'),
    path('maps_gmap/',maps_gmap, name ='maps_gmap'),
    path('maps_vector/',maps_vector, name ='maps_vector'),
    path('page_login/',page_login, name ='page_login'),
    path('page_register/',page_register, name ='page_register'),
    path('pages_forget/',pages_forget, name ='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets')

    # ---------



    
]


urlpatterns = [

    path('', views.charts_chartjs, name='charts_chartjs'),



    path('ui-badges/', ui_badges, name = 'ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name = 'ui_cards'),
    path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
    path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/',ui_switches,name='ui_switches'),
    path('ui-grids/',ui_grids,name='ui_grids'),
    path('ui_typography/',ui_typography,name='ui_typography'),
    path('tables-basic/',tables_basic,name='tables_basic'),
    path('tables_data/',tables_data,name='tables_data'),
    path('forms_basic/',forms_basic,name='forms_basic'),
    path('forms_advanced/',forms_advanced,name='forms_advanced'),
    path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
    path('font_themify/',font_themify, name ='font_themify'),
    path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
    path('charts_flot/',charts_flot, name ='charts_flot'),
    path('charts_peity/',charts_peity, name ='charts_peity'),
    path('maps_gmap/',maps_gmap, name ='maps_gmap'),
    path('maps_vector/',maps_vector, name ='maps_vector'),
    path('page_login/',page_login, name ='page_login'),
    path('page_register/',page_register, name ='page_register'),
    path('pages_forget/',pages_forget, name ='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets')
    
    ]




urlpatterns = [
    path ('', views.charts_flot, name= 'charts_flot'),



    path('ui-badges/', ui_badges, name = 'ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name = 'ui_cards'),
    path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
    path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/',ui_switches,name='ui_switches'),
    path('ui-grids/',ui_grids,name='ui_grids'),
    path('ui_typography/',ui_typography,name='ui_typography'),
    path('tables-basic/',tables_basic,name='tables_basic'),
    path('tables_data/',tables_data,name='tables_data'),
    path('forms_basic/',forms_basic,name='forms_basic'),
    path('forms_advanced/',forms_advanced,name='forms_advanced'),
    path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
    path('font_themify/',font_themify, name ='font_themify'),
    path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
    path('charts_flot/',charts_flot, name ='charts_flot'),
    path('charts_peity/',charts_peity, name ='charts_peity'),
    path('maps_gmap/',maps_gmap, name ='maps_gmap'),
    path('maps_vector/',maps_vector, name ='maps_vector'),
    path('page_login/',page_login, name ='page_login'),
    path('page_register/',page_register, name ='page_register'),
    path('pages_forget/',pages_forget, name ='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets')

]

urlpatterns = [
    path ('', views.charts_peity, name = 'charts_peity'),





    path('ui-badges/', ui_badges, name = 'ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name = 'ui_cards'),
    path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
    path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/',ui_switches,name='ui_switches'),
    path('ui-grids/',ui_grids,name='ui_grids'),
    path('ui_typography/',ui_typography,name='ui_typography'),
    path('tables-basic/',tables_basic,name='tables_basic'),
    path('tables_data/',tables_data,name='tables_data'),
    path('forms_basic/',forms_basic,name='forms_basic'),
    path('forms_advanced/',forms_advanced,name='forms_advanced'),
    path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
    path('font_themify/',font_themify, name ='font_themify'),
    path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
    path('charts_flot/',charts_flot, name ='charts_flot'),
    path('charts_peity/',charts_peity, name ='charts_peity'),
    path('maps_gmap/',maps_gmap, name ='maps_gmap'),
    path('maps_vector/',maps_vector, name ='maps_vector'),
    path('page_login/',page_login, name ='page_login'),
    path('page_register/',page_register, name ='page_register'),
    path('pages_forget/',pages_forget, name ='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets')


]

urlpatterns = [
    path ('', views.font_fontawesome, name= 'font_fontawesome'),
       path('ui-badges/', ui_badges, name = 'ui_badges'),
        path('ui-tabs/', ui_tabs, name='ui_tabs'),
        path('ui-cards/', ui_cards, name = 'ui_cards'),
        path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
        path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
        path('ui-modals/', ui_modals, name='ui_modals'),
        path('ui-switches/',ui_switches,name='ui_switches'),
        path('ui-grids/',ui_grids,name='ui_grids'),
        path('ui_typography/',ui_typography,name='ui_typography'),
        path('tables-basic/',tables_basic,name='tables_basic'),
        path('tables_data/',tables_data,name='tables_data'),
        path('forms_basic/',forms_basic,name='forms_basic'),
        path('forms_advanced/',forms_advanced,name='forms_advanced'),
        path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
        path('font_themify/',font_themify, name ='font_themify'),
        path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
        path('charts_flot/',charts_flot, name ='charts_flot'),
        path('charts_peity/',charts_peity, name ='charts_peity'),
        path('maps_gmap/',maps_gmap, name ='maps_gmap'),
        path('maps_vector/',maps_vector, name ='maps_vector'),
        path('page_login/',page_login, name ='page_login'),
        path('page_register/',page_register, name ='page_register'),
        path('pages_forget/',pages_forget, name ='pages_forget'),
    
        # --- Charts ---
        path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
        path('charts/flot/', views.charts_flot, name='charts_flot'),
        path('charts/peity/', views.charts_peity, name='charts_peity'),
    
        # --- Fonts ---
        path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
        path('font/themify/', views.font_themify, name='font_themify'),
    
        # --- Forms ---
        path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
        path('forms/basic/', views.forms_basic, name='forms_basic'),
    
        # --- Maps ---
        path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
        path('maps/vector/', views.maps_vector, name='maps_vector'),
    
        # --- Pages / Auth ---
        path('page/login/', views.page_login, name='page_login'),
        path('page/register/', views.page_register, name='page_register'),
        path('pages/forget/', views.pages_forget, name='pages_forget'),
    
        # --- Tables ---
        path('tables/basic/', views.tables_basic, name='tables_basic'),
        path('tables/data/', views.tables_data, name='tables_data'),
    
        # --- UI Elements ---
        path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
        path('ui/badges/', views.ui_badges, name='ui_badges'),
        path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
        path('ui/cards/', views.ui_cards, name='ui_cards'),
        path('ui/grids/', views.ui_grids, name='ui_grids'),
        path('ui/modals/', views.ui_modals, name='ui_modals'),
        path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
        path('ui/switches/', views.ui_switches, name='ui_switches'),
        path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
        path('ui/typography/', views.ui_typography, name='ui_typography'),
    
        
    
        # --- Widgets ---
        path('widgets/', views.widgets, name='widgets')

]


urlpatterns = [
        path ('', views.font_themify, name= 'font_themify'),
        path('ui-badges/', ui_badges, name = 'ui_badges'),
        path('ui-tabs/', ui_tabs, name='ui_tabs'),
        path('ui-cards/', ui_cards, name = 'ui_cards'),
        path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
        path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
        path('ui-modals/', ui_modals, name='ui_modals'),
        path('ui-switches/',ui_switches,name='ui_switches'),
        path('ui-grids/',ui_grids,name='ui_grids'),
        path('ui_typography/',ui_typography,name='ui_typography'),
        path('tables-basic/',tables_basic,name='tables_basic'),
        path('tables_data/',tables_data,name='tables_data'),
        path('forms_basic/',forms_basic,name='forms_basic'),
        path('forms_advanced/',forms_advanced,name='forms_advanced'),
        path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
        path('font_themify/',font_themify, name ='font_themify'),
        path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
        path('charts_flot/',charts_flot, name ='charts_flot'),
        path('charts_peity/',charts_peity, name ='charts_peity'),
        path('maps_gmap/',maps_gmap, name ='maps_gmap'),
        path('maps_vector/',maps_vector, name ='maps_vector'),
        path('page_login/',page_login, name ='page_login'),
        path('page_register/',page_register, name ='page_register'),
        path('pages_forget/',pages_forget, name ='pages_forget'),
    
        # --- Charts ---
        path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
        path('charts/flot/', views.charts_flot, name='charts_flot'),
        path('charts/peity/', views.charts_peity, name='charts_peity'),
    
        # --- Fonts ---
        path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
        path('font/themify/', views.font_themify, name='font_themify'),
    
        # --- Forms ---
        path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
        path('forms/basic/', views.forms_basic, name='forms_basic'),
    
        # --- Maps ---
        path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
        path('maps/vector/', views.maps_vector, name='maps_vector'),
    
        # --- Pages / Auth ---
        path('page/login/', views.page_login, name='page_login'),
        path('page/register/', views.page_register, name='page_register'),
        path('pages/forget/', views.pages_forget, name='pages_forget'),
    
        # --- Tables ---
        path('tables/basic/', views.tables_basic, name='tables_basic'),
        path('tables/data/', views.tables_data, name='tables_data'),
    
        # --- UI Elements ---
        path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
        path('ui/badges/', views.ui_badges, name='ui_badges'),
        path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
        path('ui/cards/', views.ui_cards, name='ui_cards'),
        path('ui/grids/', views.ui_grids, name='ui_grids'),
        path('ui/modals/', views.ui_modals, name='ui_modals'),
        path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
        path('ui/switches/', views.ui_switches, name='ui_switches'),
        path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
        path('ui/typography/', views.ui_typography, name='ui_typography'),
    
        
    
        # --- Widgets ---
        path('widgets/', views.widgets, name='widgets')

]



urlpatterns = [
        path ('', views.font_themify, name= 'font_themify'),
        path('ui-badges/', ui_badges, name = 'ui_badges'),
        path('ui-tabs/', ui_tabs, name='ui_tabs'),
        path('ui-cards/', ui_cards, name = 'ui_cards'),
        path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
        path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
        path('ui-modals/', ui_modals, name='ui_modals'),
        path('ui-switches/',ui_switches,name='ui_switches'),
        path('ui-grids/',ui_grids,name='ui_grids'),
        path('ui_typography/',ui_typography,name='ui_typography'),
        path('tables-basic/',tables_basic,name='tables_basic'),
        path('tables_data/',tables_data,name='tables_data'),
        path('forms_basic/',forms_basic,name='forms_basic'),
        path('forms_advanced/',forms_advanced,name='forms_advanced'),
        path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
        path('font_themify/',font_themify, name ='font_themify'),
        path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
        path('charts_flot/',charts_flot, name ='charts_flot'),
        path('charts_peity/',charts_peity, name ='charts_peity'),
        path('maps_gmap/',maps_gmap, name ='maps_gmap'),
        path('maps_vector/',maps_vector, name ='maps_vector'),
        path('page_login/',page_login, name ='page_login'),
        path('page_register/',page_register, name ='page_register'),
        path('pages_forget/',pages_forget, name ='pages_forget'),
    
        # --- Charts ---
        path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
        path('charts/flot/', views.charts_flot, name='charts_flot'),
        path('charts/peity/', views.charts_peity, name='charts_peity'),
    
        # --- Fonts ---
        path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
        path('font/themify/', views.font_themify, name='font_themify'),
    
        # --- Forms ---
        path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
        path('forms/basic/', views.forms_basic, name='forms_basic'),
    
        # --- Maps ---
        path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
        path('maps/vector/', views.maps_vector, name='maps_vector'),
    
        # --- Pages / Auth ---
        path('page/login/', views.page_login, name='page_login'),
        path('page/register/', views.page_register, name='page_register'),
        path('pages/forget/', views.pages_forget, name='pages_forget'),
    
        # --- Tables ---
        path('tables/basic/', views.tables_basic, name='tables_basic'),
        path('tables/data/', views.tables_data, name='tables_data'),
    
        # --- UI Elements ---
        path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
        path('ui/badges/', views.ui_badges, name='ui_badges'),
        path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
        path('ui/cards/', views.ui_cards, name='ui_cards'),
        path('ui/grids/', views.ui_grids, name='ui_grids'),
        path('ui/modals/', views.ui_modals, name='ui_modals'),
        path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
        path('ui/switches/', views.ui_switches, name='ui_switches'),
        path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
        path('ui/typography/', views.ui_typography, name='ui_typography'),
    
        
    
        # --- Widgets ---
        path('widgets/', views.widgets, name='widgets')

]







urlpatterns = [
        path ('', views.forms_advanced, name= 'forms_advanced'),
        path('ui-badges/', ui_badges, name = 'ui_badges'),
        path('ui-tabs/', ui_tabs, name='ui_tabs'),
        path('ui-cards/', ui_cards, name = 'ui_cards'),
        path('ui-alerts/', ui_alerts, name = 'ui_alerts'),
        path('ui-progressbar/', ui_progressbar  ,name='ui_progressbar'),
        path('ui-modals/', ui_modals, name='ui_modals'),
        path('ui-switches/',ui_switches,name='ui_switches'),
        path('ui-grids/',ui_grids,name='ui_grids'),
        path('ui_typography/',ui_typography,name='ui_typography'),
        path('tables-basic/',tables_basic,name='tables_basic'),
        path('tables_data/',tables_data,name='tables_data'),
        path('forms_basic/',forms_basic,name='forms_basic'),
        path('forms_advanced/',forms_advanced,name='forms_advanced'),
        path('font_fontawesome/',font_fontawesome, name ='font_fontawesome'),
        path('font_themify/',font_themify, name ='font_themify'),
        path('charts_chartjs/',charts_chartjs, name ='charts_chartjs'),
        path('charts_flot/',charts_flot, name ='charts_flot'),
        path('charts_peity/',charts_peity, name ='charts_peity'),
        path('maps_gmap/',maps_gmap, name ='maps_gmap'),
        path('maps_vector/',maps_vector, name ='maps_vector'),
        path('page_login/',page_login, name ='page_login'),
        path('page_register/',page_register, name ='page_register'),
        path('pages_forget/',pages_forget, name ='pages_forget'),
    
        # --- Charts ---
        path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
        path('charts/flot/', views.charts_flot, name='charts_flot'),
        path('charts/peity/', views.charts_peity, name='charts_peity'),
    
        # --- Fonts ---
        path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
        path('font/themify/', views.font_themify, name='font_themify'),
    
        # --- Forms ---
        path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
        path('forms/basic/', views.forms_basic, name='forms_basic'),
    
        # --- Maps ---
        path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
        path('maps/vector/', views.maps_vector, name='maps_vector'),
    
        # --- Pages / Auth ---
        path('page/login/', views.page_login, name='page_login'),
        path('page/register/', views.page_register, name='page_register'),
        path('pages/forget/', views.pages_forget, name='pages_forget'),
    
        # --- Tables ---
        path('tables/basic/', views.tables_basic, name='tables_basic'),
        path('tables/data/', views.tables_data, name='tables_data'),
    
        # --- UI Elements ---
        path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
        path('ui/badges/', views.ui_badges, name='ui_badges'),
        path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
        path('ui/cards/', views.ui_cards, name='ui_cards'),
        path('ui/grids/', views.ui_grids, name='ui_grids'),
        path('ui/modals/', views.ui_modals, name='ui_modals'),
        path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
        path('ui/switches/', views.ui_switches, name='ui_switches'),
        path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
        path('ui/typography/', views.ui_typography, name='ui_typography'),
    
        
    
        # --- Widgets ---
        path('widgets/', views.widgets, name='widgets')

]


urlpatterns = [
        path('', views.forms_basic, name='forms_basic'),
        path('ui-badges/', ui_badges, name='ui_badges'),
        path('ui-tabs/', ui_tabs, name='ui_tabs'),
        path('ui-cards/', ui_cards, name='ui_cards'),
        path('ui-alerts/', ui_alerts, name='ui_alerts'),
        path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
        path('ui-modals/', ui_modals, name='ui_modals'),
        path('ui-switches/', ui_switches, name='ui_switches'),
        path('ui-grids/', ui_grids, name='ui_grids'),
        path('ui_typography/', ui_typography, name='ui_typography'),
        path('tables-basic/', tables_basic, name='tables_basic'),
        path('tables_data/', tables_data, name='tables_data'),
        path('forms_basic/', forms_basic, name='forms_basic'),
        path('forms_advanced/', forms_advanced, name='forms_advanced'),
        path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
        path('font_themify/', font_themify, name='font_themify'),
        path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
        path('charts_flot/', charts_flot, name='charts_flot'),
        path('charts_peity/', charts_peity, name='charts_peity'),
        path('maps_gmap/', maps_gmap, name='maps_gmap'),
        path('maps_vector/', maps_vector, name='maps_vector'),
        path('page_login/', page_login, name='page_login'),
        path('page_register/', page_register, name='page_register'),
        path('pages_forget/', pages_forget, name='pages_forget'),

        # --- Charts ---
        path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
        path('charts/flot/', views.charts_flot, name='charts_flot'),
        path('charts/peity/', views.charts_peity, name='charts_peity'),

        # --- Fonts ---
        path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
        path('font/themify/', views.font_themify, name='font_themify'),

        # --- Forms ---
        path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
        path('forms/basic/', views.forms_basic, name='forms_basic'),

        # --- Maps ---
        path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
        path('maps/vector/', views.maps_vector, name='maps_vector'),

        # --- Pages / Auth ---
        path('page/login/', views.page_login, name='page_login'),
        path('page/register/', views.page_register, name='page_register'),
        path('pages/forget/', views.pages_forget, name='pages_forget'),

        # --- Tables ---
        path('tables/basic/', views.tables_basic, name='tables_basic'),
        path('tables/data/', views.tables_data, name='tables_data'),

        # --- UI Elements ---
        path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
        path('ui/badges/', views.ui_badges, name='ui_badges'),
        path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
        path('ui/cards/', views.ui_cards, name='ui_cards'),
        path('ui/grids/', views.ui_grids, name='ui_grids'),
        path('ui/modals/', views.ui_modals, name='ui_modals'),
        path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
        path('ui/switches/', views.ui_switches, name='ui_switches'),
        path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
        path('ui/typography/', views.ui_typography, name='ui_typography'),

        # --- Widgets ---
        path('widgets/', views.widgets, name='widgets'),
]

urlpatterns = [
    path('', views.maps_gmap, name='maps_gmap'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 10. maps-vector
urlpatterns = [
    path('', views.maps_vector, name='maps_vector'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 11. page-login
urlpatterns = [
    path('', views.page_login, name='page_login'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 12. page-register
urlpatterns = [
    path('', views.page_register, name='page_register'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 13. pages-forget
urlpatterns = [
    path('', views.pages_forget, name='pages_forget'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 14. tables-basic
urlpatterns = [
    path('', views.tables_basic, name='tables_basic'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 15. tables-data
urlpatterns = [
    path('', views.tables_data, name='tables_data'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 16. ui-alerts
urlpatterns = [
    path('', views.ui_alerts, name='ui_alerts'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 17. ui-badges
urlpatterns = [
    path('', views.ui_badges, name='ui_badges'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 18. ui-buttons
urlpatterns = [
    path('', views.ui_buttons, name='ui_buttons'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 19. ui-cards
urlpatterns = [
    path('', views.ui_cards, name='ui_cards'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 20. ui-grids
urlpatterns = [
    path('', views.ui_grids, name='ui_grids'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 21. ui-modals
urlpatterns = [
    path('', views.ui_modals, name='ui_modals'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

# 22. widgets
urlpatterns = [
    path('', views.widgets, name='widgets'),
    path('ui-badges/', ui_badges, name='ui_badges'),
    path('ui-tabs/', ui_tabs, name='ui_tabs'),
    path('ui-cards/', ui_cards, name='ui_cards'),
    path('ui-alerts/', ui_alerts, name='ui_alerts'),
    path('ui-progressbar/', ui_progressbar, name='ui_progressbar'),
    path('ui-modals/', ui_modals, name='ui_modals'),
    path('ui-switches/', ui_switches, name='ui_switches'),
    path('ui-grids/', ui_grids, name='ui_grids'),
    path('ui_typography/', ui_typography, name='ui_typography'),
    path('tables-basic/', tables_basic, name='tables_basic'),
    path('tables_data/', tables_data, name='tables_data'),
    path('forms_basic/', forms_basic, name='forms_basic'),
    path('forms_advanced/', forms_advanced, name='forms_advanced'),
    path('font_fontawesome/', font_fontawesome, name='font_fontawesome'),
    path('font_themify/', font_themify, name='font_themify'),
    path('charts_chartjs/', charts_chartjs, name='charts_chartjs'),
    path('charts_flot/', charts_flot, name='charts_flot'),
    path('charts_peity/', charts_peity, name='charts_peity'),
    path('maps_gmap/', maps_gmap, name='maps_gmap'),
    path('maps_vector/', maps_vector, name='maps_vector'),
    path('page_login/', page_login, name='page_login'),
    path('page_register/', page_register, name='page_register'),
    path('pages_forget/', pages_forget, name='pages_forget'),

    # --- Charts ---
    path('charts/chartjs/', views.charts_chartjs, name='charts_chartjs'),
    path('charts/flot/', views.charts_flot, name='charts_flot'),
    path('charts/peity/', views.charts_peity, name='charts_peity'),

    # --- Fonts ---
    path('font/fontawesome/', views.font_fontawesome, name='font_fontawesome'),
    path('font/themify/', views.font_themify, name='font_themify'),

    # --- Forms ---
    path('forms/advanced/', views.forms_advanced, name='forms_advanced'),
    path('forms/basic/', views.forms_basic, name='forms_basic'),

    # --- Maps ---
    path('maps/gmap/', views.maps_gmap, name='maps_gmap'),
    path('maps/vector/', views.maps_vector, name='maps_vector'),

    # --- Pages / Auth ---
    path('page/login/', views.page_login, name='page_login'),
    path('page/register/', views.page_register, name='page_register'),
    path('pages/forget/', views.pages_forget, name='pages_forget'),

    # --- Tables ---
    path('tables/basic/', views.tables_basic, name='tables_basic'),
    path('tables/data/', views.tables_data, name='tables_data'),

    # --- UI Elements ---
    path('ui/alerts/', views.ui_alerts, name='ui_alerts'),
    path('ui/badges/', views.ui_badges, name='ui_badges'),
    path('ui/buttons/', views.ui_buttons, name='ui_buttons'),
    path('ui/cards/', views.ui_cards, name='ui_cards'),
    path('ui/grids/', views.ui_grids, name='ui_grids'),
    path('ui/modals/', views.ui_modals, name='ui_modals'),
    path('ui/progressbar/', views.ui_progressbar, name='ui_progressbar'),
    path('ui/switches/', views.ui_switches, name='ui_switches'),
    path('ui/tabs/', views.ui_tabs, name='ui_tabs'),
    path('ui/typography/', views.ui_typography, name='ui_typography'),

    # --- Widgets ---
    path('widgets/', views.widgets, name='widgets'),
]

