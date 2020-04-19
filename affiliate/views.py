from django.shortcuts import render
from .models import Products


# Create your views here.
def home(request):
    pro1 = Products()
    pro1.name = 'Nautilus Treadmill Series'
    pro1.des = 'Bluetooth connectivity, syncs with the Nautilus Trainer 2 App and other apps for fitness tracking'
    pro1.price = 1.908
    pro1.link = 'https://amzn.to/2Vh9c74'
    pro1.img = 'affiliate/images/t0.jpg'

    pro2 = Products()
    pro2.name = 'Nautilus Treadmill Series'
    pro2.des = 'Bluetooth connectivity, syncs with the Nautilus Trainer 2 App and other apps for fitness tracking'
    pro2.price = 800
    pro2.link = 'https://amzn.to/2Vh9c74'
    pro2.img = 'affiliate/images/t1.jpg'

    pro3 = Products()
    pro3.name = 'Nautilus Treadmill Series'
    pro3.des = 'Bluetooth connectivity, syncs with the Nautilus Trainer 2 App and other apps for fitness tracking'
    pro3.price = 850
    pro3.link = 'https://amzn.to/2Vh9c74'
    pro3.img = 'affiliate/images/t1.jpg'

    pros = {pro1,pro2,pro3}

    return render(request, 'affiliate/home.html', {'pro': pros})


def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'
    return {'BASE_URL': scheme + request.get_host(), }
