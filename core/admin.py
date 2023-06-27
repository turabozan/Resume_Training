from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.site_header = 'CV Administration'
@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameter', 'updated_date','created_date']
    search_fields = ['name','description','parameter']
    list_editable = ['parameter']
    #readonly_fields = []
    class Meta:
        model = GeneralSetting

@admin.register(ImageSetting)
class ImageSetting(admin.ModelAdmin):
    list_display = ['id','name','description','file', 'updated_date','created_date']
    search_fields = ['name','description','file']
    list_editable = ['file']
    #readonly_fields = []
    class Meta:
        model = ImageSetting

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ['id','order','name','percentage', 'updated_date','created_date']
    search_fields = ['name']
    list_editable = ['order','name','percentage',]
    #readonly_fields = []
    class Meta:
        model = Skill

@admin.register(Experience)
class Experience(admin.ModelAdmin):
    list_display = ['id','company_name','job_title','job_location','start_date','end_date', 'updated_date','created_date']
    search_fields = ['company_name','job_title','job_location']
    list_editable = ['company_name','job_title','start_date','end_date']
    #readonly_fields = []
    class Meta:
        model = Experience

@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = ['id','school_name','major','department','start_date','end_date', 'updated_date','created_date']
    search_fields = ['school_name','major','department',]
    list_editable = ['school_name','major','department','start_date','end_date']
    #readonly_fields = []
    class Meta:
        model = Education