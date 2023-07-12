from django.contrib import messages
#from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from add_contact.models import AddContact
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
def home(request):
    return render(request,'home.html')

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
    

def ContactList(request):
    allcont= AddContact.objects.all()
    paginator = Paginator(allcont,3) 
    page_num = request.GET.get('page')
    paged_cont = paginator.get_page(page_num)
    return render(request,'allcontact.html',{'allcont':paged_cont})

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
        #return redirect('allcont',{'messages':messages})
        
    else:
        
        return render(request,'edit_contuct.html',{'get_cont':get_cont})
    
def DeleteContuct(request,pk):
    get_cont= get_object_or_404(AddContact,pk=pk)
    get_cont.delete()

    return redirect('allcont')