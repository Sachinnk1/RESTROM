import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Customers,Chef,Booking,Menu1,CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from django.core.exceptions import ValidationError
from datetime import date

@login_required
def index(request):
    x=Menu1.objects.all()
    return render(request,'index.html',{'data':x})


def about(request):
    return render(request,'about.html')


def book(request):
    return render(request,'book.html')


def menu(request):
    return render(request,'menu.html')


def admin_home(request):
    return render(request,'admin_home.html')

@login_required
def chef_home(request):
    return render(request,'chef_home.html')

@login_required
def custom_home(request):
    return render(request,'custom_home.html')


def home(request):
    return render(request,'home.html')


def login_page(request):
    if request.method=='POST':
        u=request.POST['uname']
        psw=request.POST['pass']
        user=authenticate(request,username=u,password=psw)

        if user is not None and user.is_superuser==1:
            return redirect(admin_home)
        elif user is not None and  user.usertype=="customer":
            login(request,user)
            request.session['custm_id']=user.id
            return redirect(index)
        
        elif user is not None and user.usertype=="chef":
            login(request,user)
            request.session['chef_id']=user.id
            return redirect(chef_home)
        
        elif u=='' and psw=='':
            return HttpResponse("<script>alert('Enter username and password');window.location.href='/login_page/'</script>")
        
        else:
            return HttpResponse("<script>alert('Enter valid Username and Password');window.location.href='/login_page/'</script>")

    else:
        return render(request,'login_page.html')
    

def lgout(request):
    logout(request)
    return redirect(home)


def customer_reg(request):
    if request.method=='POST':
        n=request.POST['name']
        ph=request.POST['phoneno']
        a=request.POST['add']
        em=request.POST['email']
        un=request.POST['uname']
        p=request.POST['pass']
        x=User.objects.create_user(username=un,password=p,email=em,usertype="customer",is_active=True)
        y=Customers.objects.create(Name=n,Phone=ph,Address=a,customers_id=x,Status=1)
        x.save()
        y.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location.href='/login_page/'</script>")

    else:
        return render(request,'customer_reg.html')


def view_reg_customer(request):
    data=Customers.objects.all()
    context={'data':data}
    return render(request,'registered_customer.html',context)


def chef_reg(request):
    if request.method=='POST':
        n=request.POST['name']
        pl=request.POST['place']
        c=request.POST['contact']
        em=request.POST['email']
        s=request.POST['salary']
        q=request.POST['qualification']
        ex=request.POST['experience']
        un=request.POST['uname']
        psw=request.POST['pass']
        x=User.objects.create_user(username=un,password=psw,email=em,usertype="chef",is_staff=True)
        y=Chef.objects.create(Name=n,Place=pl,Contact=c,Salary=s,Qualification=q,Experiance=ex,chef_id=x)
        x.save()
        y.save()
        return HttpResponse("<script>alert('Registered Successfully');window.location.href='/admin_home/'</script>")

    else:
        return render(request,'chef_reg.html')
    


def chef_view(request):
    data=Chef.objects.all()
    context={'data':data}
    return render(request,'chef_view.html',context)



def delete_customer(request,id):
    x=Customers.objects.get(id=id)
    x.delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/view_reg_customer/'</script>")



def custom_edit(request):
    if request.method=='GET':
        custom=request.session.get('custm_id')
        em=Customers.objects.get(customers_id_id=custom)
        user=User.objects.get(id=custom)
        # context={}
        # context['data']=em

        return render(request,'custom_edit.html',{'cust':em,'user':user})

def custom_edit1(request,uid):
    if request.method=='POST':
        custom=Customers.objects.get(id=uid)
        # user=User.objects.get(id=uid)
        custom.Name=request.POST['name']
        custom.Phone=request.POST['phoneno']
        custom.Address=request.POST['add']
        # user.email=request.POST['email']
        custom.save()
        # user.save()
        return redirect(custom_home)
    

def chef_edit1(request,uid):
    x=Chef.objects.get(id=uid)
    return render(request,'chef_edit.html',{'x':x})

def chef_update(request,uid):
    if request.method=='POST':
        n=request.POST['name']
        pl=request.POST['place']
        c=request.POST['contact']
        s=request.POST['salary']
        q=request.POST['qualification']
        ex=request.POST['experience']
    chef_id=User.objects.get(id=uid)
    chef_id.Name=n
    chef_id.Place=pl
    chef_id.Contact=c
    chef_id.Salary=s
    chef_id.Qualification=q
    chef_id.Experiance=ex
    chef_id.save()
    return redirect(chef_view)



def book_table(request):
    today_date = date.today()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        persons = request.POST.get('person')
        booking_date = request.POST.get('date')

        if not all([name, phone, email, persons, booking_date]):
            return HttpResponse("<script>alert('All fields are required!');window.history.back();</script>")

        try:
            # Fetch the user based on email or create a new one
            user, created = User.objects.get_or_create(
                email=email,
                defaults={'username': email, 'first_name': name}
            )

            # Check if booking date is valid
            if date.fromisoformat(booking_date) < today_date:
                return HttpResponse("<script>alert('Booking date cannot be in the past!');window.history.back();</script>")

            # Create a new customer record linked to the user
            customer, customer_created = Customers.objects.get_or_create(
                customers_id=user.id,
                defaults={'Name': name, 'Phone': phone}
            )

            # Create a booking
            Booking.objects.create(
                booking_id=customer,
                Name=name,
                Phone=phone,
                Email=email,
                Persons=persons,
                Date=booking_date
            )

            return HttpResponse("<script>alert('Seat booked successfully');window.location.href='/book_table/'</script>")


        except Exception as e:
            return HttpResponse(f"<script>alert('An error occurred: {str(e)}');window.history.back();</script>")

    return render(request, 'book.html', {'today_date': today_date})



