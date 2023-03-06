# Generated by Django 4.1.7 on 2023-03-06 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comanda',
            fields=[
                ('comanda_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'comanda',
            },
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('estabelecimento_id', models.AutoField(primary_key=True, serialize=False)),
                ('estabelecimento_nome', models.CharField(max_length=100)),
                ('estabelecimento_endereco', models.CharField(max_length=200)),
                ('estabelecimento_telefone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'estabelecimento',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('mesa_id', models.AutoField(primary_key=True, serialize=False)),
                ('mesa_numero', models.IntegerField()),
                ('mesa_capacidade', models.IntegerField()),
                ('mesa_status', models.BooleanField(default=False)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.estabelecimento')),
            ],
            options={
                'db_table': 'mesa',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reserva_id', models.AutoField(primary_key=True, serialize=False)),
                ('reserva_reserva', models.DateTimeField()),
                ('reserva_nome_cliente', models.CharField(max_length=100)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.mesa')),
            ],
            options={
                'db_table': 'reserva',
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('recibo_id', models.AutoField(primary_key=True, serialize=False)),
                ('recibo_subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recibo_taxas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recibo_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.comanda')),
            ],
            options={
                'db_table': 'recibo',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_nome', models.CharField(max_length=100)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.estabelecimento')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('item_menu_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_menu_nome', models.CharField(max_length=100)),
                ('item_menu_preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_menu_categoria', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.menu')),
            ],
            options={
                'db_table': 'itemmenu',
            },
        ),
        migrations.CreateModel(
            name='ItemComanda',
            fields=[
                ('item_comanda_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_comanda_quantidade', models.IntegerField()),
                ('comanda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.comanda')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.itemmenu')),
            ],
            options={
                'db_table': 'itemcomanda',
            },
        ),
        migrations.CreateModel(
            name='Garcom',
            fields=[
                ('garcom_id', models.AutoField(primary_key=True, serialize=False)),
                ('garcom_nome', models.CharField(max_length=100)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.estabelecimento')),
            ],
            options={
                'db_table': 'garcom',
            },
        ),
        migrations.AddField(
            model_name='comanda',
            name='garcom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.garcom'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='mesa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estabelecimentos.mesa'),
        ),
    ]
