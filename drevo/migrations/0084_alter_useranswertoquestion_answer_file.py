# Generated by Django 3.2.4 on 2023-10-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0083_merge_20231027_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswertoquestion',
            name='answer_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='proof/', verbose_name='Файл'),
        ),
    ]