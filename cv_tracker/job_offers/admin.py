from django.contrib import admin
from .models import JobOffer

@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'posted_at', 'created_at')
    search_fields = ('title', 'company_name', 'location')
    list_filter = ('posted_at', 'created_at')
    ordering = ('-created_at',)
