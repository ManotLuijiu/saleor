# Generated by Django 4.2.20 on 2025-04-23 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("channel", "0020_channel_use_legacy_line_voucher_propagation_for_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="channel",
            old_name="use_legacy_line_voucher_propagation_for_order",
            new_name="use_legacy_line_discount_propagation_for_order",
        ),
    ]
