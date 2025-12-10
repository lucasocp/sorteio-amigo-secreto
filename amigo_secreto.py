import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==============================
# 1. LISTA DE PARTICIPANTES
# Formato: "Nome": "email"
# ==============================
participantes = {
    "Pessoa 1": "pessoa1@gmail.com",
    "Pessoa 2": "pessoa2@gmail.com",
    "Pessoa 3": "pessoa3@gmail.com",
    "Pessoa 4": "pessoa4@gmail.com",
    "Pessoa 5": "pessoa5@gmail.com",
    "Pessoa 6": "pessoa6@gmail.com",
    "Pessoa 7": "pessoa7@gmail.com",
    "Pessoa 8": "pessoa8@gmail.com",
    "Pessoa 9": "pessoa9@gmail.com",
    "Pessoa 10":"pessoa10@gmail.com",
}

# ==============================
# 2. FUNÇÃO DE SORTEIO
# ==============================
def sortear(participantes):
    nomes = list(participantes.keys())
    sorteados = nomes[:]
    random.shuffle(sorteados)

    # evitar pessoa tirar ela mesma
    for i in range(len(nomes)):
        if nomes[i] == sorteados[i]:
            return sortear(participantes)  # refaz o sorteio

    return dict(zip(nomes, sorteados))


# ==============================
# 3. FUNÇÃO PARA ENVIAR E-MAIL
# ==============================
def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(mensagem, "plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
        servidor.quit()
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar para {destinatario}: {e}")

# ==============================
# 4. EXECUTANDO O SORTEIO E ENVIO
# ==============================
pares = sortear(participantes)

print("\n--- Resultado do sorteio ---")
for pessoa, amigo in pares.items():
    print(f"{pessoa} tirou {amigo}")

print("\n--- Enviando e-mails ---")

email_origem = "emailorigem@gmail.com"
senha = "SUA_SENHA_DE_APP"  # para Gmail, use senha de app -> Vá em: Conta Google → Segurança → Verificação em duas etapas → Senhas de app

for pessoa, amigo in pares.items():
    destino = participantes[pessoa]
    mensagem = f"Olá {pessoa}!\n\nSeu amigo secreto é: **{amigo}**.\n\nBoas festas!"
    enviar_email(email_origem, senha, destino, "Seu Amigo Secreto 🎁", mensagem)