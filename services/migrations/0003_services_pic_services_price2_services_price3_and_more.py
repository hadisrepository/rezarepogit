# Generated by Django 4.1 on 2022-12-22 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_services_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='pic',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='price2',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='services',
            name='price3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='services',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='services',
            name='status',
            field=models.CharField(choices=[('pub', 'done'), ('drf', 'register')], max_length=3),
        ),
        migrations.AlterField(
            model_name='services',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
