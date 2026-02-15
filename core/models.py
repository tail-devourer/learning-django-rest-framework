from django.db import models
from django.utils.translation import gettext_lazy as _


class TodoModel(models.Model):
    name = models.CharField(_('Name'), max_length=256)
    description = models.TextField(_('Description'), max_length=65535, blank=True, null=True)
    due = models.DateField(_('Due Date'), blank=True, null=True)
