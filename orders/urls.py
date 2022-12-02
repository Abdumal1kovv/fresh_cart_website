from django.conf.urls import handler404
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, reverse_lazy

from orders.views import (
    ResetPasswordView, RegisterView, IndexView, WishlistView, UserNotificationView, UserPaymentMethodView,
    UserSettingsView, UserAddressView, UserOrderView, CartView, ProductListView, ProductDetailView, ProductCommentView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(
        template_name='orders/auth/login.html',
        next_page=reverse_lazy('index')
    ), name='login'),
    path('logout', LogoutView.as_view(
        template_name='orders/auth/logout.html',
        next_page=reverse_lazy('index')
    ), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('reset-password', ResetPasswordView.as_view(), name='reset_password'),

    path('wishlist', WishlistView.as_view(), name='wishlist'),
    path('cart', CartView.as_view(), name='cart'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('product/comment/<str:product_slug>', ProductCommentView.as_view(), name='add_product_comment'),
    path('user/payment-method', UserPaymentMethodView.as_view(), name='user_payment_method'),
    path('user/orders', UserOrderView.as_view(), name='user_orders'),
    path('user/notification', UserNotificationView.as_view(), name='user_notification'),
    path('user/address', UserAddressView.as_view(), name='user_address'),
    path('user/settings', UserSettingsView.as_view(), name='user_settings'),
    # path('404', ErrorNotFoundView.as_view(), name='error_404'),
]

handler404 = 'orders.views.error_page'
