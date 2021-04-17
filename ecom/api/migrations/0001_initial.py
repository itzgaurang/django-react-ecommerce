from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="gaurang", email="gaurang.shukla@yahoo.com",
                          is_staff=True, is_superuser=True, gender="Male")

        user.set_password("Password#9161")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
