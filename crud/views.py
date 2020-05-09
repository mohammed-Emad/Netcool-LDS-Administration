from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Computer, Alias, Filter,UserProfileInfo
import datetime
from .forms import ComputerForm, AliasForm, FilterForm ,UserForm ,UserProfileInfoForm
import os
from django.contrib.auth.models import User
import pandas as pd
import csv
import codecs
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
import difflib
import os
import socket
from django.http import JsonResponse, Http404
kDell = 'Kdell'

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from os.path import isfile, join

listno = ['SELECT name', 'type FROM sqlite_master', "WHERE type in",'ORDER BY name']
def logFile(name,email):
    old = os.path.join(settings.BASE_DIR, 'logg.log')

    csvnew = os.path.join(settings.BASE_DIR, 'logfile.csv')
    file = open(csvnew, "a" ,encoding="UTF-8")


    if isfile(csvnew):
       filetest = open(csvnew, "r" ,encoding="UTF-8")
       h = filetest.readlines()
       if len(h) == 0:
          tx = 'Time,Name,Email,Details'
          file.write(tx)
          file.write('\n')
       
    with open(old, "r" ,encoding="UTF-8") as myfile:

         text = myfile.readlines()
         for line in text:
             if not line.strip():#, 'Name ,Email'
                continue
             if line.rfind(listno[0]) != -1:
                continue
             if line.rfind(listno[1]) != -1:
                continue
             if line.rfind(listno[2]) != -1:
                continue
             if line.rfind(listno[3]) != -1:
                continue
                
             line = line.replace(",", ".")
             #line = line.replace(" ", "_")
             line = line.replace("#", ",")
             line = line.replace("Name", str(name))
             line = line.replace("Email", str(email))
             
             file.write(line)
             
    oldE = open(old, "w" ,encoding="UTF-8")
    oldE.write('')


        
