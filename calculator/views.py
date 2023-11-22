from django.shortcuts import render
from math import sqrt,remainder,factorial,pi
from django.contrib import messages


def Calculator(request):
        result=''
        if request.method == 'POST': 
            if 'sum' in request.POST:
                try:
                    s1 = eval(request.POST.get('val1',0))
                    s2 = eval(request.POST.get('val2',0))
                    add = request.POST.get('sum')
                    list_val = [s1,s2]
                    result = sum(list_val)
                    return render(request,'qmath.html',
                        {'result':result,'s1':s1, 'add':add,'s2':s2,'equ':'=' })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            
            if 'minus' in request.POST:
                try:
                    s1 = eval(request.POST.get('val1',0))
                    s2 = eval(request.POST.get('val2',0))
                    add = request.POST.get('minus')
                    result = s1-s2
                    return render(request,'qmath.html',
                        {'result':result,'s1':s1, 'add':add,'s2':s2,'equ':'=' })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            
            if 'multiply' in request.POST:
                try:
                    s1 = eval(request.POST.get('val1',0))
                    s2 = eval(request.POST.get('val2',0))
                    add = request.POST.get('multiply')
                    result = s1*s2
                    return render(request,'qmath.html',
                        {'result':result,'s1':s1, 'add':add,'s2':s2,'equ':'=' })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')

            if 'division' in request.POST:
                try:
                    s1 = eval(request.POST.get('val1',0))
                    s2 = eval(request.POST.get('val2',0))
                    add = request.POST.get('division')
                    result = s1/s2
                    return render(request,'qmath.html',
                        {'result':result,'s1':s1, 'add':add,'s2':s2,'equ':'=' })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            #Square Root
            if 'sqroot' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    ops= request.POST.get('sqroot')
                    if value1 >= 0 :
                        result= sqrt(value1)
                        return render(request,'qmath.html',{'result':result,
                        'v1': value1, 'equ':'=','ops':ops
                    })
                    else:
                        messages.error(request,'Give me real number')
                        return render (request,'qmath.html')
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
             #Power2
            if 'power2' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    result= pow(value1,2)
                    return render(request,'qmath.html',{'result':result,
                        'v1': value1,'equ':'=',
                        'ops':'sqr of '
                    })
                    
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            #power3
            if 'power3' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    result= pow(value1,3)
                    return render(request,'qmath.html',{'result':result,
                        'v1': value1,'equ':'=',
                        'ops':'cube of '
                    })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
            # modulus
            if 'mod' in request.POST:
                try:
                    value1= eval(request.POST.get('val1',0))
                    value2= eval(request.POST.get('val2',0))
                    #ops = request.POST.get('mod')
                    result = remainder(value1,value2)
                    return render(request,'qmath.html',{'result':result,
                    'm1':value1,'m2':value2,'mod':'mod','equ':'='
                    })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')

            if 'factor' in request.POST:
                try:
                    value1=eval(request.POST.get('val1',0))
                    result= factorial(value1)
                    return render(request,'qmath.html',{'result':result,
                        'v1': value1,'equ':'=',
                        'ops':'Factorial of '
                    })
                except ValueError:
                    messages.error(request,'Wrong input value')
                    return render (request,'qmath.html')
            
            if 'pi' in request.POST:
                try:
                    #value1=eval(request.POST.get('pi',0))
                    result= 3.141592
                    return render(request,'qmath.html',{'result':result,
                        'v1': value1,'equ':'=',
                        'ops':'pi '
                    })
                except ValueError:
                    messages.error(request,'Wrong input value')
                    return render (request,'qmath.html')
        else:
            return render (request,'qmath.html')  