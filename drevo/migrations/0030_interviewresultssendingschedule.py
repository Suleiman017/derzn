# Generated by Django 4.1.1 on 2022-12-23 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0029_alter_glossaryterm_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewResultsSendingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_sending', models.DateTimeField(auto_now_add=True, verbose_name='Дата возможной рассылки')),
                ('last_sending', models.DateTimeField(auto_now=True, verbose_name='Дата последней рассылки')),
                ('interview', models.ForeignKey(help_text='Выберите знание, вид которого "Интервью"', on_delete=django.db.models.deletion.CASCADE, related_name='sending_schedule', to='drevo.znanie', verbose_name='Интервью')),
            ],
            options={
                'verbose_name': 'Рассылка результатов интервью',
                'verbose_name_plural': 'Рассылки результатов интервью',
                'ordering': ['-next_sending'],
            },
        ),
    ]