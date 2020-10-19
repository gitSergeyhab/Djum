from django.contrib import admin

# Register your models here.
from .models import Specialty, Company, Vacancy, Application, UserResume


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'level', 'specialty', 'company', 'salary_min', 'salary_max', 'published_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'specialty', 'company', 'published_at']
    list_filter = ['level', 'specialty', 'company']


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'code', 'slug']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('code',)}


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'owner', 'employee_count']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'location', 'employee_count']


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['written_username', 'written_phone', 'vacancy', 'user']
    list_display_links = ['user']
    search_fields = ['written_username']
    list_filter = ['vacancy']


class UserResumeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'readiness', 'salary', 'specialty',
                    'level', 'education', 'user']
    list_display_links = ['user']


admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(UserResume, UserResumeAdmin)
