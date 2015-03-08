from django.contrib import admin
from communityfund.apps.home.models import Project, Community

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'initiator', 'percent_funded')

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass