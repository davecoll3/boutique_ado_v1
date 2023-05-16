from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Product
from profiles.models import UserProfile


def wishlist(request, product_id):
    """ wishlist page """

    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, product_id=product_id)
    wishlist_exists = Wishlist.objects.filter(user=user, product=product).exists()

    context = {
        'user': user,
        'product': product,
        'wishlist_exists': True,
    }
    return render(request, 'wishlist/wishlist_list.html', context)
