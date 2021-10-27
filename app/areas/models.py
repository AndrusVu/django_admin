from django.db import models

from core.models import BaseModel


class Area(BaseModel):
    title = models.CharField("Title", max_length=64, unique=True)
    description = models.TextField("Description", blank=True, null=False)
    thumbnail_url = models.URLField("Thumbnail URL", blank=True, null=False)

    class Meta:
        app_label = "areas"
        verbose_name_plural = "Areas"
        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.title} (area {self.id})"
