# Generated by Django 5.0.1 on 2024-03-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceIt', '0009_alter_expert_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
