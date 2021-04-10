# Generated by Django 3.1.7 on 2021-03-27 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('magnitude', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.magnitude')),
            ],
        ),
    ]
