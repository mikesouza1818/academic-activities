# Exercício: Sistema de Login Simples

# Informações de login predefinidas
usuario_correto = "Maycon"
senha_correta = "3856"

# Solicitar ao usuário que insira nome de usuário e senha
usuario_input = input("Digite o nome de usuário: ")
senha_input = input("Digite a senha: ")

# Verificar se as informações de login estão corretas
if usuario_input == usuario_correto and senha_input == senha_correta:
    print("Login bem-sucedido!")
else:
    print("Login falhou. Verifique o nome de usuário e senha.")
