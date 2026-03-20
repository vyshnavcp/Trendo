from .models import Cart, Category,SubCategory,Newsletter


def cart_count(request):
    # if user is logged in
    if request.user.is_authenticated:
        try:
            # get user's cart
            cart = Cart.objects.get(registration__authuser=request.user)
            # count cart items
            count = cart.items.count()
        except Cart.DoesNotExist:
            count = 0
    else:
        count = 0

    return {
        'cart_item_count': count
    }

def footer_categories(request):
    """
    Adds categories + newsletter status to all templates
    """
    categories = Category.objects.all()

    is_subscribed = False

    if request.user.is_authenticated:
        is_subscribed = Newsletter.objects.filter(
            email=request.user.email
        ).exists()

    return {
        'footer_categories': categories,
        'is_subscribed': is_subscribed
    }

def navbar_categories(request):
    """
    Adds categories with subcategories for navbar mega menu
    """
    categories = Category.objects.prefetch_related("subcategories").all()
    return {
        "nav_categories": categories
    }