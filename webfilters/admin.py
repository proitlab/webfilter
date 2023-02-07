from django.contrib import admin
from crum import get_current_user
from .models import WebFilter
# Register your models here.


class WebFilterAdmin(admin.ModelAdmin):
    exclude = ['user', 'organization']
    list_display = ['name', 'domains', 'uuid']

    def get_queryset(self, request):
        user = get_current_user()
        if user.is_superuser:
            qs = WebFilter.objects.all()
        else:
            if user.organization:
                qs = WebFilter.objects.filter(organization=user.organization)
            else:
                qs = WebFilter.objects.filter(user=user)

        return qs



admin.site.register(WebFilter, WebFilterAdmin)

