# Generated by Django 5.0.1 on 2024-03-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceIt', '0004_field_expert_about_me_expert_rate_expert_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='about_me',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='expert',
            name='rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expert',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
