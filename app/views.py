from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate


def log(request):
	return render(request, 'log.html')

#**********Login**********

def login(request):
    client = designation.objects.get(designation="client")
    staff = designation.objects.get(designation="staff")
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'owner_dashboard')

        elif register.objects.filter(username=request.POST['username'], password=request.POST['password'],designation=client.id).exists():              
                member=register.objects.get(username=request.POST['username'], password=request.POST['password'])
                request.session['c_id'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['c_id'] = member.id 
                mem=register.objects.filter(id= member.id)  
                return render(request,'index.html',{'mem':mem})

        elif register.objects.filter(username=request.POST['username'], password=request.POST['password'],designation=staff.id).exists():                
                member=register.objects.get(username=request.POST['username'], password=request.POST['password'])
                request.session['s_id'] = member.designation_id
                request.session['usernamets1'] = member.username
                request.session['s_id'] = member.id 
                mem1=register.objects.filter(id= member.id)                
                # return render(request,'committee_viewworkorder.html',{'mem1':mem1})
                return redirect('committee_viewworkorder')
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'log.html', context)
    return render(request,'log.html')


def reg(request):
	return render(request, 'reg.html')
#**********Registration**********

def registration(request):
    if request.method == 'POST':
        reg = register()
        reg.firstname = request.POST['first_name']
        reg.lastname = request.POST['last_name']
        reg.username = request.POST['username']
        reg.password = request.POST['password']
        reg.cpassword = request.POST['cpassword']
        reg.email = request.POST['email']
        reg.save()
        msg_success = "Registered successfully"
        return render(request, 'reg.html', {'msg_success': msg_success})
    return render(request,'reg.html')



def pwd(request):
	return render(request, 'pwd.html')	


def index(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'index.html',{'mem':mem})
    else:
        return redirect('/')
						
def about(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'about.html',{'mem':mem})
    else:
        return redirect('/')

def services(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'services.html',{'mem':mem})
    else:
        return redirect('/')

def portfolio(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'portfolio.html',{'mem':mem})
    else:
        return redirect('/')

def request(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'request.html',{'mem':mem})
    else:
        return redirect('/')

def contact(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'contact.html',{'mem':mem})
    else:
        return redirect('/')

def addreq(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'addreq.html',{'mem':mem})
    else:
        return redirect('/')

