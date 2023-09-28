from django.urls import path
from Admin import views

app_name="webadmin"

urlpatterns = [
    path('dis/', views.district,name='district'),
    path('cat/',views.category),
    path('sub/',views.subcategory),
    path('pl/',views.place),
    path('areg/',views.adminregister),
    path('districtd/<int:did>',views.districtd,name="districtd"),
    path('editdist/<int:did>',views.editdis,name="editdis")
]