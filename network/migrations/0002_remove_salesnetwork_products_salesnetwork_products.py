# Generated by Django 5.1.5 on 2025-01-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salesnetwork",
            name="products",
        ),
        migrations.AddField(
            model_name="salesnetwork",
            name="products",
            field=models.ManyToManyField(
                blank="True", null="True", to="network.product", verbose_name="Продукты"
            ),
            preserve_default="True",
        ),
    ]
