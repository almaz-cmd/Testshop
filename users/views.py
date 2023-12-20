from django.http import JsonResponse
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.hashers import make_password
import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.shortcuts import render


@cache_page(60 * 15, cache='products_cache')  # Кэширование на 15 минут
def get_products(request):
    products = [...]

    return render(request, 'products.html', {'products': products})


def get_data():
    data = cache.get('my_data')
    if not data:
        cache.set('my_data', data, timeout=3600)  # Кэширование на час
    return data


def send_notification(request):
    subject = 'Notification Subject'
    message = 'Notification Message'
    from_email = 'from@example.com'
    to_email = 'to@example.com'
    send_mail(subject, message, from_email, [to_email])
    return JsonResponse({'message': 'Notification sent successfully.'})


def create_product(request):
    cache.delete('products_cache')

def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = make_password(data.get('password'))

        new_user = DjangoUser.objects.create(username=username, email=email, password=password)
        new_user.save()

        return JsonResponse({'message': 'User registered successfully.'})

    return JsonResponse({'error': 'Invalid request.'}, status=400)

def login_user(request):
    pass


def index():
    return None