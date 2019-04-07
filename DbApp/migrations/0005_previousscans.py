# Generated by Django 2.1 on 2019-01-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DbApp', '0004_delete_previousscans'),
    ]

    operations = [
        migrations.CreateModel(
            name='previousScans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='x', max_length=30)),
                ('dbid', models.CharField(max_length=100)),
                ('dbweight', models.IntegerField()),
                ('lastUsage', models.DateTimeField()),
            ],
        ),
    ]
