# Generated by Django 4.0.3 on 2022-08-19 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('work_list', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='collaborator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collabo.project')),
            ],
        ),
    ]
