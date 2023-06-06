from django.urls import path,include

from .views import post_index, post_create, post_detail, post_update, post_delete

app_name = 'post'

urlpatterns = [

    path('index/', post_index , name="index"),
    path('create/', post_create, name='create'),
    # path('detail/<int:pk>/', post_detail, name='detail')
    path('filer/', include('filer.urls')),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/update/', post_update, name="update"),
    path('<slug:slug>/delete/', post_delete, name='delete'),


]
# from django.urls import path
#
# from .views import dosya_detay,versiyonunu_goster
#
# app_name = 'post'
#
# urlpatterns = [
#
#     path('index/', dosya_detay, name="index"),
#     path('create/', versiyonunu_goster, name='create'),
#
#
#
# ]
