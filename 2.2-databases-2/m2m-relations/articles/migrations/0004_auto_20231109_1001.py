# Generated by Django 3.1.2 on 2023-11-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_auto_20231108_1656"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["published_at"],
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.AlterField(
            model_name="scope",
            name="tag_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
            ),
        ),
        migrations.AlterField(
            model_name="scope",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
            ),
        ),
    ]