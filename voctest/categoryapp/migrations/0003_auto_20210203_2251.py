# Generated by Django 3.1.5 on 2021-02-03 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocapp', '0004_remove_voclist_category_num'),
        ('categoryapp', '0002_auto_20210203_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylist',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voclist', to='vocapp.voclist'),
        ),
    ]
