# Generated by Django 2.0.3 on 2018-04-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180403_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='odgovori',
            name='odgovor10',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor7',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor8',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='odgovori',
            name='odgovor9',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='odgovori',
            name='odgovor1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='odgovori',
            name='odgovor2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='odgovori',
            name='odgovor3',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]