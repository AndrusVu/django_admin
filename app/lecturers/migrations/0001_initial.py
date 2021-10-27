# Generated by Django 3.2.8 on 2021-10-27 06:23
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True
    dependencies = [("areas", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True, db_index=True)),
                ("name", models.CharField(max_length=64, unique=True, verbose_name="Name")),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("programming_language", "Programming Language"),
                            ("database", "Database"),
                            ("cloud_technology", "Cloud Technology"),
                            ("testing_tool", "Testing Tool"),
                            ("frameworks", "Frameworks"),
                            ("other", "Other"),
                        ],
                        db_index=True,
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="Category",
                    ),
                ),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="skills", to="areas.area"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Skills", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Lecturer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True, db_index=True)),
                ("full_name", models.CharField(max_length=128, verbose_name="Full Name")),
                ("area", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="areas.area")),
                (
                    "skills",
                    models.ManyToManyField(
                        blank=True, related_name="lecturers", to="lecturers.Skill", verbose_name="Lecturer Skills"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Lecturers", "ordering": ["full_name"]},
        ),
    ]
