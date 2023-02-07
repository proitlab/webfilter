import uuid
from django.db import models
from crum import get_current_user
from custom_accounts.models import User, Organization
from django.utils.translation import gettext as _

# Create your models here.

class WebFilter(models.Model):
    name = models.CharField(_('Name'), max_length=50, unique=True)
    domains = models.TextField(_('Domain List'))

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_('User'),
        blank=True,
        null=True
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        verbose_name=_('Organization'),
        blank=True,
        null=True
    )
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        db_table = 'webfilter'
        verbose_name = 'Web Filter'
        verbose_name_plural = 'Web Filters'


    def __str__(self):
        return '{}'.format(self.name)

    def save(self):
        if self.user is None:
            current_user = get_current_user()
            self.user = current_user
            self.organization = current_user.organization

        return super(WebFilter, self).save()

