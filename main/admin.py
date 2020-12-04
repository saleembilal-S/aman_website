from django.contrib import admin
from .models import CompanyInfo,CamerasInfo,UserInfo
# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(CamerasInfo)
admin.site.register(UserInfo)
