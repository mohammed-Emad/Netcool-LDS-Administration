from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Computer, Alias, Filter
import datetime
from .forms import ComputerForm, AliasForm, FilterForm
import os
from django.contrib.auth.models import User
import pandas as pd
import csv
import codecs
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.conf import settings
from django.conf.urls.static import static
from .filters import UserFilter
import os
import socket
kDell = 'Kdell'


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
    
ese = {'igu': 'US', 'igl': 'LA', 'chs': 'CA', 'igp': 'AP', 'igj': 'JP', 'ige': 'EMEA'}

def convr(GCUST,SRVLV):

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
    

    
def home(request):
    computers = Computer.objects.filter(~Q(subAccount=kDell))
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    LOG,host,DT = dets()
    return render(request, 'home.html', {'computers': computers, 'aliases': aliases, 'filters': filters ,'LOG':LOG,'host':host,'DT':DT})


def new_computer(request):
    form = ComputerForm(request.POST or None)

    if form.is_valid():
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
        
        return redirect('home')

    return render(request, 'computer_form.html', {'form': form})
    
    
def mult_lds2(request):

    return render(request, 'Multiple.html')
    
def mult_lds(request):
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
        
    if request.method == 'POST' and request.POST.get('save',False):
       no = []
       print(dbak.data)
       for dk in dbak.data:
          name = dk['name'] #POST.get
          if Computer.objects.filter(resourceId=name) is not None:
              print('no',no)
              no.append(name)
              continue
          queue = dbak.queue #POST.get
          customer = dk['customer']
          severity = dk['severity']
   
          computer = Computer()
          computer.resourceId = name
          computer.fqdn = name
          computer.subAccount = "{0}-{1}".format(severity ,queue)

          computer.customerCode = customer
        
          computer.lastSavedDate = datetime.date.today()
          computer.save()
          
          alias = Alias()
          alias.resourceId = name
          alias.alias = str(name).split('.')[:1],
          alias.lastSavedDate = datetime.date.today()
          alias.save()

       if len(no) >0:
         k = 'Sorry these names already exist, will be discarded ({})'.format(no)
         return render_to_response('Multiple.html', {'message':k})

       else:
         return render_to_response('Multiple.html', {'message':'Save complete'})

    #return redirect('search')


    print(request)
    return render(request, 'Multiple.html')

def mult_save(request):
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
    
    
def update_computer(request, _id):
    computer = Computer.objects.filter(id=_id)
    aliasA = Alias.objects.all()
    

            
    data = {
        'resourceId': computer.get().resourceId,
        'subAccount': computer.get().subAccount.split('-')[0],
        'value': computer.get().subAccount.split('-')[1],
        'customerCode': computer.get().customerCode
    }
    form = ComputerForm(request.POST or None, initial=data)

    if form.is_valid():
    
        for als in aliasA:
            if computer.resourceId == als.resourceId:
        
               alias = Alias(id=als.id)
               alias.update(
                    resourceId = form.cleaned_data['resourceId'],
                    alias = str(form.cleaned_data['resourceId']).split('.')[:1],
                    lastSavedDate = datetime.date.today()
               )
               
        computer.update(
            resourceId=form.cleaned_data['resourceId'],
            fqdn=form.cleaned_data['resourceId'],
            subAccount="{0}-{1}".format(form.cleaned_data['value'] ,form.cleaned_data['subAccount'])
        )


        return redirect('home')

    return render(request, 'computer_form.html', {'form': form})

def delete_computer2(request, _id):
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()
    
    #Computer.objects.filter(id=_id).delete() #.update(supportOrg=kDell, subAccount=kDell)
    Cm = Computer.objects.filter(id=_id)
    for cmb in computers:
        if cmb.id == _id:
           iid = cmb.resourceId
           icu = cmb.customerCode
           Alias.objects.filter(resourceId=iid).delete()
           Computer.objects.filter(id=_id).delete()
           print(iid,icu,"resourceId-resourceId")

    return redirect('home')

def delete_computer(request, _id):
    Computer.objects.filter(id=_id).delete()
    return redirect('home')


def delete_filter(request, _id):
    computers = Computer.objects.all()
    filters = Filter.objects.all()
    
    Cm = Computer.objects.filter(id=_id)
    for filt in filters:
        if filt.id == _id:
           iid = filt.id
           icu = filt.customerCode
           
           Filter.objects.filter(id=iid).delete()
           #Computer.objects.filter(id=_id).delete()

    return redirect('home')


