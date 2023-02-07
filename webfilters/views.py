from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import WebFilter
from custom_accounts.models import Organization


def get_webfilter(request, uuid):
    print(uuid)
    try:
        organization = Organization.objects.get(uuid=uuid)
        webfilters = WebFilter.objects.filter(organization=organization)
        alldomains = ''
        for filter in webfilters:
            alldomains += filter.domains
            alldomains += '\n'
    except ObjectDoesNotExist:
        alldomains = ''

    return HttpResponse(alldomains, content_type='text/plain')