def index(request):
    return render(request,'index2.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = profile_form.cleaned_data['email']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    logFile(usernamee,email)
    return render(request,'regester2.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('login_conv'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login2.html', {})

class bak():
     def __init__(self):
        self.data = None
        self.queue = None

dbak = bak()

def dets():
    LOGIN = os.environ.get('USER')
    hostname = socket.gethostname()

    DT = datetime.date.today().strftime('%Y-%m-%d')
    return LOGIN,hostname,DT
    
    
conff = {'US':'igu', 'LA':'igl', 'CA':'chs', 'AP':'igp', 'JP':'igj', 'EMEA':'EMEA'}

ese = {'igu': 'US', 'igl': 'LA', 'chs': 'CA', 'igp': 'AP', 'igj': 'JP', 'ige': 'EMEA', 'US': 'US', 'LA': 'LA', 'CA': 'CA', 'AP': 'AP', 'JP': 'JP', 'ehe': 'EMEA'}

def codeCu(name,gust):

    if gust == 'EMEA' or gust == 'emea' or gust == 'Emea':
       
       if name.rfind(".ahe.") != -1:
          GCUST="ehe"
       else:
          GCUST="ige"
    else:
        GCUST = gust
        
    return GCUST
                     
def convr(GCUST,SRVLV):
    TKACT_RM = 0
    if (str(GCUST) == "igu" and 
        str(SRVLV) == "Bronze" ):
        TKACT_RM = 70
    if (str(GCUST) == "igu" and
        str(SRVLV) == "Silver" ):
        TKACT_RM = 53
    if (str(GCUST) == "igu" and
        str(SRVLV) == "Gold" ):
        TKACT_RM = 1
    if (str(GCUST) == "chs" ):
        TKACT_RM = 135
    if (str(GCUST) == "igl" and
        str(SRVLV) == "Bronze" ):
        TKACT_RM = 115
    if (str(GCUST) == "igl" and
        str(SRVLV) == "Silver" ):
        TKACT_RM = 115
    if ( str(GCUST) == "igl" and
        str(SRVLV) == "Gold" ):
        TKACT_RM = 110
    if ( str(GCUST) == "ige" and
        str(SRVLV) == "Bronze" ):
        TKACT_RM = 252
    if (str(GCUST) == "ige" and
        str(SRVLV) == "Silver" ):
        TKACT_RM = 112
    if (str(GCUST) == "ige" and
        str(SRVLV) == "Gold" ):
        TKACT_RM = 133
    if (str(GCUST) == "igj" and
        str(SRVLV) == "Bronze" ):
        TKACT_RM = 207
    if (str(GCUST) == "igj" and
        str(SRVLV) == "Silver" ):
        TKACT_RM = 113
    if ( str(GCUST) == "igj" and
        str(SRVLV) == "Gold" ):
        TKACT_RM = 205
    if (str(GCUST) == "igp" and
        str(SRVLV) == "Bronze" ):
        TKACT_RM = 231
    if ( str(GCUST) == "igp" and
        str(SRVLV) == "Silver" ):
        TKACT_RM = 114
    if (str(GCUST) == "igp" and
        str(SRVLV) == "Gold" ):
        TKACT_RM = 228
        
    return TKACT_RM


@login_required
def login_conv(request):
    print(request.user.id)
    user=UserProfileInfo.objects.get(id=request.user.id)

    if user.position == "manager":
       print(user.position)
       return redirect('home')
    elif user.position == "normal":
       print(user.position)
       return redirect('home5')
       
    print(user.position)

    return redirect('error')



@login_required
def home(request):
    print(request.user.id)
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    print(user.position)
    computers = Computer.objects.filter(~Q(subAccount=kDell))
    aliases = Alias.objects.all()
    filters = Filter.objects.all()

    print(usernamee.id, usernamee)
    LOG,host,DT = dets()
    logFile(usernamee,email)
    return render(request, 'home.html', {'computers': computers, 'aliases': aliases, 'filters': filters ,'Email':email,'Name':usernamee.username,'DT':DT})

@login_required
def error(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    logFile(usernamee,email)
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'error.html')

@login_required
def error2(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    logFile(usernamee,email)
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'error2.html')

@login_required
def new_computer(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = ComputerForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['resourceId']#POST.get
        g = Computer.objects.filter(resourceId=str(name)).distinct()
        print(g,'-------')
        for tt in g:
             print(tt)
             if str(tt) == str(name):
                print('error')
                logFile(usernamee,email)
                return redirect('error')
        print('-------------:' ,form.cleaned_data['customerCode'])
        gust = codeCu(form.cleaned_data['resourceId'],form.cleaned_data['customerCode'])
        print(gust)
        computer = Computer()
        computer.resourceId = form.cleaned_data['resourceId']
        computer.fqdn = form.cleaned_data['resourceId']
        computer.subAccount = "{0}-{1}".format(form.cleaned_data['value'] ,form.cleaned_data['subAccount'])
        #computer.subAccount = form.cleaned_data['subAccount']

        computer.customerCode = gust
        
        computer.lastSavedDate = datetime.date.today()
        computer.save()

        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['resourceId']).split('.')[:1],
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home')
    logFile(usernamee,email)
    return render(request, 'computer_form.html', {'form': form})
    
@login_required
def mult_lds2(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    logFile(usernamee,email)
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'Multiple.html')

@login_required
def mult_lds(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    if request.method == 'POST' and bool(request.FILES.get('myfile', False)) : 
        myfile = request.FILES['myfile']
        queue = request.POST.get('queue',False) #POST.get
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        jjk = (str(settings.BASE_DIR)+str(uploaded_file_url))
        df = pd.read_csv(jjk)
        retb =  {'columns': df.columns, 'rows': df.to_dict('records') ,'queue':queue}
        dbak.data =df.to_dict('records') # retb
        dbak.queue = queue
        return render(request, 'my_view.html', retb )
        
    if request.method == 'POST':
       ##print(request.method.POST.get('save',False))
       no =[]
       for dk in dbak.data:
          name = dk['name'] #POST.get
          g = Computer.objects.filter(resourceId=name).distinct()
          print(g,'-------')
          for tt in g:
             print(tt)
             if str(tt) == str(name):
                print('error')
                return redirect('error')

       
       for dk in dbak.data:
          name = dk['name'] #POST.get
          print(dk)
          
          queue = dbak.queue #POST.get
          customer = dk['customer']
          severity = dk['severity']

          gust = codeCu(name,str(conff[str(dk['customer'])]))
          print(customer ,'_to_->',gust)
          computer = Computer()
          computer.resourceId = name
          computer.fqdn = name
          computer.subAccount = "{0}-{1}".format(severity ,queue)

          computer.customerCode = gust
        
          computer.lastSavedDate = datetime.date.today()
          computer.save()
          
          alias = Alias()
          alias.resourceId = name
          alias.alias = str(name).split('.')[:1],
          alias.lastSavedDate = datetime.date.today()
          alias.save()
          logFile(usernamee,email)
       '''if len(no)>0:
             messages.warning(request, 'Exception. There are: {} names already exist for this we have not saved them please check it out:see:{}'.format(len(no),str(no))) 
       else:'''
       return redirect('search')

    logFile(usernamee,email)
    print(request)
    return render(request, 'Multiple.html')

@login_required
def mult_save(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    logFile(usernamee,email)
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    if request.method == 'POST' and request.POST.get('queue',False):
        print(dbak.data)
        name = dbak.data['name'] #POST.get
        queue = dbak.data['queue'] #POST.get
        customer = dbak.data['customer']
        severity = dbak.data['severity']
        #dbak.data
        print(name,queue,'__________',customer,'-----',severity)
        
        return render(request, 'home.html' )
        
        
    return render(request, 'Multiple.html')
    
@login_required
def update_computer(request, _id):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computer = Computer.objects.filter(resourceId=_id)
    alias = Alias.objects.filter(resourceId=_id)
    
    if computer.get().subAccount.rfind('-') > -1:
       subAA = computer.get().subAccount.split('-')[0]
       subAB = computer.get().subAccount.split('-')[1]
    else:
       subAA = computer.get().subAccount
       subAB = computer.get().subAccount
       
    data = {
        'resourceId': computer.get().resourceId,
        'subAccount': subAA,
        'value': subAB,
        'customerCode': computer.get().customerCode
    }
    form = ComputerForm(request.POST or None, initial=data)
    if form.is_valid():
        Alias.objects.filter(resourceId=_id).delete()
        Computer.objects.filter(resourceId=_id).delete()
               
        computer = Computer()
        computer.resourceId = form.cleaned_data['resourceId']
        computer.fqdn = form.cleaned_data['resourceId']
        computer.subAccount = "{0}-{1}".format(form.cleaned_data['value'] ,form.cleaned_data['subAccount'])
        #computer.subAccount = form.cleaned_data['subAccount']

        computer.customerCode = form.cleaned_data['customerCode']
        
        computer.lastSavedDate = datetime.date.today()
        computer.save()

        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['resourceId']).split('.')[:1],
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home')
    logFile(usernamee,email)
    return render(request, 'computer_form.html', {'form': form})

@login_required
def delete_computer2(request, _id):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computers = Computer.objects.all()


    computer = Computer.objects.filter(resourceId=_id)
    print(request)
    resid = computer.get().resourceId
    suba  = computer.get().subAccount
    cust  = computer.get().customerCode
    fq    = computer.get().fqdn
    #loc  = computer.get().LOCATION
    
    
    Computer.objects.filter(resourceId=_id).delete()
    computer = Computer()
    
    computer.resourceId   = resid
    computer.fqdn         = fq
    computer.subAccount   = 'decom'
    computer.customerCode = cust
    computer.supportOrg   = 'decom'
    #computer.locaTion    = 'decom' 
    #computer.ibmmanaGed   = 5
    computer.lastSavedDate = datetime.date.today()
    computer.save()
    logFile(usernamee,email)
    return redirect('search')
    
        
@login_required
def delete_computer(request, _id):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    Computer.objects.filter(resourceId=_id).delete()
    logFile(usernamee,email)
    return redirect('home')

@login_required
def delete_filter(request, _id):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computers = Computer.objects.all()
    filters = Filter.objects.all()
    
    Filter.objects.filter(filterName=_id).delete()
    logFile(usernamee,email)
    return redirect('home')

@login_required
def new_alias(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['alias']).split('.')[:1]
        alias.lastSavedDate = datetime.date.today()
        alias.save()

        return redirect('home')
        logFile(usernamee,email)
    return render(request, 'alias_form.html', {'form': form})

@login_required
def new_filter(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = FilterForm(request.POST or None)
    
       
    if form.is_valid():


        name = str(form.cleaned_data['filterName']) #POST.get
        gg = Filter.objects.filter(filterName=name).distinct()
        if gg:
          tt = gg.get().filterName
          print(tt)
          if str(tt) == str(name):
                print('error')
                return redirect('error2')

        _filter = Filter()
        _filter.customerCode = str(form.cleaned_data['customerCode'])
        _filter.filterName = str(form.cleaned_data['filterName'])
        _filter.filterDesc = str(form.cleaned_data['filterDesc'])
        _filter.filterState =0
        _filter.filterWeight = form.cleaned_data['filterWeight']
        _filter.subAccount = str(form.cleaned_data['subAccount'])
        
        TKACT_RM = convr(form.cleaned_data['customerCode'] ,form.cleaned_data['value'])
        print(form.cleaned_data['customerCode'],form.cleaned_data['value'] , 'TKACT_RM' ,TKACT_RM) 
        _filter.ticketActionId =  int(TKACT_RM)
        _filter.ticketGroup = str(form.cleaned_data['ticketGroup'])
        _filter.save()
        logFile(usernamee,email)
        return redirect('home') #.lower()

    return render(request, 'filter_form.html', {'form': form})

@login_required
def update_filter(request ,_id):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    _filter = Filter.objects.filter(filterName=_id)
    data = {

        'customerCode': _filter.get().customerCode,
        'filterName': _filter.get().filterName,
        'filterDesc': _filter.get().filterDesc,
        'filterWeight': _filter.get().filterWeight,
        'subAccount': _filter.get().subAccount,
        'ticketActionId': _filter.get().ticketActionId,
        'ticketGroup': _filter.get().ticketGroup

    }
    form = FilterForm(request.POST or None, initial=data)
    #form = FilterForm(request.POST or None)
    
    
    
    
    if form.is_valid():
        TKACT_RM = convr(form.cleaned_data['customerCode'] ,form.cleaned_data['value'])
        name = str(form.cleaned_data['filterName']) #POST.get
        gg = Filter.objects.filter(filterName=name).distinct()
        if gg:
          tt = gg.get().filterName
          print(tt)
          if str(tt) == str(name):
                print('error')
                return redirect('error2')
        _filter.update(
            customerCode = form.cleaned_data['customerCode'],
            filterName = form.cleaned_data['filterName'],
            filterDesc = form.cleaned_data['filterDesc'],
            filterState =0,
            filterWeight = form.cleaned_data['filterWeight'],
            subAccount = form.cleaned_data['subAccount'],
            ticketActionId =  TKACT_RM,
            ticketGroup = form.cleaned_data['ticketGroup']
        )
        logFile(usernamee,email)
        return redirect('home')

    return render(request, 'filter_form.html', {'form': form})
    
##----2 add
@login_required
def new_alias2(request, _rid):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = form.cleaned_data['alias']
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home')

    return render(request, 'alias_form.html', {'form': form ,'rid': _rid})

@login_required
def new_filter2(request, _rid):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = FilterForm(request.POST or None)

    if form.is_valid():
        _filter = Filter()
        _filter.resourceId = form.cleaned_data['resourceId']
        _filter.customerCode = form.cleaned_data['customerCode']
        _filter.filterName = form.cleaned_data['filterName']
        _filter.filterDesc = form.cleaned_data['filterDesc']
        _filter.filterWeight = form.cleaned_data['filterWeight']
        _filter.subAccount = form.cleaned_data['subAccount']
        _filter.ticketGroup = form.cleaned_data['ticketGroup']
        _filter.save()
        logFile(usernamee,email)
        return redirect('home')

    return render(request, 'filter_form.html', {'form': form ,'rid': _rid})



@login_required
def searchdevice(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    resultsB = None
    resultsA = None
    if request.method == 'GET':
        query= request.GET.get('q')


        submitbutton= request.GET.get('submit')
        tr = []
        if query is not None:
               for crpm in computers:
                   if str(crpm.resourceId).lower().rfind(str(query).lower()) > -1:
                      resultsA= Computer.objects.filter(resourceId=str(query)).distinct()
                      print(str(crpm.customerCode))
                      crpm.customerCode = ese[str(crpm.customerCode)]
                      tr.append(crpm)
               logFile(usernamee,email)
               return render(request, 'result.html',{'computers': tr, 'aliases': aliases, 'filters': filters})
               

             

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

#filter
@login_required
def searchfilter(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    resultsB = None
    resultsA = None
    if request.method == 'GET': 
        query= request.GET.get('q')


        submitbutton= request.GET.get('submit')
        print(submitbutton)

        
        
        if query is not None:
            print(query,'query',Computer.ciClass)
               

            if request.GET.get('vehicleA'):
               kj = request.GET.get('vehicleA')
               trT = []
               for fir  in filters:
                   if str(fir.subAccount).lower().rfind(str(query).lower()) > -1:
                   
                      #resultsA= Computer.objects.filter(subAccount=query).distinct()
                      fir.customerCode = ese.get(str(fir.customerCode))
                      trT.append(fir)

                      
               logFile(usernamee,email)
               return render(request, 'resultff.html',{'filtersA': trT, 'aliases': aliases, 'filters': filters} )
               
               
            elif request.GET.get('vehicleB'):
               kjj = request.GET.get('vehicleB')
               trT2 = []
               for firT  in filters:
                   if str(firT.filterName).lower().rfind(str(query).lower())  > -1:
                      firT.customerCode = ese.get(str(firT.customerCode))
                      trT2.append(firT)

               return render(request, 'resultff2.html',{'filtersB': trT2, 'aliases': aliases, 'filters': filters} )
               

                  


            

        else:
            return render(request, 'search_filter.html')

    else:
        return render(request, 'search_filter.html')

@login_required
def view_all(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()

    #for ty in computers:
    #computers.customerCode =ese.get(str(computers.customerCode))
    #filters.customerCode =ese.get(str(filters.customerCode))
    logFile(usernamee,email)
    return render(request, 'all.html', {'computers': computers, 'aliases': aliases, 'filters': filters})

@login_required
def csvv(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    with open('stockitems_misuper.csv') as myfile:
         response = HttpResponse(myfile, content_type='text/csv')
         response['Content-Disposition'] = 'attachment; filename=stockitems_misuper.csv'
         return response

@login_required
def myview(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    df = pd.read_csv(file)
    return render(request, 'my_view.html', {'columns': df.columns, 'rows': df.to_dict('records')})

@login_required
def index(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

    return render(request, "my_view.html", locals())

@login_required
def view_log(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="manager":
       print(user.position)
       raise Http404('You are not allowed to access this link')
       
    csvnew = os.path.join(settings.BASE_DIR, 'logfile.csv')
    if isfile(csvnew):

        df = pd.read_csv(csvnew)
        data_html = df.to_html()
        context = {'loaded_data': data_html}

        retb =  {'columns': df.columns, 'rows': df.to_dict('records')}
        filepath = {'filee': csvnew}
        return render(request, 'my_view5.html', context ,filepath)
        
    

   
##################################normal##################################################

############################################################################################################
@login_required
def home5(request):
    print(request.user.id)
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    print(user.position)
    computers = Computer.objects.filter(~Q(subAccount=kDell))
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    current_user = request.user
    current_email = user.email
    print(current_user.id, current_user.username)
    print(type(current_user.username))
    LOG,host,DT = dets()
    logFile(usernamee,email)
    return render(request, 'home5.html', {'computers': computers, 'aliases': aliases, 'filters': filters ,'Email':current_email,'Name':current_user.username,'DT':DT})

@login_required
def error5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'error5.html')

@login_required
def error25(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'error25.html')

@login_required
def new_computer5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = ComputerForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['resourceId']#POST.get
        g = Computer.objects.filter(resourceId=str(name)).distinct()
        print(g,'-------')
        for tt in g:
             print(tt)
             if str(tt) == str(name):
                print('error')
                return redirect('error5')
        print('-------------:' ,form.cleaned_data['customerCode'])
        gust = codeCu(form.cleaned_data['resourceId'],form.cleaned_data['customerCode'])
        print(gust)
        computer = Computer()
        computer.resourceId = form.cleaned_data['resourceId']
        computer.fqdn = form.cleaned_data['resourceId']
        computer.subAccount = "{0}-{1}".format(form.cleaned_data['value'] ,form.cleaned_data['subAccount'])
        #computer.subAccount = form.cleaned_data['subAccount']

        computer.customerCode = gust
        
        computer.lastSavedDate = datetime.date.today()
        computer.save()

        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['resourceId']).split('.')[:1],
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home5')

    return render(request, 'computer_form5.html', {'form': form})
    
@login_required
def mult_lds25(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    return render(request, 'Multiple5.html')

@login_required
def mult_lds5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    if request.method == 'POST' and bool(request.FILES.get('myfile', False)) : 
        myfile = request.FILES['myfile']
        queue = request.POST.get('queue',False) #POST.get
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        jjk = (str(settings.BASE_DIR)+str(uploaded_file_url))
        df = pd.read_csv(jjk)
        retb =  {'columns': df.columns, 'rows': df.to_dict('records') ,'queue':queue}
        dbak.data =df.to_dict('records') # retb
        dbak.queue = queue
        return render(request, 'my_view5.html', retb )
        
    if request.method == 'POST':
       ##print(request.method.POST.get('save',False))
       no =[]
       for dk in dbak.data:
          name = dk['name'] #POST.get
          g = Computer.objects.filter(resourceId=name).distinct()
          print(g,'-------')
          for tt in g:
             print(tt)
             if str(tt) == str(name):
                print('error5')
                logFile(usernamee,email)
                return redirect('error5')

       
       for dk in dbak.data:
          name = dk['name'] #POST.get
          print(dk)
          
          queue = dbak.queue #POST.get
          customer = dk['customer']
          severity = dk['severity']

          gust = codeCu(name,str(conff[str(dk['customer'])]))
          print(customer ,'_to_->',gust)
          computer = Computer()
          computer.resourceId = name
          computer.fqdn = name
          computer.subAccount = "{0}-{1}".format(severity ,queue)

          computer.customerCode = gust
        
          computer.lastSavedDate = datetime.date.today()
          computer.save()
          
          alias = Alias()
          alias.resourceId = name
          alias.alias = str(name).split('.')[:1],
          alias.lastSavedDate = datetime.date.today()
          alias.save()
          logFile(usernamee,email)
       '''if len(no)>0:
             messages.warning(request, 'Exception. There are: {} names already exist for this we have not saved them please check it out:see:{}'.format(len(no),str(no))) 
       else:'''
       return redirect('search5')


    print(request)
    return render(request, 'Multiple5.html')

@login_required
def mult_save5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    if request.method == 'POST' and request.POST.get('queue',False):
        print(dbak.data)
        name = dbak.data['name'] #POST.get
        queue = dbak.data['queue'] #POST.get
        customer = dbak.data['customer']
        severity = dbak.data['severity']
        #dbak.data
        print(name,queue,'__________',customer,'-----',severity)
        
        return render(request, 'home5.html' )
        
        
    return render(request, 'Multiple5.html')
    
    
        

@login_required
def new_alias5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['alias']).split('.')[:1]
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home5')

    return render(request, 'alias_form5.html', {'form': form})

@login_required
def new_filter5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = FilterForm(request.POST or None)
    
       
    if form.is_valid():


        name = str(form.cleaned_data['filterName']) #POST.get
        gg = Filter.objects.filter(filterName=name).distinct()
        if gg:
          tt = gg.get().filterName
          print(tt)
          if str(tt) == str(name):
                print('error5')
                return redirect('error25')

        _filter = Filter()
        _filter.customerCode = str(form.cleaned_data['customerCode'])
        _filter.filterName = str(form.cleaned_data['filterName'])
        _filter.filterDesc = str(form.cleaned_data['filterDesc'])
        _filter.filterState =0
        _filter.filterWeight = form.cleaned_data['filterWeight']
        _filter.subAccount = str(form.cleaned_data['subAccount'])
        
        TKACT_RM = convr(form.cleaned_data['customerCode'] ,form.cleaned_data['value'])
        print(form.cleaned_data['customerCode'],form.cleaned_data['value'] , 'TKACT_RM' ,TKACT_RM) 
        _filter.ticketActionId =  int(TKACT_RM)
        _filter.ticketGroup = str(form.cleaned_data['ticketGroup'])
        _filter.save()
        logFile(usernamee,email)
        return redirect('home5') #.lower()

    return render(request, 'filter_form5.html', {'form': form})

##----5 add
@login_required
def new_alias25(request, _rid):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email

    if user.position!="normal":
       print(user.position)
       raise Http404('You are not allowed to access this link')
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = form.cleaned_data['alias']
        alias.lastSavedDate = datetime.date.today()
        alias.save()
        logFile(usernamee,email)
        return redirect('home5')

    return render(request, 'alias_form5.html', {'form': form ,'rid': _rid})

@login_required
def new_filter25(request, _rid):
    form = FilterForm(request.POST or None)
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    if form.is_valid():
        _filter = Filter()
        _filter.resourceId = form.cleaned_data['resourceId']
        _filter.customerCode = form.cleaned_data['customerCode']
        _filter.filterName = form.cleaned_data['filterName']
        _filter.filterDesc = form.cleaned_data['filterDesc']
        _filter.filterWeight = form.cleaned_data['filterWeight']
        _filter.subAccount = form.cleaned_data['subAccount']
        _filter.ticketGroup = form.cleaned_data['ticketGroup']
        _filter.save()
        logFile(usernamee,email)
        return redirect('home5')

    return render(request, 'filter_form5.html', {'form': form ,'rid': _rid})



@login_required
def searchdevice5(request):
    user=UserProfileInfo.objects.get(id=request.user.id)
    usernamee = request.user
    email = user.email
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    resultsB = None
    resultsA = None
    if request.method == 'GET':
        query= request.GET.get('q')


        submitbutton= request.GET.get('submit')
        tr = []
        if query is not None:
               for crpm in computers:
                   if str(crpm.resourceId).lower().rfind(str(query).lower()) > -1:
                      resultsA= Computer.objects.filter(resourceId=str(query)).distinct()
                      print(str(crpm.customerCode))
                      crpm.customerCode = ese[str(crpm.customerCode)]
                      tr.append(crpm)
               logFile(usernamee,email)
               return render(request, 'result5.html',{'computers': tr, 'aliases': aliases, 'filters': filters})
               

             

        else:
            return render(request, 'search5.html')

    else:
        return render(request, 'search5.html')


#filter
@login_required
def searchfilter5(request):

    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    resultsB = None
    resultsA = None
    if request.method == 'GET': 
        query= request.GET.get('q')


        submitbutton= request.GET.get('submit')
        print(submitbutton)

        
        
        if query is not None:
            print(query,'query',Computer.ciClass)
               

            if request.GET.get('vehicleA'):
               kj = request.GET.get('vehicleA')
               trT = []
               for fir  in filters:
                   if str(fir.subAccount).lower().rfind(str(query).lower()) > -1:
                   
                      #resultsA= Computer.objects.filter(subAccount=query).distinct()
                      fir.customerCode = ese.get(str(fir.customerCode))
                      trT.append(fir)

                      

               return render(request, 'resultff5.html',{'filtersA': trT, 'aliases': aliases, 'filters': filters} )
               
               
            elif request.GET.get('vehicleB'):
               kjj = request.GET.get('vehicleB')
               trT2 = []
               for firT  in filters:
                   if str(firT.filterName).lower().rfind(str(query).lower())  > -1:
                      firT.customerCode = ese.get(str(firT.customerCode))
                      trT2.append(firT)

               return render(request, 'resultff25.html',{'filtersB': trT2, 'aliases': aliases, 'filters': filters} )
               


        else:
            return render(request, 'search_filter5.html')

    else:
        return render(request, 'search_filter5.html')

@login_required
def myview5(request):
    df = pd.read_csv(file)
    return render(request, 'my_view5.html', {'columns': df.columns, 'rows': df.to_dict('records')})

@login_required
def index5(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

    return render(request, "my_view5.html", locals())

