# Generated by Django 3.2.4 on 2022-12-21 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_ratings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'verbose_name_plural': 'Orders Placed'},
        ),
        migrations.AlterField(
            model_name='ratings',
            name='rating',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('EL', 'Electronics'), ('HE', 'Hearing and Music'), ('WA', 'Watches'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('BP', 'Beauty Products'), ('FW', 'Footwear'), ('KW', 'Kids Wear'), ('KC', 'Knitted Clothes'), ('FR', 'Frozen and Chilled'), ('B', 'Bakery'), ('CA', 'Car Accessories'), ('RF', 'Restaurant Food'), ('GR', 'Groceries'), ('BK', 'Bakeries'), ('RF', 'Restaurant Food'), ('KS', 'Kashmiri Spices'), ('RP', 'Rice and Pulses'), ('DF', 'Dry Fruits')], max_length=5),
        ),
    ]
