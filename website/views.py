from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addRecordForm
from .models import Record
# Create your views here.
def home(request):

    records = Record.objects.all()

    # Check to see if login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Login!")
            return redirect('home')
        else:
            messages.success(request, 'There Was An Error Login Please try against...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def log_out(request):
    logout(request)
    messages.success(request, "You have Been Logged Out!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        # Authenticate and login

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been success Register Login!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must be Logged In to View That Page...")
        return redirect("home")

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "You have been deleted success!")
        return redirect("home")
    else:
         messages.success(request, "You Must be Logged In to Do That...")
         return redirect("home")
    
def add_record(request):
    form = addRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added...")
                return redirect("home")
        return render(request, "add_record.html", {'form': form})
    else:
        messages.success(request, "Record not added")
        return redirect("home")
        
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Update")
            return redirect('home')
        return render(request, "update_record.html", {'form': form})
    else:
        messages.success(request, "You Must be Logged In...")
        return redirect('home')




    





