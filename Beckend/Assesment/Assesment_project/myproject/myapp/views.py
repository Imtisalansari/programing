from django.contrib import messages
from django.contrib.auth import get_user_model

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import PolicyHolder
from .utils import send_confirmation_email
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
    if request.method == "POST":
        try:
            user = User.objects.get(mobile=request.POST['mobile'])
            mobile =  request.POST['mobile']
            otp = random.randint(1001,9999) 
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"4FLqt2yEconSrjiDwMvY19AXNB308IKZpWTkehHuxf7bVdG5aOjkV09BWEUrcpAST5JOZQs2dFoYxe8D","variables_values":str(otp),"route":"otp","numbers":str(mobile)}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

            request.session['mobile']=user.mobile
            request.session['otp']=otp

            return render(request,'otp.html')

        except Exception as e:
                msg = "Mobile not found!!"
                print('*',e) 
                return render(request,'fpass.html',{'msg':msg})


    else:
        return render(request,'fpass.html')
def logout(request):
    del request.session['email']

    return redirect('login')


def login(request):
    if request.method=="POST":


        try:
            user = User.objects.get(email=request.POST['email'])

            if user.password == request.POST['password']:
                request.session['email']=user.email
                request.session['uprofile']=user.uprofile.url
                if user.usertype=="buyer":
                    return redirect('index')
                else:
                    return redirect('sindex')

                    
            else:
                msg = "Invalid Password!!!"
                return render(request,'login.html',{'msg':msg})

        except:
            msg = "Invalid Email!!!"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')





def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('login')
    holders = PolicyHolder.objects.all()
    return render(request, 'dashboard.html', {'holders': holders})

def approve_user(request, user_id):
    holder = PolicyHolder.objects.get(id=user_id)
    holder.status = 'Approved'
    holder.save()
    return redirect('dashboard')

def reject_user(request, user_id):
    holder = PolicyHolder.objects.get(id=user_id)
    holder.status = 'Rejected'
    holder.save()
    return redirect('dashboard')