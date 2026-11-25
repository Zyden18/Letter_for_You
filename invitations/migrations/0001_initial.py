from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="DateResponse",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("answer", models.CharField(choices=[("yes", "Yes"), ("maybe_later", "Maybe another time")], max_length=20)),
                ("ideas", models.JSONField(blank=True, default=list)),
                ("custom_idea", models.CharField(blank=True, max_length=100)),
                ("preferred_day", models.DateField(blank=True, null=True)),
                ("preferred_time", models.TimeField(blank=True, null=True)),
                ("note", models.CharField(blank=True, max_length=240)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name": "date response", "verbose_name_plural": "date responses", "ordering": ["-created_at"]},
        ),
    ]