def reqsave(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        if request.method == 'POST':
            s1 = request.POST['name']
            s2 = request.POST['dtime']
            s3 = request.POST['email']
            s4 = request.POST['phone']
            s5 = request.POST['detials']
            s6 = request.POST['location']
            s7 = request.POST['check']
            s8 = request.POST['cdate']
            s9 = request.POST['urgency']
            print(s1,s4)
            print(s9,s5)
            ab = addrequest(name = s1,email = s3,Date_Time = s2,phone = s4,
                req_details = s5,location = s6,category = s7,completion_date = s8,urgency = s9)
            ab.save()
            print(s7)
            return render(request,'request.html')
        return render(request,'addreq.html',{'mem':mem})
    else:
        return redirect('/')

def sort(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'sort.html',{'mem':mem})
    else:
        return redirect('/')

def show(request):
    if 'c_id' in request.session:
        if request.session.has_key('c_id'):
            c_id = request.session['c_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=c_id)
        return render(request,'show.html',{'mem':mem})
    else:
        return redirect('/')

def staff(request):
	return render(request, 'tempowner/staff.html')     

#-----------------Owner Module--------------------

def owner_dashboard(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        mem = register.objects.filter(id=SAdm_id)
        return render(request,'owner_dashboard.html',{'mem':mem})
    else:
        return redirect('/')

def owner_addperson(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            a1 = request.POST['name']
            a2 = request.POST['email']
            a3 = request.POST['phone']
            a4 = request.POST['address']
            add = addperson( name = a1,email = a2,phone = a3,address = a4)
            add.save()
        return render(request,'owner_addperson.html',{'owner':owner})
    else:
        return redirect('/')

def owner_allotworkorder(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        var = addrequest.objects.all().order_by('-id')
        staff = designation.objects.get(designation="staff")
        mem = register.objects.filter(designation=staff)
        if request.method == 'POST':
            g1 = request.POST['name']
            g2 = request.POST['work']
            g3 = request.POST['start']
            g4 = request.POST['end']
            print(g1,g3)
            work = givework( user_id = g1,work = g2,startdate = g3,enddate = g4)
            work.save()
            m="Give work Successfully"
        return render(request,'owner_allotworkorder.html',{'var':var,'mem':mem,'owner':owner})
    else:
        return redirect('/')


def owner_addvendors(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        if request.method == 'POST':
            v1 = request.POST['name']
            v2 = request.POST['email']
            v3 = request.POST['phone']
            v4 = request.POST['product']
            v5 = request.POST['address']
            add = addvendors( name = v1,email = v2,phone = v3, product = v4,address = v5)
            add.save()
        return render(request,'owner_addvendors.html',{'owner':owner})
    else:
        return redirect('/')

def owner_purchaseorder(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        var = payment.objects.all().order_by('-id')
        return render(request,'owner_purchaseorder.html',{'var':var,'owner':owner})
    else:
        return redirect('/')


def owner_vendorsnewpayment(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        mem = addvendors.objects.distinct()
        if request.method == 'POST':
            p1 = request.POST['name']
            p2 = request.POST['date']
            p3 = request.POST['product']
            p4 = request.POST['quantity']
            p5 = request.POST['acntno']
            p6 = request.POST['paymod']
            p7 = request.POST['amount']
            pay = payment( name = p1,date = p2, product = p3,quantity = p4,
                    accountno = p5,paymethod = p6, amount = p7)
            pay .save()
        return render(request,'owner_vendorsnewpayment.html',{'mem':mem,'owner':owner})
    else:
        return redirect('/')



def owner_salesorder(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        var = sales.objects.all().order_by('-id')
        return render(request,'owner_salesorder.html',{'var':var,'owner':owner})
    else:
        return redirect('/')

def owner_reports(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        owner = register.objects.filter(id=SAdm_id)
        work = workstatus.objects.all().order_by('-id')
        stock = stockdetails.objects.all().order_by('-id')
        pack = packing.objects.all().order_by('-id')
        return render(request,'owner_reports.html',{'work':work,'stock':stock,'pack':pack,'owner':owner})
    else:
        return redirect('/')

#-----------------Maintenance Committee--------------------
def committee_viewworkorder(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = givework.objects.filter(user_id = s_id).order_by('-id')
        return render(request,'committee_viewworkorder.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def committe_acceptwork(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        al = givework.objects.filter(id=id).update(status ='Approved')     
        return redirect('committee_viewworkorder')
    else:
        return redirect('/')

def committe_rejectwork(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        al = givework.objects.filter(id=id).update(status ='Rejected')     
        return redirect('committee_viewworkorder')
    else:
        return redirect('/')

def committee_stockdetails(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = stockdetails.objects.all().order_by('-id')
        return render(request,'committee_stockdetails.html',{'var':var,'mem1':mem1})
    else:
        return redirect('/')

def committee_updatestockdetails(request,id):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = stockdetails.objects.filter(id=id)
        if request.method == 'POST':
            s1 = stockdetails.objects.get(id=id)
            s1.product= request.POST.get('product')
            s1.quantity = request.POST.get('quantity')
            s1.save()
        return render(request,'committee_updatestockdetails.html',{'var':var,'mem1':mem1})
    else:
        return redirect('/')

def committee_updateworkstatus(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        if request.method == 'POST':
            w1 = request.POST['date']
            w2 = request.POST['status']
            work = workstatus( date = w1,status = w2,user_id = s_id)
            work.save()
        return render(request,'committee_updateworkstatus.html',{'mem1':mem1})
    else:
        return redirect('/')

def committee_packingdetails(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        var = packing.objects.all().order_by('-id')
        return render(request,'committee_packingdetails.html',{'mem1':mem1,'var':var})
    else:
        return redirect('/')

def committee_repairingdetails(request):
    if 's_id' in request.session:
        if request.session.has_key('s_id'):
            s_id = request.session['s_id']
        else:
            return redirect('/')
        mem1 = register.objects.filter(id=s_id)
        return render(request,'committee_repairingdetails.html',{'mem1':mem1})
    else:
        return redirect('/')