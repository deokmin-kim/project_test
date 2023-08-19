# Generated by Django 4.2.4 on 2023-08-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.EmailField(max_length=254, verbose_name="이메일")),
                ("password", models.CharField(max_length=64, verbose_name="비밀번호")),
                (
                    "created_dt",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록날짜"),
                ),
            ],
            options={
                "verbose_name": "고객",
                "verbose_name_plural": "고객",
                "db_table": "my_user",
            },
        ),
    ]