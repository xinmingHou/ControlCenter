# Generated by Django 2.1.7 on 2019-04-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm_template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('name_en', models.CharField(max_length=128)),
                ('pattern', models.CharField(choices=[('supervised', '监督学习'), ('semi_supervised', '半监督学习'), ('RF', '强化学习'), ('unsupervised', '无监督学习'), ('others', '其他')], default='监督学习', max_length=32)),
                ('template_file', models.FileField(upload_to='alg_tem_file')),
            ],
            options={
                'verbose_name': '算法',
                'verbose_name_plural': '算法',
                'ordering': ['-name'],
            },
        ),
    ]
