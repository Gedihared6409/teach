from django.shortcuts import render,redirect
from .forms import  OrderForm,CustomerForm,RepairAssetForm
from django.contrib import messages
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'users_register.html' 
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        
        user = form.save(commit=False)
        user.is_employee = True
        user.save()
        login(self.request,user)
        return redirect('login')

def homy(request):
    return render(request, 'accounts/homy.html')
@unauthenticated_user
def registerPage(request):  
        form =CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                #Added username after video because of error returning customer name if not added
                Customer.objects.create(
                    user=user,
                    name=user.username,
                    )
                messages.success(request, 'account was created for '+ username)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('repairform')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def repairassets(request):
    
    if request.method == 'POST':
        form = RepairAssetForm(request.POST)
        if form.is_valid():
            Asset = form.save()
            current_user = request.user.username

            # username = current_user.usernam
        return redirect ('welcome')
    else:
        form = RepairAssetForm
    return render(request, 'accounts/repairforms.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login' )
@admin_only
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_customers = customers.count()
    
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    

    context = {'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,
    'pending':pending}
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login' )
@allowed_users(allowed_roles=['Admin'])
def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm(initial={'customer':customer})
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def create_customer_order(request, pk):
    customerss = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm(initial={'customerss':customerss})
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
def create_teacher_order(request):
    # customerss = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login' )
@allowed_users(allowed_roles=['Admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})
def homee(request):
    

    return render(request, 'accounts/base.html')


def userPage(request):
    current_user = request.user
    pk = current_user.id
    customers = Customer.objects.get(id = pk)
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders':orders, 'total_orders':total_orders,'delivered':delivered,'pending':pending,'customers':customers,'pk':pk}
    return render(request, 'accounts/user.html' ,context)
def teacherPage(request):
    current_user = request.user
    pk = current_user.id
    customers = Customer.objects.get(id = pk)
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders':orders, 'total_orders':total_orders,'delivered':delivered,'pending':pending,'customers':customers}
    return render(request, 'accounts/teacher.html' ,context)

@login_required(login_url='login' )
@allowed_users(allowed_roles=['Admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id = pk_test)
    
    orders = customer.order_set.all()
    
    order_count = orders.count()


    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request, 'accounts/customer.html',context)
@login_required(login_url='login' )
@allowed_users(allowed_roles=['Admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST , instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login' )
@allowed_users(allowed_roles=['Admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':

        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles= ['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid:
            form.save()
    context = {'form':form}
    return render(request, 'accounts/acccounts_setting.html', context)

#react
#data structures
#javascript
#deep learning (tensorflow,keras,)
#machine learning ["sciket", "pandas", "numpy", "scipy", "spacy", "Ocatve", "Jupyter"]
#mobileApp: ["Flutter"]



#teacher
