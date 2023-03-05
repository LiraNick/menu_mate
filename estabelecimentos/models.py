from django.db import models



class Estabelecimento(models.Model):
    estabelecimento_id = models.AutoField(primary_key=True)
    estabelecimento_nome = models.CharField(max_length=100)
    estabelecimento_endereco = models.CharField(max_length=200)
    estabelecimento_telefone = models.CharField(max_length=20)

    class Meta:
        db_table = "estabelecimento"


class Mesa(models.Model):
    mesa_id = models.AutoField(primary_key=True)
    mesa_numero = models.IntegerField()
    mesa_capacidade = models.IntegerField()
    mesa_status = models.BooleanField(default=False)
    estabelecimento_id = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    class Meta:
        db_table = "mesa"


class Garcom(models.Model):
    garcom_id = models.AutoField(primary_key=True)
    garcom_nome = models.CharField(max_length=100)
    estabelecimento_id = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    class Meta:
        db_table = "garcom"


class Comanda(models.Model):
    comanda_id = models.AutoField(primary_key=True)
    mesa_id = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    garcom_id = models.ForeignKey(Garcom, on_delete=models.CASCADE)

    class Meta:
        db_table = "comanda"


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_nome = models.CharField(max_length=100)
    estabelecimento_id = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    class Meta:
        db_table = "menu"


class ItemMenu(models.Model):
    item_menu_id = models.AutoField(primary_key=True)
    item_menu_nome = models.CharField(max_length=100)
    item_menu_preco = models.DecimalField(max_digits=10, decimal_places=2)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = "itemmenu"


class ItemComanda(models.Model):
    item_comanda_id = models.AutoField(primary_key=True)
    item_comanda_quantidade = models.IntegerField()
    comanda_id = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)

    class Meta:
        db_table = "itemcomanda"


class Recibo(models.Model):
    recibo_id = models.AutoField(primary_key=True)
    recibo_subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    recibo_taxas = models.DecimalField(max_digits=10, decimal_places=2)
    recibo_total = models.DecimalField(max_digits=10, decimal_places=2)
    comanda_id = models.ForeignKey(Comanda, on_delete=models.CASCADE)

    class Meta:
        db_table = "recibo"


class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    reserva_reserva = models.DateTimeField()
    reserva_nome_cliente = models.CharField(max_length=100)
    mesa_id = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    class Meta:
        db_table = "reserva"