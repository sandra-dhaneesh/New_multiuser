# Generated by Django 4.2.3 on 2024-02-04 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BillSoftwareapp', '0005_debitnotetransactionhistory_modules_list_party_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('account_num', models.PositiveBigIntegerField(null=True)),
                ('ifsc', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
                ('upi_id', models.CharField(max_length=255)),
                ('as_of_date', models.DateField(null=True)),
                ('card_type', models.CharField(max_length=255)),
                ('open_balance', models.BigIntegerField(null=True)),
                ('current_balance', models.BigIntegerField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BillSoftwareapp.company')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
