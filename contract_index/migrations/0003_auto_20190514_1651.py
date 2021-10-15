# Generated by Django 2.0.7 on 2019-05-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_index', '0002_index_localcompanies'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestrictLocalCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('local_company_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='index',
            name='contract_title',
            field=models.CharField(db_index=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='index',
            name='remarks',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]