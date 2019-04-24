from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Algorithm_template

from django.http import JsonResponse
from django.conf import settings
import os

def index(request):
    # jport = "8888"

    # command = "jupyter notebook stop " + jport
    #
    # os.system(command)

    # c0 = "cd"
    # c1 = "jupyter notebook --no-browser --port " + jport + \
    #      " --NotebookApp.token='' --NotebookApp.disable_check_xsrf=True"
    #
    # command = c0 + "&&" + c1
    #
    # output = os.popen(command)
    #
    # print(output.read())

    return render(request, 'displayer/index.html')

def editor(request):
    url_active = "/step_intro/"
    if 'select_tem' in request.POST:
        # step1
        url_active = "/select_tem/"
    if 'ide_coding' in request.POST:
        # setp2
        url_active = "/ide_editor/"    
    if 'config_sub' in request.POST:
        # setp3
        url_active = "/config_sub/"
    if 'view_jobs' in request.POST:
        # setp3
        url_active = "/view_jobs/"
    return render(request, 'displayer/editor.html', locals())

# 多个editor页面步骤
def step_intro(request):
    # data = Algorithm_template.objects.get(name_en='Lasso') 
    # filename = os.path.join(settings.MEDIA_ROOT , data.template_file.path)
    return render(request,'displayer/step_intro.html',locals())  

def select_tem(request):
    # algs_all = models.Algorithm_template.objects.values("category","name_en","name").order_by("category")
    algs_all = Algorithm_template.objects.all()
    return render(request,'displayer/select_tem.html',locals()) 

def ide_editor(request):
    return render(request,'displayer/ide_editor.html',locals()) 


def copy_tem(request):    
    name_en = request.GET.get("name_templ")
    print(name_en)
    
    data = Algorithm_template.objects.get(name_en = name_en)
    filename = os.path.join(settings.MEDIA_ROOT , data.template_file.path)
   
    command = "cp "+filename+" user_code/UserCode.ipynb"

    output = os.popen(command)

    a = {
            "a":"OK",
            "filename":filename,
            "output":"output"
            }

    return JsonResponse(a)



def config_sub(request):
    # ipynb_name = 
    # # 将代码按照日期保存，方便下次使用
    # command = "cp user_code/UserCode.ipynb user_code/"+ ipynb_name+".ipynb "
    # output1 = os.popen(command)
    # print(output1)

    # 将ipynb文件转化成py
    command = "jupyter nbconvert --to python user_code/UserCode.ipynb"
    output1 = os.popen(command)
    print(output1)

    return render(request,'displayer/config_sub.html')   

def submit_job(request):
    print("begin to submit_job")
    jobname = request.POST.get("jobname")
    command = "rm /Users/houxinming/Documents/UserCode.py && cp user_code/UserCode.py /Users/houxinming/Documents/"
    output2 = os.popen(command)

    filename =  "/Users/houxinming/Documents/"
    
    print(jobname)


    res = {
            "a": "OK",
            # "filename": filename,
            # "jobname":jobname,
        }
    return JsonResponse(res)

    

def view_jobs(request):
    return render(request,'displayer/view_jobs.html')

# narbar的页面
def monitor(request):
    return render(request, 'displayer/monitor.html')

def deploy(request):
    return render(request, 'displayer/deploy.html')

def training(request):
    return render(request, 'displayer/training.html')

def docs(requset):
    return render(requset, 'displayer/docs.html')

def case(requset):
    return render(requset, 'displayer/case.html')



def test_page(request):
    return render(request, 'displayer/test_page.html')


