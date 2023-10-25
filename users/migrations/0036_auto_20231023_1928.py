# Generated by Django 3.2.4 on 2023-10-23 16:28

from django.db import migrations


def migrate_data(apps, schema_editor):

    """
        Перевод данных таблиц users.UserSuggection и users.SuggestionType
        таблицы drevo.Suggestion и drevo.SuggestionType
    """

    drevo_suggestion = apps.get_model('drevo', 'Suggestion')
    users_suggestion = apps.get_model('users', 'UserSuggection')
    drevo_type = apps.get_model('drevo', 'SuggestionType')
    users_type = apps.get_model('users', 'SuggestionType')

    # Перенос данных из users.SuggestionType в drevo.SuggestionType
    for i in users_type.objects.all():
        drevo_type.objects.create(type_name=i.type_name, weight=i.type_name)

    # Перенос данных из users.UserSuggestion в drevo.Suggestion
    for i in users_suggestion.objects.all():
        drevo_suggestion.objects.create(
            parent_knowlege=i.parent_knowlege,
            name=i.name,
            user=i.user,
            suggestion_type=drevo_type.objects.get(weight=i.suggestion_type.weight),  # weight - поле уникальное
            expert=i.expert,
            is_approve=i.is_approve,
            check_date=i.check_date,
            create_date=i.create_date
        )


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_auto_20231018_2153'),
        ('drevo', '0080_suggestion_suggestiontype')
    ]

    operations = [
        migrations.RunPython(migrate_data)
    ]
