# Generated by Django 5.0.1 on 2024-03-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceIt', '0007_alter_expert_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='C:/Users/mosta/Desktop/Desktop/Mostafa Azouz/Queen mary/Ace-It!/Code/frontend/src/assets/Expert_imgs'),
        ),
    ]
