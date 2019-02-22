login = input("Login:")
senha = input("senha:")

print("o usuario digitado foi: %s, e a senha digitada foi: %s" % (login, senha))


if login == senha:
    print("usuario logado")
else:
    print("usuario invalido")

