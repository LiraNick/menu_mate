

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

# pip install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Apenas para teste (será buscado direto do Banco de Dados)
info_banco_cliente={'nome':'luiz roberto', 
                    'cpf':'88899966652', 
                    'produtos':'refrigerante', 
                    'un':32, 'total':98.5 , 
                    'data':'02/03/2023',
                    'email': 'marcosilveira.game@gmail.com'}


# Função que irá enviar Nota fiscal via email
def envia_nf(documento, dados_cliente):
    """
    Envia email para o cliente (email está cadastrado no Banco de Dados)
    
    documento (pdf) - Caminho para do arquivo que será enviado
    dados_cliente - Dicionário contendo dados do Cliente.
                    Será utilizado para adicionar as informações do cliente no email
    """


    # Quem envia o email
    remetente = 'marcosilveira.lg@gmail.com'
    
    # Senha gerada pelo Google
    senha = 'cyznahdwxqeimfcv'

    # Quem irá receber o email (aluno contido no arquivo Excel)
    destinatario =  dados_cliente['email']
    
    # Criação do objeto "mensagem/email que será enviado"
    mensagem = MIMEMultipart()
    
    # Inserindo os parametros no objeto
    # Remetente , Destinatario , Titulo
    mensagem['from'] = remetente
    mensagem['to'] = destinatario
    mensagem['subject'] = f'Nota Fiscal Eletrônica - {dados_cliente["data"]}'
    
    # Inserindo Mensagem ao "corpo" do email
    mensagem.attach(MIMEText(
        f"""    Olá {dados_cliente['nome'].split()[0].title()}.\n 
        Segue em anexo sua Nota Fiscal Eletrônica""", 'plain'))
    
    # Anexo
    # Abrir documento 
    with open(documento, 'rb') as nf_anexo:
        conteudo = nf_anexo.read()
    
    # Cria o anexo do arquivo Word
    anexo = MIMEApplication(conteudo, _subtype='pdf')
    
    anexo.add_header('Content-Disposition', 'attachment', filename='nf_' + dados_cliente['nome'].replace(' ', '_').lower() + '.pdf')
    
    # Insere anexo ao objeto
    mensagem.attach(anexo)
    
    
    # Envio do EMAIL
    # Objeto responsável pela conexão com o servidor
    email = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Habilita a segurança
    email.starttls()
    
    # Login
    email.login(remetente, senha)
    
    # Envio do email
    email.sendmail(remetente, destinatario, mensagem.as_string())
    
    # Enserra a conexão com o servidor
    email.quit()
    

# Função que irá criar o arquivo PDF
def cria_nf(dados_cliente):
    """
    Cria o arquivo PDF (Nota Fiscal)
    
    dados_cliente  - Dicionário contendo dados do cliente contido no Banco de Dados
    """
    

    # Criar arquivo PDF
    # Nome do arquivo será o nome do cliente
    nf_pdf = canvas.Canvas(dados_cliente['nome'].replace(' ', '_').lower() + '.pdf'
                        , pagesize=letter)

    # Adicionar informações na "Nota Fiscal"
    nf_pdf.drawString(50, 700, f"Cliente: {dados_cliente['nome']}")
    nf_pdf.drawString(50, 685, f"CPF: {dados_cliente['cpf']}")
    nf_pdf.drawString(50, 670, f"Produto: {dados_cliente['produtos']}")
    nf_pdf.drawString(50, 655, f"Quantidade: {dados_cliente['un']}")
    nf_pdf.drawString(50, 640, f"Data: {dados_cliente['data']}")
    nf_pdf.drawString(50, 625, f"Email: {dados_cliente['email']}")
    nf_pdf.drawString(50, 610, f"Total: {dados_cliente['total']}")
    

    # Salva
    nf_pdf.save()
    
    # Caminho para acessar o arquivo PDF
    nf_pdf = dados_cliente['nome'].replace(' ', '_').lower() + '.pdf'
            
    # Chama a função que envia a Nota Fiscal por email
    envia_nf(nf_pdf, dados_cliente)
    

cria_nf(info_banco_cliente)
