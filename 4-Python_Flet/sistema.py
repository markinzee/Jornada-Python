#Importando o framework flet
import flet as ft 


#Criando a função principal
def main(pagina):
    texto= ft.Text('MariaSystem')
    pagina.add(texto)
    
    nome_usuario = ft.TextField(label='Digite seu usuário')
    
    chat=ft.Column()
    
    def Enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
        
    pagina.pubsub.subscribe(Enviar_mensagem_tunel)
    
   
    
    def enviar_mensagem(evento):
        #Colocar nome de usuário na mensagem
        texto_campo_mensagem= f'{nome_usuario.value}: {campo_mensagem.value}'
        pagina.pubsub.send_all(texto_campo_mensagem)
        #Limpar o campo mensagem
        campo_mensagem.value=''
        pagina.update()
        
        
        
    botao_enviar= ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    campo_mensagem= ft.TextField(label='Digite sua mensagem aqui')
    
    #Função para entrar no chat
    def entrar_chat(evento):
        #Fechar o Popup ao entrar no chat
        popup.open=False
        
        #Remover o botao de iniciar 
        pagina.remove(botao_iniciar)
        
        #Adicionar o chat
        pagina.add(chat)
        
        #Criar o campo de enviar mensagens
        linha_mensagem=ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        
        #Adicionar o campo de mensagem
        pagina.add(campo_mensagem)
        
        #Adicionar o botão de enviar
        pagina.add(botao_enviar)
        
        texto_entrou_chat= f'{nome_usuario.value} entrou no chat'
        chat.controls.append(ft.Text(texto_entrou_chat))
        pagina.update()
        
        
    popup=ft.AlertDialog(
        open=False,
        modal=True, 
        title=ft.Text('Bem-vindo(a) ao Maria System'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat)]
        )
    
    #Iniciar o chat
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    
    botao_iniciar= ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    pagina.add(botao_iniciar)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)


