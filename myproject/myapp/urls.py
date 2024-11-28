from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('book/',views.book,name='book'),
    path('menu/',views.menu,name='menu'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('chef_home/',views.chef_home,name='chef_home'),
    path('custom_home/',views.custom_home,name='custom_home'),
    path('',views.home,name='home'),
    path('lgout/',views.lgout,name='lgout'),




    path('login_page/',views.login_page,name='login_page'),
    path('customer_reg/',views.customer_reg,name='customer_reg'),
    path('view_reg_customer/',views.view_reg_customer,name='view_reg_customer'),
    path('chef_view/',views.chef_view,name='chef_view'),
    path('chef_reg/',views.chef_reg,name='chef_reg'),

    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),
    path('custom_edit/',views.custom_edit,name='custom_edit'),
    path('custom_edit1/<int:uid>',views.custom_edit1,name='custom_edit1'),

    path('chef_edit1/<int:uid>',views.chef_edit1,name='chef_edit1'),
    path('chef_update/<int:uid>',views.chef_update,name='chef_update'),


    path('book_table/',views.book_table,name='book_table'),
    path('booking_list_view/',views.booking_list_view,name='booking_list_view'),
    path('approve_booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('menu_reg1/',views.menu_reg1,name='menu_reg1'),
    path('menu_view1/',views.menu_view1,name='menu_view1'),

    path('admin_menu_view/',views.admin_menu_view,name='admin_menu_view'),
    path('delete_menu/<int:id>',views.delete_menu,name='delete_menu'),

    path('menu_edit1/<int:uid>/',views.menu_edit1,name='menu_edit1'),





    path('product_view/<int:id>', views.product_view, name='product_view'),


    path('delete_seat/<int:id>', views.delete_seat, name='delete_seat'),


    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('Approved_booking_view/', views.Approved_booking_view, name='Approved_booking_view'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)