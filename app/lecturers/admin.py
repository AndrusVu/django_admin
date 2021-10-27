from django import forms
from django.contrib import admin

from lecturers.models import Lecturer, Skill


class SkillInline(admin.TabularInline):
    model = Skill.lecturers.through

    # def get_queryset(self, request):
    #     return super().get_queryset(request)


class LecturerForm(forms.ModelForm):
    def clean_skills(self):
        cleaned_data = self.clean()
        skills = cleaned_data.get("skills")
        area = cleaned_data.get("area")
        if self.instance.id and not (skills & self.instance.area.skills.all()).exists():  # if lecturer exists
            self.add_error("skills", "These skills area not valid because it is from another area.")
        if not self.instance.id and area and not (skills & area.skills.all()).exists():  # if lecturer doesn't exist
            self.add_error("skills", "These skills area not valid because it is from another area.")
        return skills


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    form = LecturerForm
    list_display = ["full_name", "area", "modified"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["full_name", "area"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    add_fieldsets = [(None, {"fields": ["full_name", "area"]})]
    ordering = ["-modified"]
    # inlines = [SkillInline]

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return self.fieldsets

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return super().get_readonly_fields(request, obj) + ["area"]
    #
    #     return super().get_readonly_fields(request, obj)

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "skills":  # remove Skills from other Areas than area of Lecturer
    #         lecturer_id = request.resolver_match.kwargs.get("object_id")
    #         if lecturer_id:
    #             area = Lecturer.objects.get(id=lecturer_id).area
    #             kwargs["queryset"] = Skill.objects.filter(area=area)
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "area", "category", "modified"]
    list_filter = ["category"]
    readonly_fields = ["created", "modified"]
    fieldsets = [
        (None, {"fields": ["name", "area", "category"]}),
        ("System", {"classes": ["collapse"], "fields": ["created", "modified"]}),
    ]
    ordering = ["-modified"]
