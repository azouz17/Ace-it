# Generated by Django 5.0.1 on 2024-03-13 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AceIt', '0003_expert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='expert',
            name='about_me',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='expert',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AceIt.field'),
        ),
    ]
