from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.



def index(request):
    return render(request,'index.html')




User = get_user_model()

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')

        # Basic validations
        if not all([username, email, password, confirm_password, first_name, last_name, phone_number]):
            messages.error(request, "Please fill in all fields.")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create user using your custom manager
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('register')

    return render(request, 'login.html')




def fpassword(request):
    return render(request,'fpassword.html')

def logout(request):
    return render(request,'logout.html')



def login(request):
    return render(request,'login.html')




