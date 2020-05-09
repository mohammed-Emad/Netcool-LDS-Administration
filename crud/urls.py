from django.urls import path ,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from .views import home, new_computer, update_computer, delete_computer, delete_computer2, new_alias, new_filter ,searchdevice,searchfilter ,view_all,myview,mult_lds, new_alias2, new_filter2 ,delete_filter,update_filter,mult_save,error,error2,special ,index ,user_logout ,register ,user_login,login_conv

from .views import home5, new_computer5, new_alias5, new_filter5 ,searchdevice5,searchfilter5 ,myview5, mult_lds5, new_alias25, new_filter25 ,mult_save5, error5, error25 ,view_log


urlpatterns = [
    path('', user_login, name="user_login"),
    path('home/', home, name="home"),#login_conv
    path('login_conv/', login_conv, name="login_conv"),
    path('new_computer', new_computer, name="new_computer"),
    path('update_computer/<str:_id>', update_computer, name="update_computer"),
    path('update_filter/<str:_id>', update_filter, name="update_filter"),
    path('delete_computer/<str:_id>', delete_computer, name="delete_computer"),
    path('delete_computer2/<str:_id>', delete_computer2, name="delete_computer2"),
    path('delete_filter/<str:_id>', delete_filter, name="delete_filter"),
    path('new_alias', new_alias, name="new_alias"),
    path('new_filter', new_filter, name="new_filter"),
    path('new_alias2/<str:_rid>', new_alias2, name="new_alias2"),
    path('new_filter2/<str:_rid>', new_filter2, name="new_filter2"),
    path('search/', searchdevice, name='search'),
    path('searchfilter/', searchfilter, name='searchfilter'),
    path('view_log/', view_log, name='view_log'),
    #--------------------------------#
    path('home5/', home5, name="home5"),#login_conv
    path('new_computer5', new_computer5, name="new_computer5"),
    path('new_alias5', new_alias5, name="new_alias5"),
    path('new_filter5', new_filter5, name="new_filter5"),
    path('new_alias25/<str:_rid>', new_alias25, name="new_alias25"),
    path('new_filter25/<str:_rid>', new_filter25, name="new_filter25"),
    path('search5/', searchdevice5, name='search5'),
    path('searchfilter5/', searchfilter5, name='searchfilter5'),
    path('error5/', error5, name="error5"),
    path('error2/', error25, name="error2"),
    path('mult_lds5/', mult_lds5, name="mult_lds5"),
    path('mult_save5/', mult_save5, name="mult_save5"),
    #--------------------------------#
    path('view_all/', view_all, name='view_all'),
    path('error/', error, name="error"),
    path('error2/', error2, name="error2"),
    path('mult_lds/', mult_lds, name="mult_lds"),
    path('mult_save/', mult_save, name="mult_save"),
    path('accounts/', include('django.contrib.auth.urls')),
    
]

urlpatterns += [
    url(r'^$',index,name='index'),
    url(r'^special/',special,name='special'),
    url(r'^logout/$', user_logout, name='logout'),
]

urlpatterns +=[
    url(r'^register/$',register,name='register'),
    url(r'^user_login/$',user_login,name='user_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
