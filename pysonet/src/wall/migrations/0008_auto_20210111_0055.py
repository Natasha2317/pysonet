# Generated by Django 3.1.4 on 2021-01-10 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0007_auto_20210108_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='idtechnology',
            field=models.CharField(choices=[('php', 'php'), ('angular', 'angular'), ('js', 'js'), ('python', 'python'), ('django', 'django'), ('perl', 'perl')], default='django', max_length=100, verbose_name='Технология'),
        ),
    ]
