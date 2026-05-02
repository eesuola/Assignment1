from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.CharField(blank=True, null=True),
        ),
    ]
