# Generated by Django 5.0.6 on 2024-07-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ulist', '0007_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='votes_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
