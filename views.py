from django.shortcuts import render,redirect
from .models import signupform,loginform,railway1,tourismm,educationm,fertilizerm
from .forms import signupf,loginformf,railwayform,tourismform,educationform,fertilizerform
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create your views here.
def index(request):
    return render(request,'docs/site_pages/carousel/index.html')
def contactus(request):
    return render(request,'docs/site_pages/contactus/contactus.html')
def login(request):
    if request.method == 'POST':
        form=loginformf(request.POST)
        if form.is_valid():
            new_req=loginform(lemail=request.POST['useremail'],lpassword=request.POST['userpass'])
            new_req.save()
            e=signupform.objects.filter(email=new_req.lemail)
            if len(e)==0:
                return render(request,'docs/site_pages/login/login.html',{'text':"Invalid Details"})
            else:
                for i in e:
                    if i.password==new_req.lpassword:
                        global name_user
                        name_user=i.username
                        return render(request,'docs/site_pages/ministry/ministry.html',{'name':i.username})
                    else:
                        return render(request,'docs/site_pages/login/login.html',{'text':"Invalid Details"})
    else:
        form=loginformf()
    context={'form':form}
    return render(request,'docs/site_pages/login/login.html',context)


def signup(request):
    if request.method == 'POST':
        form=signupf(request.POST)
        if form.is_valid():
            new_req=signupform(username=request.POST['user'],email=request.POST['emailid'],password=request.POST['passw'])
            new_req.save()
            return redirect('login')
    else:
        form=signupf()
    context={'form':form}
    return render(request,'docs/site_pages/signup/signup.html',context)

def ministry(request):
    return render(request,'docs/site_pages/ministry/ministry.html',{'name':name_user})
def railway(request):
    if request.method == 'POST':
        form=railwayform(request.POST)
        if form.is_valid():
            new_req=railway1(track_length=request.POST['trackl'])
            new_req.save()
            data=pd.read_csv('railway.csv')
            x=data['Year'].values
            for i in range(len(x)):
                x[i]=int(x[i][0:4])
            y=data['Total'].values
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)
            x_train=x_train.reshape(-1,1)
            x_test=x_test.reshape(-1,1)
            model=LinearRegression()
            model.fit(x_train,y_train)
            n=int(new_req.track_length)
            pred=model.predict(np.array(n).reshape(-1,1))

            return render(request,'docs/site_pages/railway/railway.html',{'text':pred[0],'year':'Total Length of Running Railway Tracks(Km) in '+ new_req.track_length +' is ','name':name_user})
    else:
        form=railwayform()
    context={'form':form,'name':name_user}
    return render(request,'docs/site_pages/railway/railway.html',context)
def tourism(request):
    if request.method == 'POST':
        form=tourismform(request.POST)
        if form.is_valid():
            new_req=tourismm(yeart=request.POST['yeartf'])
            new_req.save()
            data=pd.read_csv('tourism.csv')
            x=data['Year'].values
            y=data['Foreign Tourist Ariivals in Numbers'].values
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)
            x_train=x_train.reshape(-1,1)
            x_test=x_test.reshape(-1,1)
            model=LinearRegression()
            model.fit(x_train,y_train)
            n=int(new_req.yeart)
            pred=model.predict(np.array(n).reshape(-1,1))
            return render(request,'docs/site_pages/tourism/tourism.html',{'text':pred[0],'year':'Total Number of Foreign Tourists Who may Visit India in '+ new_req.yeart+' are ','name':name_user})
    else:
        form=tourismform()
    context={'form':form,'name':name_user}
    return render(request,'docs/site_pages/tourism/tourism.html',context)   
def agriculture(request):
    if request.method == 'POST':
        form=fertilizerform(request.POST)
        if form.is_valid():
            new_req=fertilizerm(yeaf=request.POST['yearff'])
            new_req.save()
            x=np.array([40324,65527,109020])
            y=np.array([2011,2013,2016])
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)
            x_train=x_train.reshape(-1,1)
            x_test=x_test.reshape(-1,1)
            model=LinearRegression()
            model.fit(x_train,y_train)
            n=int(new_req.yeaf)
            pred=model.predict(np.array(n).reshape(-1,1))
            return render(request,'docs/site_pages/agriculture/agriculture.html',{'text':pred[0],'year':'Total Amount Bio Fertilizer Production(MT) in India Year '+ new_req.yeaf+' is ','name':name_user})

    else:
        form=fertilizerform()
    context={'form':form,'name':name_user}
    return render(request,'docs/site_pages/agriculture/agriculture.html',context)
def education(request):
    if request.method == 'POST':
        form=educationform(request.POST)
        if form.is_valid():
            new_req=educationm(yeare=request.POST['yearef'])
            new_req.save()
            ds=pd.read_csv("data.csv")
            x=ds["Year"].values
            y=ds["All Categories - Class I-V - Girls"].values
            x=np.delete(x,28)
            y=np.delete(y,28)
            for i in range(28):
                x[i]=(x[i])[0:4]
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=21)
            x_train=x_train.reshape(-1,1)
            x_test=x_test.reshape(-1,1)
            model=LinearRegression()
            model.fit(x_train,y_train)
            n=int(new_req.yeare)
            pred=model.predict(np.array(n).reshape(-1,1))
            return render(request,'docs/site_pages/education/education.html',{'text':pred[0],'year':'Gross Enrollment of Class I-V - Girls in Schools in India in '+ new_req.yeare+' is ','sign':'%','name':name_user})
    else:
        form=educationform()
    context={'form':form,'name':name_user}
    return render(request,'docs/site_pages/education/education.html',context)





