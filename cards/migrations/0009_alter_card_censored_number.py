# Generated by Django 5.0.3 on 2024-06-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_alter_card_censored_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='censored_number',
            field=models.CharField(default=True, editable=False, max_length=16),
        ),
    ]