def new_alias(request):
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = str(form.cleaned_data['alias']).split('.')[:1]
        alias.lastSavedDate = datetime.date.today()
        alias.save()

        return redirect('home')

    return render(request, 'alias_form.html', {'form': form})


def new_filter(request):
    form = FilterForm(request.POST or None)

    if form.is_valid():
        _filter = Filter()
        _filter.customerCode = form.cleaned_data['customerCode']
        _filter.filterName = form.cleaned_data['filterName']
        _filter.filterDesc = form.cleaned_data['filterDesc']
        _filter.filterWeight = form.cleaned_data['filterWeight']
        _filter.subAccount = form.cleaned_data['subAccount']
        
        TKACT_RM = convr(form.cleaned_data['customerCode'] ,form.cleaned_data['value'])
        print(form.cleaned_data['customerCode'],form.cleaned_data['value'] , 'TKACT_RM' ,TKACT_RM) 
        _filter.ticketActionId =  TKACT_RM
        _filter.ticketGroup = form.cleaned_data['ticketGroup']
        _filter.save()

        return redirect('home')

    return render(request, 'filter_form.html', {'form': form})

def update_filter(request ,_id):
    form = FilterForm(request.POST or None)
    _filter = Filter.objects.filter(id=_id)
    
    if form.is_valid():
        TKACT_RM = convr(form.cleaned_data['customerCode'] ,form.cleaned_data['value'])
        _filter.update(
            customerCode = form.cleaned_data['customerCode'],
            filterName = form.cleaned_data['filterName'],
            filterDesc = form.cleaned_data['filterDesc'],
            filterWeight = form.cleaned_data['filterWeight'],
            subAccount = form.cleaned_data['subAccount'],
            ticketActionId =  TKACT_RM,
            ticketGroup = form.cleaned_data['ticketGroup']
        )

        return redirect('home')

    return render(request, 'filter_form.html', {'form': form})
    
##----2 add
def new_alias2(request, _rid):
    form = AliasForm(request.POST or None)

    if form.is_valid():
        alias = Alias()
        alias.resourceId = form.cleaned_data['resourceId']
        alias.alias = form.cleaned_data['alias']
        alias.lastSavedDate = datetime.date.today()
        alias.save()

        return redirect('home')

    return render(request, 'alias_form.html', {'form': form ,'rid': _rid})


def new_filter2(request, _rid):
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

        return redirect('home')

    return render(request, 'filter_form.html', {'form': form ,'rid': _rid})




def searchdevice(request):

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
                   if crpm.resourceId.rfind(query) > -1:
                      resultsA= Computer.objects.filter(resourceId=str(query)).distinct()
                      crpm.customerCode = ese.get(str(crpm.customerCode))
                      tr.append(crpm)
                      
               return render(request, 'result.html',{'computers': tr, 'aliases': aliases, 'filters': filters})
               

             

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

#filter
def searchfilter(request):

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
                   if fir.subAccount.rfind(query) > -1:
                   
                      #resultsA= Computer.objects.filter(subAccount=query).distinct()
                      fir.customerCode = ese.get(str(fir.customerCode))
                      trT.append(fir)

                      

               return render(request, 'resultff.html',{'filtersA': trT, 'aliases': aliases, 'filters': filters} )
               
               
            elif request.GET.get('vehicleB'):
               kjj = request.GET.get('vehicleB')
               trT2 = []
               for firT  in filters:
                   if firT.filterName.rfind(query) > -1:
                      firT.customerCode = ese.get(str(firT.customerCode))
                      trT2.append(firT)

               return render(request, 'resultff2.html',{'filtersB': trT2, 'aliases': aliases, 'filters': filters} )
               

                  


            

        else:
            return render(request, 'search_filter.html')

    else:
        return render(request, 'search_filter.html')


def view_all(request):
    computers = Computer.objects.all()
    aliases = Alias.objects.all()
    filters = Filter.objects.all()

    #for ty in computers:
    #computers.customerCode =ese.get(str(computers.customerCode))
    #filters.customerCode =ese.get(str(filters.customerCode))
    return render(request, 'all.html', {'computers': computers, 'aliases': aliases, 'filters': filters})


def csvv(request):
    with open('stockitems_misuper.csv') as myfile:
         response = HttpResponse(myfile, content_type='text/csv')
         response['Content-Disposition'] = 'attachment; filename=stockitems_misuper.csv'
         return response

         
def myview(request):
    df = pd.read_csv(file)
    return render(request, 'my_view.html', {'columns': df.columns, 'rows': df.to_dict('records')})


def index(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        csvfile.open()
        reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

    return render(request, "my_view.html", locals())
    
    
