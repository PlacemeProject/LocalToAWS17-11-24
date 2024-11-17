from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.urls import reverse
from .models import Users
from job_seekers.models import Candidates
from django.contrib.auth import get_user_model
from django.conf import settings
import requests
# from django.contrib.auth.hashers import make_password

from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
# from .forms import CustomAuthenticationForm
from django.http import HttpResponse

def AuthPage(request):
    return redirect('auth:login')
    

def ratelimited(request, exception):
    return HttpResponse("You have exceeded the limit. Please try again later.", status=429)


def LogoutPage(request):
    try:
        logout(request)
        return redirect('job_seeker:home')
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
        

@ratelimit(key='ip', rate='5/m', method='POST', block=True)
@csrf_protect
def LoginPage(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            recaptcha_response = request.POST.get('g-recaptcha-response')
            # # Recaptcha
            # payload = {
            #     'secret': settings.RECAPTCHA_PRIVATE_KEY,
            #     'response': recaptcha_response
            # }
            # response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
            # result = response.json()

            # if not result.get('success'):
            #     messages.error(request, 'reCAPTCHA verification failed. Please try again.')
            #     return redirect('auth:login')
            # Authenticate
            if not username or not password:
                messages.error(request, "Enter the valid Username and Password.")
                return render(request,'auth:login.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
            user=authenticate(request,username=username,password=password)
            if user is not None:
                    auth_login(request,user)
                    return redirect('job_seeker:home')
            else:
                messages.error(request, "Invalid Username and Password.")
                return render(request,'auth/login.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)


    return render(request,'auth/login.html' ,{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})


@ratelimit(key='ip', rate='5/m', method='POST', block=True)
@csrf_protect
def SignupPage(request):
    try:
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            mobile_no = request.POST.get('mobile_no')
            # country = request.POST.get('country')
            # state = request.POST.get('state')
            # city = request.POST.get('city')
            recaptcha_response = request.POST.get('g-recaptcha-response')
            # # Recaptcha
            # payload = {
            #     'secret': settings.RECAPTCHA_PRIVATE_KEY,
            #     'response': recaptcha_response
            # }
            # response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
            # result = response.json()

            # if not result.get('success'):
            #     messages.error(request, 'reCAPTCHA verification failed. Please try again.')
            #     return redirect('auth:signup')

            # Validate POST data
            if full_name and email and password1 and password2 and mobile_no and len(mobile_no) == 10:
                if not Users.objects.filter(email=email).exists():
                    if not Users.objects.filter(mobile_no=mobile_no).exists():
                        try:
                            validate_email(email)
                        except ValidationError:
                            messages.error(request, "Invalid email format.")
                            return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
                        else:
                            if password1==password2:

                                try:
                                    validate_password(password1)
                                except ValidationError as e:
                                    messages.error(request, "Create a strong password.")
                                    return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
                                else:
                                    # Create a new user
                                    user = Users.objects.create_user(
                                        email=email,
                                        mobile_no=mobile_no,
                                        password=password1
                                    )

                                    # create candidate
                                    Candidates.objects.create(
                                        user=user,
                                        fullname=full_name
                                    )
                                    
                                    user=authenticate(request,username=email,password=password1)
                                    if user is not None:
                                        auth_login(request,user)  # Log the user in after registration
                                        return redirect('job_seeker:profile')
                                    else:
                                        messages.error(request, "Your account is created, you need to login here manually.")
                                        return render(request,'auth/login.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})   
                            else:
                                messages.error(request, "Password and Confirm password does not match.")
                                return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})                  

                    else:
                        messages.error(request, "Mobile number has already been used, Try new one.")
                        return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
                else:
                    messages.error(request, "Email has already been used, Try new one.")
                    return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
            else:
                messages.error(request, "Enter all required details.")
                return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})


        return render(request,'auth/signup.html',{'recaptcha_site_key': settings.RECAPTCHA_PUBLIC_KEY})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)


