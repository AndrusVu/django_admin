from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.forms import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from formtools.wizard.views import SessionWizardView

from events.models import Event


class EventFormFirst(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "thumbnail_url", "area"]


class EventFormSecond(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["lectures", "start_datetime"]


# context = {
#     "title": _("Add %s") % force_unicode(opts.verbose_name),
#     "adminform": adminForm,
#     "is_popup": request.REQUEST.has_key("_popup"),
#     "show_delete": False,
#     "media": mark_safe(media),
#     "inline_admin_formsets": inline_admin_formsets,
#     "errors": helpers.AdminErrorList(form, formsets),
#     "root_path": self.admin_site.root_path,
#     "app_label": opts.app_label,
# }


class EventWizardView(SessionWizardView):
    # template_name = "event_add_form.html"

    def done(self, form_list, **kwargs):
        # TODO something
        # return render(self.request, "event_add_form.html", {"form_data": [form.cleaned_data for form in form_list]})
        return redirect("/admin/events/event/")  # or return HttpResponseRedirect('/page-to-redirect-to-when-done/')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail_url", "modified"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["title", "description", "thumbnail_url"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-modified"]
    # add_form_template = "event_add_form.html"

    def get_urls(self):
        urls = super().get_urls()
        view = EventWizardView.as_view([EventFormFirst, EventFormSecond])
        custom_urls = [url(r"^add/$", self.admin_site.admin_view(view), name="event-report")]
        return custom_urls + urls


# admin.site.register(Event)
