from django.contrib import messages
#from pyexpat.errors import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from add_contact.models import AddContact
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from math import sqrt


def home(request):
    return render(request,'home.html')

@login_required
def newcontact(request):
    #contact=AddContact.objects.all()
    if request.method=='POST':
        name=request.POST.get('Name')
        phone1=request.POST.get('Phone1')
        phone2=request.POST.get('Phone2')
        email=request.POST.get('Email')
        pic=request.POST.get('images')
        address=request.POST.get('address')
        issues=request.POST.get('issue')
        textbox=request.POST.get('message')

        conn=AddContact(name=name,phone1=phone1,phone2=phone2,email=email,picture=pic,address=address,business_key=issues,textfield=textbox)
        conn.save()
        messages.success(request,'Contact added  successfully')
    return render(request,'addcontact.html')
    
#@login_required
def ContactList(request):
    if request.user.is_authenticated:
        allcont= AddContact.objects.all()
        paginator = Paginator(allcont,3) #pagination
        page_num = request.GET.get('page')
        paged_cont = paginator.get_page(page_num)
        return render(request,'allcontact.html',{'allcont':paged_cont})
        
    else:
        return HttpResponseRedirect(reverse('newcont'))
        

#@login_required
def EditContuct(request,pk):
    get_cont= get_object_or_404(AddContact,pk=pk)
    if request.method=='POST':
        edit_name= request.POST['Name']
        edit_phone1= request.POST['Phone1']
        edit_phone2= request.POST['Phone2']
        edit_email= request.POST['Email']
        edit_pic= request.POST['images']
        edit_addr= request.POST['address']
        edit_issue= request.POST['issue']
        edit_msg= request.POST['message']

        get_cont.name=edit_name
        get_cont.phone1=edit_phone1
        get_cont.phone2=edit_phone2
        get_cont.email=edit_email
        get_cont.picture=edit_pic
        get_cont.address=edit_addr
        get_cont.business_key=edit_issue
        get_cont.textfield=edit_msg

        get_cont.save()
        messages.success(request,'Contact updated successfully') #message is not working
        return render(request,'edit_contuct.html',{'get_cont':get_cont})
        #return redirect('editcont')
        
    else:
        get_cont= get_object_or_404(AddContact,pk=pk)
    return render(request,'edit_contuct.html',{'get_cont':get_cont})
    
def DeleteContuct(request,pk):
    get_cont= get_object_or_404(AddContact,pk=pk)
    get_cont.delete()
    return redirect('allcont')

def QuickMath(request):
        result=''
        if request.method == 'POST':
            if 'result' in request.POST:
                v1 = eval(request.POST.get('val1',0))
                v2 = eval(request.POST.get('val2',0))
                operator = request.POST.get('operator')

                if operator =='+':
                    result = v1 + v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
                elif operator =='-':
                    result= v1 - v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
                elif operator == '*':
                    result= v1*v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
                elif operator == 'm':
                    result =v1%v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
                elif operator == '%':
                    result = v1*(v2/100)
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
                elif operator == '/' and v2 is not 0:
                    result= v1/v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
            #Square Root
            elif 'sqroot' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    if value1 >= 0 :
                        result= sqrt(value1)
                        return render(request,'qmath.html',{'result':result,
                        'v1': value1
                    })
                    else:
                        messages.error(request,'Give me real number')
                        return render (request,'qmath.html')
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
             #Power
            elif 'power2' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    if value1 >= 0 :
                        result= pow(value1,2)
                        return render(request,'qmath.html',{'result':result,
                        'v1': value1
                    })
                    else:
                        messages.error(request,'Give me real number')
                        return render (request,'qmath.html')
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            #power3
            elif 'power3' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    if value1 >= 0 :
                        result= pow(value1,3)
                        return render(request,'qmath.html',{'result':result,
                        'v1': value1
                    })
                    else:
                        messages.error(request,'Give me real number')
                        return render (request,'qmath.html')
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            #mod
            elif 'mod' in request.POST:
                try:
                    value1= eval(request.POST.get('val1',0))
                    value2= eval(request.POST.get('val2',0))
                    result = value1%value2
                    return render(request,'qmath.html',{'result':result
                    })
                except:
                    return HttpResponse('asdSA')
                    #messages.error(request,'You did not give any input.')
                    #return render (request,'qmath.html')
        else:
            #if request.method=='GET':
            return render (request,'qmath.html')   
'''               
        except:
            messages.error(request,'Invalid operations')
            return HttpResponseRedirect(reverse('qmath'))


def squareRoot(request):
    #return render(request,'qmath.html')
    return HttpResponse('Here the text of the web page.')
'''        
def Result(request):
    return HttpResponseRedirect(reverse('qmath'))

            


# def Addfun(request):
#         #value=None
#         if request.method == 'POST':
#             value1 = int(request.POST.get('val1'))
#             value2 = int(request.POST.get('val2'))
#             value = value1 + value2
#         return render(request,'result.html',{'val':value})

#def Calculator(request):
#     return render(request,'calculator.html')
