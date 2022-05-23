from django.shortcuts import render
from .models import Information,InformationForm
import pickle
import sklearn

global ssc_p,hsc_p,degree_p,workex,etest_p,specialisation
def get(request):
    global ssc_p, hsc_p, degree_p, workex, etest_p, specialisation
    if request.method=='POST':
        form=InformationForm(request.POST)
        if form.is_valid():
            ssc_p=form.cleaned_data.get('ssc_p')
            hsc_p=form.cleaned_data.get('hsc_p')
            degree_p=form.cleaned_data.get('degree_p')
            workex=form.cleaned_data.get('workex')
            etest_p=form.cleaned_data.get('etest_p')
            specialisation=form.cleaned_data.get('specialisation')
            form.save()
    form=InformationForm()
    return render(request,'first/info.html',{'form':form})

def result(request):
    data=Information.objects.last()
    result=getPredications(data)
    return render(request,'first/show.html',{'result':result})

def getPredications(data):
    model=pickle.load(open('C://Users//MADHURI//Desktop//Place_model.sav','rb'))
    predicate=model.predict([[data.ssc_p,data.hsc_p,data.degree_p,data.workex,data.etest_p,data.specialisation]])
    predicate1=predicate[0]

    if predicate1==1:
        return 'Placed'
    elif predicate1==0:
        return 'Not Placed'
    else:
        return 'Error'

# Create your views here.
def home(request):
    return render(request,'first/home.html')

def about(request):
    return render(request,'first/about_us.html')

def contact(request):
    return render(request,'first/contact.html')