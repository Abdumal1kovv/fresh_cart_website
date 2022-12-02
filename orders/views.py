from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView
from django_filters import FilterSet
from django_filters.views import FilterMixin

from orders.forms import CustomUserCreationForm, UserSettingsForm, CommentModelForm
from orders.models import Product, Cart


def error_page(request, error):
    render(request, '404.html', status=404)


class IndexView(TemplateView):
    template_name = 'orders/index.html'


class ResetPasswordView(TemplateView):
    template_name = 'orders/auth/reset-password.html'


class WishlistView(TemplateView):
    template_name = 'orders/products/wishlist.html'


class CartView(ListView):
    queryset = Cart.objects.all()
    template_name = 'orders/products/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).first


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'orders/products/list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.request.GET.get('slug', None)
        if slug:
            qs = qs.filter(category__slug=slug)
        return qs


class ProductDetailView(DetailView):
    queryset = Product.objects.order_by('-created_at')
    template_name = 'orders/products/detail.html'
    context_object_name = 'product'


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'orders/auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductCommentView(FormView):
    form_class = CommentModelForm
    template_name = 'orders/products/detail.html'

    def post(self, request, *args, **kwargs):
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()


        return redirect('product_detail', kwargs.get('product_slug'))


class UserNotificationView(TemplateView):
    template_name = 'orders/account/notification.html'


class UserOrderView(TemplateView):
    template_name = 'orders/account/orders.html'


class UserPaymentMethodView(TemplateView):
    template_name = 'orders/account/payment-method.html'


class UserAddressView(TemplateView):
    template_name = 'orders/account/address.html'


class UserSettingsView(FormView):
    template_name = 'orders/account/settings.html'
    form_class = UserSettingsForm
    success_url = reverse_lazy('user_settings')

    def form_valid(self, form):
        User.objects.filter(pk=self.request.user.id).update(**form.cleaned_data)
        return super().form_valid(form)
