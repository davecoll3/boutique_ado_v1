from django.shortcuts import render, redirect, reverse, HttpResponse, get_list_or_404, get_object_or_404

from django.contrib import messages

from .models import FavouritesList, FavouritesListItem
from products.models import Product
from profiles.models import UserProfile


def favourites_list(request):
    user = get_object_or_404(UserProfile, user=request.user)
    favourites_list = FavouritesList.objects.get_or_create(user=user)
    favourites_user = favourites_list[0]
    existing_favourites = FavouritesListItem.objects.filter(favourites=favourites_user).exists()
    items = []

    if existing_favourites:
        user_favourites_list = get_list_or_404(FavouritesListItem, favourites=favourites_user)
        for product_object in user_favourites_list:
            product = get_object_or_404(Product, name=product_object)
            dates = FavouritesListItem.objects.only('added_on')
            items.append(product)
        context = {
            'favourites_list': True,
            'products': items,
            'dates': dates
        }

        return render(request, 'favourites/favourites_list.html', context)

    else:
        context = {
            'favourites_list': False
        }

        return render(request, 'favourites/favourites_list.html', context)


def remove_favourite(request, product_id):
    # Remove from favourites

    redirect_url = request.POST.get('redirect_url')

    user = get_object_or_404(UserProfile, user=request.user)
    favourites_list = FavouritesList.objects.get_or_create(user=user)
    favourites_user = favourites_list[0]

    if request.POST:
        product = Product.objects.get(pk=product_id)
        item_exists = FavouritesListItem.objects.filter(product=product).exists()
        if item_exists:
            product = FavouritesListItem.objects.get(product=product)
            product.delete()
            messages.success(request, "Product removed from wishlist")
            return redirect(redirect_url)
        else:
            messages.error(request, "Error: this item is not in your favourites list!")
            return redirect(redirect_url)
    else:
        messages.error(request, 'Error: could not remove item from favourites list!')
        return render(request, 'home/index.html')
