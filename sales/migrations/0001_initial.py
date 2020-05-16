# Generated by Django 3.0.5 on 2020-05-11 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.CharField(editable=False, max_length=8, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='CASH', max_length=20)),
                ('customer_address', models.CharField(blank=True, max_length=30)),
                ('customer_phone', models.CharField(blank=True, max_length=10)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField()),
                ('last_bal', models.IntegerField(default=0)),
                ('p_and_f', models.FloatField(default=0)),
                ('round_off', models.FloatField(default=0.0)),
                ('total_amount', models.FloatField()),
                ('amount_paid', models.IntegerField(default=0)),
                ('current_bal', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField()),
                ('item_mrp', models.FloatField()),
                ('item_discount', models.FloatField(default=0)),
                ('item_sp', models.FloatField()),
                ('item_total', models.FloatField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Invoice')),
            ],
        ),
    ]
