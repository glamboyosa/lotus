# Generated by Django 4.0.5 on 2022-09-18 22:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0011_alter_billingplan_billing_plan_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billablemetric",
            name="aggregation_type",
            field=models.CharField(
                choices=[
                    ("count", "Count"),
                    ("sum", "Sum"),
                    ("max", "Max"),
                    ("unique", "Unique"),
                ],
                default="count",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="billingplan",
            name="billing_plan_id",
            field=models.CharField(
                default=uuid.UUID("074476dd-6bc4-4724-ba8a-055e2c24a400"),
                max_length=255,
                unique=True,
            ),
        ),
    ]
