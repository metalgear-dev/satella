# Generated by Django 2.1 on 2018-09-03 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_title', models.CharField(max_length=200)),
                ('signing_target_kou', models.CharField(max_length=200)),
                ('signing_target_otsu', models.CharField(max_length=2000)),
                ('signing_date_disp', models.CharField(blank=True, max_length=200, null=True)),
                ('signing_date', models.DateField(blank=True, null=True)),
                ('expiration_date_disp', models.CharField(blank=True, max_length=200, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('auto_update', models.NullBooleanField()),
                ('file_name', models.CharField(blank=True, max_length=200, null=True)),
                ('pdf_path', models.CharField(max_length=2000)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('hidden_flag', models.BooleanField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('deleted_flag', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IndexLocalCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index', to='contract_index.Index')),
            ],
        ),
        migrations.CreateModel(
            name='LocalCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_company_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='indexlocalcompany',
            name='local_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='local_company', to='contract_index.LocalCompany'),
        ),
    ]