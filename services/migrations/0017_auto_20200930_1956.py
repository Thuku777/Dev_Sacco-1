# Generated by Django 3.1 on 2020-09-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20200930_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='count_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='count_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='count_3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='count_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='fact_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='fact_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='fact_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='fact_4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
