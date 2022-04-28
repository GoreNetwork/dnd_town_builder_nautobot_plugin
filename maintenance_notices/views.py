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


class MaintenanceNoticeEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()
    model_form = forms.MaintenanceNoticeForm

class MaintenanceNoticeCreateView(MaintenanceNoticeEditView):
    """Create view."""

    def alter_obj(self, obj, request, *args, **kwargs):
        """Insert user into object."""
        obj.created_by = request.user
        return obj
class MaintenanceNoticeDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.MaintenanceNotice
    queryset = models.MaintenanceNotice.objects.all()    