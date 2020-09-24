from django.contrib import admin
from .models import Faq,NigerianCases,GlobalCases

# Register your models here.


class faqAdmin(admin.ModelAdmin):
    list_display = ('title','body','created_at')


class casesAdmin(admin.ModelAdmin):
    list_display = ('states','total_cases','active_cases','discharged','death_cases')


class globalCasesAdmin(admin.ModelAdmin):
    list_display = ('country','country_total_cases','country_recovery','country_total_deaths')


admin.site.register(GlobalCases, globalCasesAdmin)
admin.site.register(Faq, faqAdmin)
admin.site.register(NigerianCases, casesAdmin)

