# Generated by Django 5.0.3 on 2024-06-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_remove_card_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='censored_number',
            field=models.CharField(default='default string', editable=False, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='000000******0000'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='ccv',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]