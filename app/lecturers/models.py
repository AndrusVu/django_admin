from django.db import models
from model_utils.choices import Choices

from areas.models import Area
from core.models import BaseModel


CATEGORY = Choices(
    ("programming_language", "Programming Language"),
    ("database", "Database"),
    ("cloud_technology", "Cloud Technology"),
    ("testing_tool", "Testing Tool"),
    ("frameworks", "Frameworks"),
    ("other", "Other"),
)


class Skill(BaseModel):
    name = models.CharField("Name", max_length=64, unique=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name="skills")
    category = models.CharField(
        "Category", max_length=32, null=True, blank=True, default=None, choices=CATEGORY, db_index=True
    )

    class Meta:
        app_label = "lecturers"
        verbose_name_plural = "Skills"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} (skill {self.id})"


class Lecturer(BaseModel):
    full_name = models.CharField("Full Name", max_length=128)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    skills = models.ManyToManyField(Skill, blank=True, verbose_name="Lecturer Skills", related_name="lecturers")

    class Meta:
        app_label = "lecturers"
        verbose_name_plural = "Lecturers"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} (lecturer {self.id})"
