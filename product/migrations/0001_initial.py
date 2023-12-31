# Generated by Django 4.2.4 on 2023-08-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="상품명")),
                ("price", models.IntegerField(verbose_name="상품가격")),
                ("description", models.TextField(verbose_name="상품설명")),
                ("stock", models.IntegerField(verbose_name="재고")),
                (
                    "created_dt",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록날짜"),
                ),
            ],
            options={
                "verbose_name": "상품",
                "verbose_name_plural": "상품",
                "db_table": "my_product",
            },
        ),
    ]
