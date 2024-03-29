from django.shortcuts import render
from .models import Car, Brand, Colour

def car(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    colors = Colour.objects.all()
    selected_color_id = request.GET.get('color')
    if selected_color_id:
        cars = cars.filter(colour_id=selected_color_id)
    return render(request, 'blog/index.html', {'cars': cars, 'brands': brands, 'colors': colors})

def brand(request, brand_id):
    cars = Car.objects.filter(brand_id=brand_id)
    brands = Brand.objects.all()
    ctx = {
        'cars': cars,
        'brands': brands
    }
    return render(request, 'blog/index.html', ctx)