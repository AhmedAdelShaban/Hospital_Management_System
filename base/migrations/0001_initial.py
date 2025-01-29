# Generated by Django 4.2.2 on 2025-01-29 18:38

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("appointment_date", models.DateTimeField(blank=True, null=True)),
                ("issues", models.TextField(blank=True, null=True)),
                ("symptoms", models.TextField(blank=True, null=True)),
                (
                    "appointment_id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890", length=6, max_length=10, prefix=""
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Scheduled", "Scheduled"),
                            ("Completed", "Completed"),
                            ("Pending", "Pending"),
                            ("Cancelled", "Cancelled"),
                        ],
                        max_length=120,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.FileField(blank=True, null=True, upload_to="images")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("medications", models.TextField(blank=True, null=True)),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.appointment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("diagnosis", models.TextField()),
                ("treatment", models.TextField()),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.appointment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LabTest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("test_name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("result", models.TextField(blank=True, null=True)),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.appointment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Billing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sub_total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("tax", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[("Paid", "Paid"), ("Unpaid", "Unpaid")], max_length=120
                    ),
                ),
                (
                    "billing_id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890", length=6, max_length=10, prefix=""
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "appointment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="billing",
                        to="base.appointment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="service",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="service_appointments",
                to="base.service",
            ),
        ),
    ]
