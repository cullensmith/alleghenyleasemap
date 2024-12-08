# Generated by Django 4.2.13 on 2024-12-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasemap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolygonShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField()),
                ('geomjson', models.CharField()),
            ],
            options={
                'db_table': 'allegheny_polys',
                'managed': False,
            },
        ),
    ]
