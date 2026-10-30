
from django.urls import path
from .view_ariza import ariza, ArizaModelFoem, add_ariza
from .views_mening_arizalarim import mening_arizalarim


urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('register/', register_view, name='register'),
    path('ariza/', add_ariza,  name= 'ariza'),
    path('arz/', mening_arizalarim, name='arz')

]
