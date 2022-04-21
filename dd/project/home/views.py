# import imp
from django.shortcuts import render
# from django.utils import timezone

# from matplotlib.style import context


# Create your views here.
def home(request):
    # now = timezone.now()
    # students={'names':['ram','shyam','hari','sita','saroj']}
    stu = {'stu1':{'name':'roshan', 'roll':'1'},
           'stu2':{'name':'hari', 'roll':'2'},
           'stu3':{'name':'ram', 'roll':'3'},
           'stu4':{'name':'sita', 'roll':'4'}
            }
    students = {'student':stu}
    return render(request,'home/home.html',students)
    