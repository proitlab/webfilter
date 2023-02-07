import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
'''
from wagtail.admin.panels import FieldPanel, InlinePanel, \
    FieldRowPanel, MultiFieldPanel, HelpPanel, TabbedInterface
'''

'''
class Status(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return '%s' % self.name
'''


class Organization(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)
    is_no_org = models.BooleanField(default=False)
    start = models.TimeField(default='08:00')
    end = models.TimeField(default='17:00')
    address = models.TextField('Address', blank=True, null=True)
    additional_info = models.TextField('More Info', blank=True, null=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)

    '''
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldRowPanel([FieldPanel('start'), FieldPanel('end')], heading='Jam Operasional'),
            FieldPanel('address'),
            FieldPanel('additional_info')
        ])

    ]
    '''

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'organization'
        verbose_name = _('Organization')
        verbose_name_plural = _('Organizations')

    def __str__(self):
        return '%s' % self.name


class User(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        verbose_name=_('Organization'),
        blank=True,
        null=True,
    )
