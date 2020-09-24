from django.contrib import admin
from . models import Donors,Beneficiary
# Register your models here.

class DonorAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email','blood_group','address1')
admin.site.register(Donors, DonorAdmin)


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('benefactor','title','body','created')
admin.site.register(Beneficiary, BeneficiaryAdmin)

