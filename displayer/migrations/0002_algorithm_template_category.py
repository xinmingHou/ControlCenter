# Generated by Django 2.1.7 on 2019-04-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm_template',
            name='category',
            field=models.CharField(choices=[('classifier', '分类'), ('regression', '回归'), ('cluster', '聚类'), ('others', '其他')], default='分类', max_length=32),
        ),
    ]
