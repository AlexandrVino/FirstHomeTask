from django.urls import path

from catalog.views import item_detail, item_list

urlpatterns = [
    path('', item_list, name='catalog'),
    path('<int:item_index>/', item_detail),
]
