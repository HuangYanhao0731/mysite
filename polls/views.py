from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.http import StreamingHttpResponse
from django.contrib import messages

@login_required
def homepage(request):
     return render(request, "polls/homepage.html")

def login(request):
     return render(request, "polls/index.html")

def index(request):
     u = request.POST.get("email", '')
     p = request.POST.get("pwd", '')

     if u != None and p != None:
          #return HttpResponse("登录成功！")
          return render(request, "polls/homepage.html")
     else:
          return HttpResponse("登录失败！")
     #return render(request, "polls/index.html")

#注册界面
def register(request):
     return render(request, "polls/register.html")




#文件上传
def upload(request):
     if request.method == 'POST':
          uploaded_file = request.FILES['document']
          print(uploaded_file.name)
          print(uploaded_file.size)
     return render(request, "polls/upload.html")
# def upload(request):
#     if request.method == "POST":
#         fid = request.POST.get("fid")
#         files = request.FILES.getlist("myfiles")
#         uid = request.POST.get("uid")
#         if files is None:
#             return HttpResponse("请选择需要上传的文件")
#         for f in files:
#             file = AFile()
#             file.name = f.name
#             file.f_id = fid
#             file.save()
#             d = open(os.path.join('static/media/yf_upload', f.name), 'wb+')
#             for chunk in f.chunks():
#                 d.write(chunk)
#                 d.close()
#         file_list = FileMain.objects.filter(insert_people=uid)
#     return render(request, "polls/upload.html",{'file_list':file_list})

#设置
def setting(request):
     return render(request,"polls/setting.html")

#训练数据
def train(request):
     context = {}
     if request.method == 'POST':
          uploaded_file = request.FILES['document']
          fs = FileSystemStorage()
          name = fs.save(uploaded_file.name, uploaded_file) #储存文件
          context['url'] = fs.url(name)

     return render(request, "polls/train.html", context)

#用户反馈
def report(request):
     return render(request, "polls/report.html")

#图标复核
def table(request):
     return render(request, "polls/table.html")

#分析结果
def show_result(request):
     f = open('test/2021.06异常商品数据.txt', 'r',)
     attack_method = f.read()
     attack_method = attack_method.split('\n')
     f.close()
     return render(request, "polls/show_result.html",{"attack_method": attack_method})

#结果
def result(request):
     f = open('test/2021.06异常商品数据.txt', 'r', )
     attack_method = f.read()
     attack_method = attack_method.split('\n')
     f.close()
     return  render(request,"polls/result.html",{"attack_method": attack_method})

#下载数据
def download(request):
     file = open('test/2021.06异常商品数据.xlsx', 'rb')
     response = FileResponse(file)
     response['Content-Type'] = 'application/octet-stream'
     response['Content-Disposition'] = 'attachment;filename="2021.06.xlsx"'
     return response

def download2(request):
     file = open('test/2021.07异常商品数据.xlsx', 'rb')
     response = FileResponse(file)
     response['Content-Type'] = 'application/octet-stream'
     response['Content-Disposition'] = 'attachment;filename="2021.07.xlsx"'
     return response

def toast(response):
     messages.success(response, "哈哈哈哈")

