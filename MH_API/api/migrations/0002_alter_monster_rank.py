# Generated by Django 4.2.5 on 2023-09-18 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='rank',
            field=models.CharField(choices=[('9', 'Hunter Rank 9'), ('8', 'Hunter Rank 8'), ('7', 'Hunter Rank 7'), ('6', 'Hunter Rank 6'), ('5', 'Hunter Rank 5'), ('4', 'Hunter Rank 4'), ('3', 'Hunter Rank 3'), ('2', 'Hunter Rank 2'), ('1', 'Hunter Rank 1')], max_length=1),
        ),
    ]
