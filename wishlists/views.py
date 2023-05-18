from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist


@login_required
def wishlists(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlists/wishlist.html', context=context)


@login_required
def add_to_wishlist(request, product_id):
    # Get products for the user's wishlist
    product = get_object_or_404(Product, pk=product_id)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)

    if wishlist.products.filter(id=product_id).exists():
        messages.info(request, "This item is already in your wishlist!")
    else:
        # Add product to the wishlist
        wishlist.products.add(product)
        messages.info(request, "A new product was added to your wishlist")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    # Remove a product from the wishlist
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the wishlist
    wishlist.products.remove(product)
    messages.info(request, "A product was removed from your wishlist")

    return redirect(reverse('wishlists'))
