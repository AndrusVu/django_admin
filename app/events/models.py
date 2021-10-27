from django.db import models

from areas.models import Area
from core.models import BaseModel
from lecturers.models import Lecturer


class Event(BaseModel):
    title = models.CharField("Title", max_length=256)
    description = models.TextField("Description")
    thumbnail_url = models.URLField("Thumbnail URL")
    start_datetime = models.DateTimeField("Start Date & Time", db_index=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Area")
    lectures = models.ManyToManyField(Lecturer, verbose_name="Event Authors")

    class Meta:
        app_label = "events"
        verbose_name_plural = "Events"
        ordering = ["-modified"]

    def __str__(self) -> str:
        return f"{self.title} (event {self.id})"
