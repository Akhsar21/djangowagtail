# Generated by Django 3.1.1 on 2020-10-27 17:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0014_auto_20201021_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingWorshipTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('worship_type', models.CharField(blank=True, choices=[('business', 'Business'), ('first_day', 'First day')], max_length=255, null=True)),
                ('worship_time', models.CharField(max_length=255)),
                ('meeting', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='worship_times', to='contact.meeting')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
