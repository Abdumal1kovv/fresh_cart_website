from orders.models import Category, Cart


def access_categories(request):
    """
      The context processor must return a dictionary.
    """
    categories = Category.objects.all()
    return {'categories': categories}


# def access_cart(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     return {'cart': cart}
