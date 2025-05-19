from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'shinehub/home.html')

def home(request):
    products = [
        {'name': 'ডেক', 'image': 'shinehub/images/dek.jpg'},
        {'name': 'কোরাই', 'image': 'shinehub/images/korai.jpg'},
        {'name': 'চেয়ার', 'image': 'shinehub/images/chair.jpg'},
        {'name': 'সামিয়ানা', 'image': 'shinehub/images/samiana.jpg'},
        {'name': 'ডাব্বু', 'image': 'shinehub/images/dabbu.jpg'},
        {'name': 'ড্রাম', 'image': 'shinehub/images/dram.jpg'},
        {'name': 'স্ট্যান্ড', 'image': 'shinehub/images/stand.jpg'},
        {'name': 'টেপ', 'image': 'shinehub/images/tap.jpg'},
        {'name': 'সাইড পরদা', 'image': 'shinehub/images/side_porda.jpg'},
        {'name': 'টেবিল', 'image': 'shinehub/images/table.jpg'},
        {'name': 'লাইটিং', 'image': 'shinehub/images/lighting.jpg'},
        {'name': 'টেবিল ক্লথস', 'image': 'shinehub/images/table_cloths.jpg'},
        {'name': 'প্লেট', 'image': 'shinehub/images/plate.jpg'},
        {'name': 'গ্লাস', 'image': 'shinehub/images/glass.jpg'},
        {'name': 'গাবলা', 'image': 'shinehub/images/gabla.jpg'},
        {'name': 'কারি গাবলা', 'image': 'shinehub/images/kari_gabla.jpg'},
        {'name': 'হামান', 'image': 'shinehub/images/haman.jpg'},
        {'name': 'হাতল', 'image': 'shinehub/images/hatol.jpg'},
        {'name': 'সুসমেন', 'image': 'shinehub/images/susmen.jpg'},
        {'name': 'ঝালট', 'image': 'shinehub/images/jhalot.jpg'},
        {'name': 'প্যান্ডেল', 'image': 'shinehub/images/pandel.jpg'},
    ]
    return render(request, 'shinehub/home.html', {'products': products})
