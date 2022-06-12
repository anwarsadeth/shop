

from django.urls import path
from .import views
app_name='shop'
urlpatterns = [

    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='procatdetail')
]