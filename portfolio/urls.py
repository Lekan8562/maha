from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home,project_detail,project_comment,project_reply


app_name = 'portfolio'

urlpatterns = [
    path('',home,name='home'),
    path('<slug:project_slug>/',project_detail,name='project_detail'),
    path('project/comment/<int:project_id>/',project_comment,name='project_comment'),
    path('reply/<int:comment_id>/',project_reply,name='project_reply')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
