# Generated by Django 4.2.1 on 2023-05-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0002_invoice_line_five_total_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='line_five_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_four_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_three_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Line Total (D)'),
        ),
    ]
