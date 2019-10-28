from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()

    pl = []  # phones_list
    for device in phones:
        pl.append({
            'name': device.name,
            'price': round(device.price),
            'image': device.image,
            'slug': device.slug
        }
        )

    if request.GET.get('sort'):
        s = request.GET.get('sort')  # sort
        if s == 'name':
            pl.sort(key=lambda val: val['name'])
        elif s == 'min_price':
            pl.sort(key=lambda val: val['price'])
        elif s == 'max_price':
            pl.sort(key=lambda val: val['price'], reverse=True)
        else:
            pass

    context = {
        'pl': pl,
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    device = Phone.objects.get(slug=slug)

    rd = device.release_date.strftime('%d.%m.%Y')  # release date

    if device.lte_exists:
        lte = 'есть'
    else:
        lte = 'отсутствует'

    info = {
        'name': device.name,
        'price': round(device.price),
        'image': device.image,
        'rd': rd,
        'lte': lte
    }

    context = {
        'phone': info
    }

    return render(request, template, context)
