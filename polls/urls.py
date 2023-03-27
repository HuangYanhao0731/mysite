from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# 如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。
# 为了创建 URLconf，请在 polls 目录里新建一个 urls.py 文件。你的应用目录现在看起来应该是这样：

urlpatterns = [
    path('', views.homepage, name='homepage'),    #首页
    path('login/', views.login, name='login'),    #登录界面
    path('index/', views.index, name='index', ),
    #注册界面
    path('register/',views.register,name='register'),

    #文件上传路由配置
    path('upload/', views.upload, name='upload'),

    #设置界面
    path('index/setting/', views.setting, name='setting'),
    #训练数据
    path('index/train/',views.train, name='train'),
    #用户反馈
    path('index/report',views.report, name='report'),
    #图表复核
    path('index/table', views.table, name='table'),
    #分析结果
    path('index/show_result',views.show_result,name='show_result'),
    #结果
    path('index/result',views.result,name='result'),
    #下载数据
    path('download/',views.download),

    path('download2/', views.download2),
    #提示框
    path('toast/',views.toast),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)