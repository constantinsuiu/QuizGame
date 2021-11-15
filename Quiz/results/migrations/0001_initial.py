# Generated by Django 3.2.9 on 2021-11-14 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.answer')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.question')),
            ],
            options={
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('profit', models.FloatField(default=0.0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
            ],
            options={
                'verbose_name_plural': 'Finances',
            },
        ),
    ]
