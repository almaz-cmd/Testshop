from django.http import HttpResponse
from .models import Product
import pandas as pd
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail
from django.http import JsonResponse


def send_notification(request):
    subject = 'Notification Subject'
    message = 'Notification Message'
    from_email = 'from@example.com'
    to_email = 'to@example.com'
    send_mail(subject, message, from_email, [to_email])
    return JsonResponse({'message': 'Notification sent successfully.'})


@cache_page(60 * 15, cache='products_cache')
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').prefetch_related('tags').all()
        serialized_products = []
        for product in products:
            serialized_product = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'category_name': product.category.name,
                'price': float(product.price),
                'created_at': product.created_at.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'tags': [tag.name for tag in product.tags.all()]
            }
            serialized_products.append(serialized_product)

        return JsonResponse(serialized_products, safe=False)

    return JsonResponse({'error': 'Invalid request.'}, status=400)


def export_products(request):
    products = Product.objects.all()
    data = {
        'Name': [product.name for product in products],
        'Description': [product.description for product in products],
    }
    df = pd.DataFrame(data)
    df.to_excel('products.xlsx', index=False)

    with open('products.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=products.xlsx'
        return response

