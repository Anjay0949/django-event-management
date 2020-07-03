# Generated by Django 2.2.13 on 2020-07-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='agenda',
        ),
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='notification',
        ),
        migrations.AddField(
            model_name='event',
            name='job_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.JobCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='scheduled_status',
            field=models.CharField(choices=[('yet to scheduled', 'Yet to Scheduled'), ('scheduled', 'Scheduled')], max_length=25),
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_image/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=120)),
                ('speaker_name', models.CharField(max_length=120)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue_name', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]