# Generated by Django 3.2.4 on 2021-06-20 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210620_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
