from django.contrib import admin

# Register your models here.


from web_models import models

admin.site.register(models.Asset)
admin.site.register(models.IDC)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Tag)
admin.site.register(models.Contract)
admin.site.register(models.UserType)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)
admin.site.register(models.Status)
admin.site.register(models.DeviceType)
admin.site.register(models.HandleLog)


admin.site.register(models.Server)
admin.site.register(models.AdminInfo)

admin.site.register(models.NIC)
admin.site.register(models.Disk)
admin.site.register(models.Memory)