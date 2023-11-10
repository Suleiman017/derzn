# Generated by Django 3.2.4 on 2023-11-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0087_merge_0084_auto_20231029_1649_0086_auto_20231101_0247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glossarycategories',
            options={'ordering': ('order',), 'verbose_name': 'Категорию терминов глоссария', 'verbose_name_plural': 'Категорий терминов глоссария'},
        ),
        migrations.AlterField(
            model_name='suggestiontype',
            name='weight',
            field=models.IntegerField(blank=True, default=100, primary_key=True, serialize=False, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='tz',
            name='available_suggestion_types',
            field=models.ManyToManyField(blank=True, to='drevo.SuggestionType', verbose_name='Виды предложений'),
        ),
    ]