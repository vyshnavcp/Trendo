from django.contrib import admin
from .models import *
from .models import Article

from unfold.admin import ModelAdmin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin import register
from django.contrib.auth.models import User
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from .models import Product, Category, SubCategory, Size


admin.site.unregister(User)

@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'posted_on')
    search_fields = ('title', 'content')
    readonly_fields = ('slug',)
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    list_display = ('name', 'category', 'slug')   
    readonly_fields = ('slug',)          # Show slug but don’t allow editing
    list_filter = ('category',)                 
    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)



@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        'name', 'brand', 'product_code', 'subcategory',
        'price', 'old_price', 'stock', 'status',
        'is_signature_collection', 'is_featured', 'is_best_seller'
    )

    list_filter = (
        'subcategory', 'status',
        'is_signature_collection', 'is_featured', 'is_best_seller'
    )

    search_fields = ('name', 'brand', 'product_code')
    prepopulated_fields = {'slug': ('name',)}
 

    readonly_fields = (
        'style_type_display',
        'material_type_display',
        'created_at',
        'updated_at'
    )

    fieldsets = (
        ('Relations', {
            'fields': ('subcategory', 'sizes')
        }),
        ('Basic Info', {
            'fields': ('name', 'brand', 'product_code', 'slug', 'description', 'additional_info')
        }),
        ('Price & Stock', {
            'fields': ('price', 'old_price', 'stock')
        }),
        ('Flags', {
            'fields': ('status', 'is_signature_collection', 'is_featured', 'is_best_seller')
        }),
        ('Images', {
            'fields': ('image1', 'image2', 'image3', 'image4', 'image5')
        }),
        ('Style & Material', {
            'fields': ('style_type_display', 'material_type_display')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def style_type_display(self, obj):
        return ", ".join(obj.style_type)
    style_type_display.short_description = "Style Types"

    def material_type_display(self, obj):
        return ", ".join(obj.material_type)
    material_type_display.short_description = "Material Types"
@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    list_display = ("code", "discount_amount", "active", "min_cart_value", "expiry_date")
    list_filter = ("active",)
    search_fields = ("code",)
@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(HomeBanner)
class HomeBannerAdmin(ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)


@admin.register(Newsletter)
class NewsletterAdmin(ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    list_filter = ('status',)


@admin.register(Registration)
class RegistrationAdmin(ModelAdmin):
    list_display = ('user_name', 'email', 'phone')
    search_fields = ('user_name', 'email')


@admin.register(TermsCondition)
class TermsConditionAdmin(ModelAdmin):
    list_display = ('updated_at',)


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(ModelAdmin):
    list_display = ('updated_at',)


@admin.register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ('question', 'created_at')
    search_fields = ('question',)


@admin.register(ProductColor)
class ProductColorAdmin(ModelAdmin):
    list_display = ('product', 'name', 'hex_code')
    search_fields = ('name',)


@admin.register(ProductVariant)
class ProductVariantAdmin(ModelAdmin):
    list_display = ('product', 'size', 'color', 'stock')
    list_filter = ('size', 'color')


@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('product', 'email', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('email', 'product__name')


@admin.register(Cart)
class CartAdmin(ModelAdmin):
    list_display = ('registration', 'subtotal_amount', 'total_amount', 'created_at')


@admin.register(CartItem)
class CartItemAdmin(ModelAdmin):
    list_display = ('cart', 'product', 'variant', 'quantity', 'price')


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        'id', 'first_name', 'total',
        'payment_method', 'payment_status',
        'is_completed', 'is_delivered', 'is_cancelled'
    )
    list_filter = (
        'payment_method', 'payment_status',
        'is_completed', 'is_delivered', 'is_cancelled'
    )
    search_fields = ('first_name', 'email', 'phone')


@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'phone', 'town', 'state')