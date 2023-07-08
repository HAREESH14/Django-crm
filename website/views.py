from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()



    if request.method =='POST':
        username=request.POST['user_name']
        password=request.POST["password"]
        #authitcate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been loged in sucessfully")
            return redirect('home')
        else:
            messages.success(request,"there was an error try again.....")
            return redirect('home')
    else:
        return render(request,'website/home.html',{'records':records})




def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"YOU HAVE BEEN LOGOUT")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"your suceesfully register")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'website/register.html',{"form":form})
    return render(request,'website/register.html',{"form":form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'website/record.html',{"customer_record":customer_record})
    else:
        messages.success(request,"your must logged be to veiw that page...")
        return redirect('home')
    
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete=Record.objects.get(id=pk)
        delete.delete()
        messages.success(request,"REcorde has been deleted...")
        return redirect('home') 
    else:
        messages.success(request,"REcorde has been deleted...")
        return redirect('home')
    
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"your record added....")
                return redirect("home")
        return render(request,'website/add_record.html',{'form':form})
    else:
        messages.success(request,"your record added....")
        return redirect("home")
    
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'website/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



