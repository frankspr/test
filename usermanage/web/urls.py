from django.conf.urls import  include, url
from django.contrib import admin
from web import views
from web.views import HomeView,AccountView

urlpatterns = [
    # Examples:
    # url(r'^$', 'usermanage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',AccountView.Login ),
    url(r'^index/',HomeView.Index),
    #url(r'^userlist/(?P<id>\d*)',HomeView.UserList),
    url(r'^userlist/$',HomeView.UserList),
    url(r'^userdetail/(?P<id>\d*)/$',HomeView.UserDetail),
    url(r'^adduser/',HomeView.AddUser),
    url(r'^deluser/',HomeView.DelUser),
    
    url(r'^loginform/',AccountView.LoginByForm ),
    
]