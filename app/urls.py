from django.urls import path
from .views import car, brand

urlpatterns = [
    path('', car, name='cars'),
    path('brand/<int:brand_id>/', brand, name='bolim'),

]