# Generated by Django 2.0.3 on 2018-04-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='date received')),
                ('amount', models.FloatField(default=0)),
                ('source', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='date of receipt')),
                ('amount', models.FloatField(default=0)),
                ('category', models.CharField(max_length=300)),
            ],
        ),
    ]
