"""Views for maintenance_notices."""

from nautobot.core.views import generic

from maintenance_notices import forms, models, tables

class MaintenanceNoticeListView(generic.ObjectListView):
    """List view."""

    queryset = models.MaintenanceNotice.objects.all()
    table = tables.MaintenanceNoticeTable
    action_buttons = ("add",)

class MaintenanceNoticeView(generic.ObjectView):
    """Detail view."""

    queryset = models.MaintenanceNotice.objects.all()


class MaintenanceNoticeCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()
    model_form = forms.MaintenanceNoticeForm


class MaintenanceNoticeDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()    