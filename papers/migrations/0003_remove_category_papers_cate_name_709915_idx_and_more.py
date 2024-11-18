# Generated by Django 5.1.3 on 2024-11-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("papers", "0002_alter_papers_author"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="category",
            name="papers_cate_name_709915_idx",
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]