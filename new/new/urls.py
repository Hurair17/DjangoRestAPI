"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
# from api.views import FileView
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('person/<int:cnic>',views.person_detail),
    # path('person/', views.PersonDetail.as_view()),
    # path('vehicle/<int:cnic_id>',views.vehicle_detail),
    # path('vehicle/',views.all_vehicle),
    # path('upload/', FileView.as_view()),
    path('api/image/', views.ImageView.as_view()),
    path('api/vehicle/', views.VehicleDetail.as_view()),
    # path('api/vehicle/number/', views.SelectedVehicleDetail.as_view()),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