def booking_list_view(request):
    x=Booking.objects.all()
    context={'data':x}
    return render(request,'booking_list_view.html',context)


def approve_booking(request, booking_id):
    # Ensure the user is authorized (e.g., admin or staff)
    # if not request.user.is_staff:
    #     return HttpResponse("<script>alert('You are not authorized to perform this action.');window.history.back();</script>")

    # Fetch the booking
    booking = get_object_or_404(Booking, id=booking_id)

    # Update the status to '1' (approved)
    booking.Status = 1
    booking.save()

    return HttpResponse("<script>alert('Booking has been approved successfully!');window.location.href='/booking_list_view/';</script>")



@login_required
def Approved_booking_view(request):
    # Fetch bookings for the logged-in user with status = 1 (approved)
    approved_bookings = Booking.objects.filter(
        booking_id__customers_id=request.user,  # Link the booking to the logged-in user
        Status=1  # Only approved bookings
    )

    return render(request, 'booking_status.html', {'approved_bookings': approved_bookings})



def delete_seat(request,id):
    x=Booking.objects.get(id=id)
    x.delete()
    return HttpResponse("<script>alert('Cancelled Successfully');window.location.href='/custom_home/'</script>")



def menu_reg1(request):
    if request.method=='POST':
        n=request.POST['name']
        p=request.POST['price']
        c=request.POST['category']
        img=request.FILES['image']
        q=request.POST['quantity']
        d=request.POST['description']
        x=Menu1.objects.create(Name=n,Price=p,Category=c,Image=img,Quantity=q,Description=d)
        x.save()
        return HttpResponse("<script>alert('Registerd successfully');window.location.href='/menu_reg1/'</script>")

    else:
        return render(request,'menu_reg1.html')



def menu_view1(request):
    x=Menu1.objects.all()
    return render(request,'menu.html',{'data':x})



def delete_menu(request,id):
    x=Menu1.objects.get(id=id)
    x.delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location.href='/admin_menu_view/'</script>")


def admin_menu_view(request):
    x=Menu1.objects.all()
    return render(request,'admin_menu_view.html',{'data':x})



def menu_edit1(request, uid):
    x = Menu1.objects.get(id=uid)
    
    if request.method == "POST":
        x.Name = request.POST['Name']
        x.Price = request.POST['Price']
        x.Category = request.POST['Category']
        
        if 'Image' in request.FILES:
            x.Image = request.FILES['Image']  # Handle image upload
            
        x.Quantity = request.POST['Quantity']
        x.Description = request.POST['Description']
        
        x.save()  # Save changes
        return redirect(admin_menu_view)  # Redirect to a menu list or a success page
    
    return render(request, 'menu_edit.html', {'data': x})


def product_view(request,id):
    x=Menu1.objects.get(id=id)
    return render(request, 'product_view.html', {'data': x})















@login_required
def add_to_cart(request, item_id):
    if request.method == 'POST':
        menu_item = get_object_or_404(Menu1, id=item_id)
        customer = get_object_or_404(Customers, customers_id=request.user)
        
        try:
            quantity = int(request.POST['quantity'])
            if quantity < 1:
                messages.error(request, "Quantity must be at least 1.")
                return redirect('product_view', item_id=item_id)  # Redirect back to the product page
            
            cart_item, created = CartItem.objects.get_or_create(
                cust_id=customer,
                menu_item=menu_item,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            messages.success(request, f"{menu_item.Name} added to your cart.")
            return redirect('cart_detail')
        except (ValueError, KeyError):
            messages.error(request, "Invalid quantity provided.")
            return redirect('product_view', item_id=item_id)
    else:
        return redirect('product_view', item_id=item_id)




@login_required
def cart_detail(request):
    # Get the logged-in customer's cart items
    customer = get_object_or_404(Customers, customers_id=request.user)
    cart_items = CartItem.objects.filter(cust_id=customer)
    
    # Calculate the total price
    total_price = sum(item.get_total_price() for item in cart_items)
    
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def remove_from_cart(request, item_id):
    # Get the customer (logged-in user)
    customer = get_object_or_404(Customers, customers_id=request.user)
    
    # Get the CartItem object to be removed
    cart_item = get_object_or_404(CartItem, id=item_id, cust_id=customer)
    
    # Delete the CartItem
    cart_item.delete()
    
    return redirect('cart_detail')


# views.py

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    customer = Customers.objects.get(customers_id=request.user)  # Get the current customer
    cart_items = CartItem.objects.filter(cust_id=customer)
    
    # Calculate total price
    total_price = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        try:
            # Create a payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(total_price * 100),  # Convert to cents
                currency='usd',
                payment_method=request.POST['payment_method_id'],
                confirm=True
            )
            # Clear cart after successful payment
            cart_items.delete()
            return render(request, 'payment_success.html', {'total_price': total_price})
        except stripe.error.CardError as e:
            return render(request, 'checkout.html', {'error': str(e), 'total_price': total_price})

    # Pass the total price and Stripe public key to the template
    return render(request, 'checkout.html', {
        'total_price': total_price,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })






# # models.py
# class Payment(models.Model):
#     customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
#     transaction_id = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)


# # Save the payment details
# Payment.objects.create(
#     customer=customer,
#     transaction_id=intent['id'],
#     amount=total_price,
#     status='Success'
# )

