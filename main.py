usuarios = {
  "Nelson" : "1234",
  "Max" : "4321" 
}

def verificar_credenciais(usuario, senha) : 
  print(f"Verificar se as credendciais são validas")
  if usuario in usuario and usuarios[usuario] == senha : 
    return True 
  else:
    raise ValueError("Nome de usuario e senha incorreto") 

def login() :
  while True:
    try: 
      usuario = input("Digite seu nome de usuario ou digite sair para encerrar): ")
      if usuario == 'sair' :
        print("Encerrando programa") 
        break  
      senha = input("Digite sua senha") 

      if verificar_credenciais(usuario,senha) : 
        print(f"Login bem sucedido . Bem vindo, {usuario}")
        break

    except ValueError as e:
        print(e)
    else:
        print("Você está logado")
    finally:
        print("Tentativa de login finalizada")

login() 
        