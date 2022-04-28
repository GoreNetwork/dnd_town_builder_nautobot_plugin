"""Forms for maintenance_notices."""
from django import forms
from nautobot.utilities.forms import (
    BootstrapMixin,
)

from maintenance_notices import models

class MaintenanceNoticeForm(BootstrapMixin, forms.ModelForm):
    """MaintenanceNotice creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.MaintenanceNotice
        fields = ("__all__")