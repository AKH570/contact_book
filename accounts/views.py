from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#for user activation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def Registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        #print(form)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username=email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            #will not use phone num in create user as this func is not containing this parameter in model form
            user.phone_number = phone_number  #thats why we insert this code
            user.save()
            #user activation code:
            current_site = get_current_site(request) #return corrent site domain and port
            mail_subject = 'Activate your account'
            message = render_to_string('acct_verification_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),

            })
            to_email= form.cleaned_data.get('email')
            send_email = EmailMessage(
                mail_subject,message,to=[to_email]
            )
            send_email.send()
            messages.success(request,'An activation link is sent to your gmail account')
            return redirect('registration')
    else:   
        form = RegistrationForm()
    return render(request,'registration.html',{'form':form})


def Signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect('allcont')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'signin.html')

@login_required
def Signout(request):
    logout(request)
    messages.success(request,'You are now logged out')
    return redirect ('login')

def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
        print(f'uid is:{uid} user name is:{user}')
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        #user.is_staff= True
        user.save()
        messages.success(request,'Congratulations! Your account has been activated')
        return redirect('login')
    else:
        messages.error(request,'invalid user')
        return redirect('registration')

def ForgetPassword(request):
    if request.method=='POST':
        email = request.POST['email']
        if Account.objects.filter(email=email):
            user = Account.objects.get(email__exact=email)
            #user password reset link
            current_site = get_current_site(request) #return corrent site domain and port
            mail_subject = 'Here your password reset link'
            message = render_to_string('reset_password_link.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),

            })
            to_email= email
            send_email = EmailMessage(
                mail_subject,message,to=[to_email]
            )
            send_email.send()
            messages.success(request,'An activation link is sent to your gmail account')
            return redirect('login')
        else:
            messages.error(request,'User not exist')
            return redirect('forgetpassword')
    return render(request,'forgetpassword.html')

#after click the link url:
def CheckPasswordReset(request,uidb64,token):
    try:
        uid= urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
        print(f'uid{uid} and user {user}')
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid']=uid
        return redirect('resetpassword')
    
    else:
        messages.error(request,'Invalid user link')
        return redirect('forgetpassword')

def ResetPassword(request):
    if request.method=='POST':
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password==confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Password reset successfully done!')
            return redirect('login')
        else:
            messages.error(request,'Password didnot match')
            return redirect('resetpassword')
    else:
        return render(request,'resetpassword.html')
        