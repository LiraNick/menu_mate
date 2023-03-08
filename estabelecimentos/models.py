from django.db import models



"""
CREATE TABLE "Usuario"(
    "usu_id" BIGINT NOT NULL,
    "usu_nome" VARCHAR(255) NOT NULL,
    "usu_cfp" VARCHAR(255) NOT NULL,
    "usu_telefone" BIGINT NOT NULL,
    "usu_email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Usuario" ADD PRIMARY KEY("usu_id");
"""
class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nome = models.CharField(max_length=100)
    usu_cpf = models.CharField(max_length=14)
    usu_telefone = models.CharField(max_length=15)
    usu_email = models.CharField(max_length=100)

    class Meta:
        db_table = "usuario"


"""
CREATE TABLE "Garcom"(
    "gar_id" BIGINT NOT NULL,
    "gar_nome" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Garcom" ADD PRIMARY KEY("gar_id");
"""
class Garcom(models.Model):
    gar_id = models.AutoField(primary_key=True)
    gar_nome = models.CharField(max_length=100)

    class Meta:
        db_table = "garcom"


"""
CREATE TABLE "Mesas"(
    "mes_id" BIGINT NOT NULL,
    "mes_numero" BIGINT NOT NULL,
    "mes_capacidade" BIGINT NOT NULL,
    "mes_status" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Mesas" ADD PRIMARY KEY("mes_id");
"""
class Mesa(models.Model):
    mes_id = models.AutoField(primary_key=True)
    mes_numero = models.IntegerField()
    mes_capacidade = models.IntegerField()
    mes_status = models.CharField(max_length=10)

    class Meta:
        db_table = "mesa"


"""
CREATE TABLE "Categoria"(
    "cat_id" BIGINT NOT NULL,
    "cat_nome" VARCHAR(255) NOT NULL,
);
ALTER TABLE
    "Categoria" ADD PRIMARY KEY("cat_id");
"""
class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nome = models.CharField(max_length=50)

    class Meta:
        db_table = "categoria"


"""
CREATE TABLE "Cardapio"(
    "car_id" BIGINT NOT NULL,
    "car_item" BIGINT NOT NULL,
    "car_descricao" VARCHAR(255) NOT NULL,
    "car_preco" DOUBLE PRECISION NOT NULL,
    "cat_id" BIGINT NOT NULL
);
ALTER TABLE
    "Cardapio" ADD PRIMARY KEY("car_id");
"""
class Cardapio(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_item = models.CharField(max_length=50)
    car_descricao = models.CharField(max_length=100)
    car_preco = models.DecimalField(max_digits=10, decimal_places=2)
    cat_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        db_table = "menu"


"""
CREATE TABLE "Comanda"(
    "com_id" BIGINT NOT NULL,
    "usu_id" BIGINT NOT NULL,
    "mes_id" BIGINT NOT NULL,
    "gar_id" BIGINT NOT NULL,
    "car_id" BIGINT NOT NULL,
    "car_data" DATE NOT NULL
);
ALTER TABLE
    "Comanda" ADD PRIMARY KEY("com_id");
"""
class Comanda(models.Model):
    com_id = models.AutoField(primary_key=True)
    usu_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mes_id = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    gar_id = models.ForeignKey(Garcom, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    com_data = models.DateTimeField()

    class Meta:
        db_table = "comanda"



