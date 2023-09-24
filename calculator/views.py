from django.shortcuts import render
from math import sqrt
from django.contrib import messages


def Calculator(request):
        result=''
        if request.method == 'POST':
            operator = request.POST.get('operator')
            if 'result' in request.POST:
                v1 = eval(request.POST.get('val1',0))
                v2 = eval(request.POST.get('val2',0))
                #operator = request.POST.get('operator')

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
                elif operator == '/' and v2 != 0:
                    result= v1/v2
                    return render(request,'qmath.html',{'result':result,'v1':v1,'v2':v2,'operator':operator})
            #Square Root
            elif 'sqroot' in request.POST:
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
            elif 'power2' in request.POST:
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
            elif 'power3' in request.POST:
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
            elif 'mod' in request.POST:
                try:
                    value1= eval(request.POST.get('val1',0))
                    value2= eval(request.POST.get('val2',0))
                    #ops = request.POST.get('mod')
                    result = value1%value2
                    return render(request,'qmath.html',{'result':result,
                    'm1':value1,'m2':value2,'mod':'mod','equ':'='
                    })
                except:
                    messages.error(request,'You did not give any input.')
                    return render (request,'qmath.html')
        else:
            return render (request,'qmath.html')  