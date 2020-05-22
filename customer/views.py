from django.shortcuts import render, redirect
from customer.form import CustomerForm, FixedProductForm, YardProductForm,\
    PaymentForm
from customer.models import Customer, FixedProduct, YardProduct
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def findcustomer(request):
    form=Customer.objects.all()
    if request.method=="POST":
        data=int(request.POST.get("field"))
        c1=Customer.objects.get(id=data)
        return redirect("showcustomer",c1.id)
    else:
        query = request.GET.get('name')
        if query:
            # query example
            form = Customer.objects.filter(name__icontains=query)
        else:
            form = []
    return render(request,"findcustomer.html",{'form':form})
@login_required(login_url='login')
def showcustomer(request,c1):
    customer=Customer.objects.get(id=c1)
    fform=FixedProductForm()
    yform=YardProductForm()
    return render(request, "showcustomer.html",{'customer':customer,'fform':fform,'yform':yform} )
@login_required(login_url='login')
def purchasedetails(request,c1):
    customer1=Customer.objects.get(id=c1)
    fproduct=FixedProduct.objects.filter(customer=customer1).order_by('-time')
    yproduct=YardProduct.objects.filter(customer=customer1).order_by('-time')
    return render(request, "purchasedetails.html",{'fproduct':fproduct,'yproduct':yproduct} )  
@login_required(login_url='login')
def addcustomer(request):  
    if request.method == "POST":  
        customer = CustomerForm(request.POST)  
        if customer.is_valid():  
            try: 
                customer.save()   
                return redirect('home')  
            except:  
                pass  
    else:  
        customer = CustomerForm()  
    return render(request,'addcustomer.html',{'customer':customer})  

@login_required(login_url='login')
def addfixedproduct(request,cid):
    if request.method=="POST":
        fixedproduct= FixedProductForm(request.POST)
        if fixedproduct.is_valid():
            f=fixedproduct.save()
            customer=Customer.objects.get(id=cid)
            f.customer=customer
            f.save()
            due=customer.total_due
            due1=due+int(request.POST.get('price'))
            customer.total_due=due1
            customer.save()
            return redirect("showcustomer",customer.id)
    else:
        fixedproduct= FixedProductForm()
    return render(request, "addfixedproduct.html",{'fixedproduct':fixedproduct})
@login_required(login_url='login')
def addyardproduct(request,cid):
    if request.method=="POST":
        yardproduct=YardProductForm(request.POST)
        if yardproduct.is_valid():
            customer=Customer.objects.get(id=cid)
            due=customer.total_due
            data = request.POST.copy()
            yard=int(data.get('yard'))
            gira=int(data.get('gira'))
            price=int(data.get('per_yard_price'))
            tprice=(yard+(gira/16))*price
            y=yardproduct.save()
            due1=due+tprice
            customer.total_due=due1
            customer.save()
            y.customer=customer
            y.save()
            yobj=YardProduct.objects.get(id=y.id)
            yobj.total_price=tprice
            yobj.save()
            return redirect("showcustomer",customer.id)
    else:
        yardproduct=YardProductForm()
    return render(request, "addyardproduct.html",{'yardproduct':yardproduct})
@login_required(login_url='login')
def payment(request,cid):
    if request.method=="POST":
        payform=PaymentForm(request.POST)
        if payform.is_valid():
            customer=Customer.objects.get(id=cid)
            due=customer.total_due
            due=due-int(request.POST.get("pay"))
            customer.total_due=due
            customer.save()
            payform.save() 
            return redirect("showcustomer", customer.id)
    else:
        payform=PaymentForm()
    return render(request,"payment.html",{'payform':payform})
    
  
