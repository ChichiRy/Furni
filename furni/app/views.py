from django.shortcuts import render

# Create your views here.


def home(request):
    context = {'navbar': 'index'}
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html', {'navbar': 'about'})


def blog(request):
    context = {'navbar': 'blog'}
    return render(request, 'pages/blog.html', context)


def cart(request):
    return render(request, 'pages/cart.html', {'navbar': 'cart'})


def checkout(request):
    context = {'navbar': 'checkout'}
    return render(request, 'pages/checkout.html', context)


def contact(request):
    return render(request, 'pages/contact.html', {'navbar': 'contact'})


def index(request):
    context = {'navbar': 'index'}
    return render(request, 'pages/index.html', context)


def services(request):
    return render(request, 'pages/services.html', {'navbar': 'services'})


def shop(request):
    context = {'navbar': 'shop'}
    return render(request, 'pages/shop.html', context)


def thankyou(request):
    return render(request, 'pages/thankyou.html', {'navbar': 'thankyou'})
