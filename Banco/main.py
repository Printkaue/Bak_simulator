from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import criar_contas
from classes import conta_bancaria


class Tela1(Screen):
    
    def validar_login(self):
        # Pega os ids de cada widget da tela.
        botao = self.ids.butao_enviar
        login = self.ids.campo_usuario
        mensagem = self.ids.Erro
    
        # Verifica se o campo de usuário está vazio
        if login.text.strip() == "":
            mensagem.color = (1, 0, 0, 1)  # Define a cor da mensagem como vermelho
            mensagem.text = "Campo obrigatório"  # Define o texto da mensagem
            botao.disabled = True  # Desabilita o botão
        else:
            mensagem.text = ""  # Limpa a mensagem de erro
            botao.disabled = False  # Habilita o botão
    
    
    def logar(self):
        login = self.ids.campo_usuario.text.strip()
        mensagem = self.ids.Erro

        # Verifica se o nome de usuário existe no dicionário de contas
        if login in criar_contas.contas:
            mensagem.text = ""  # Limpa a mensagem de erro
            tela2 = self.manager.get_screen("Tela2")
            tela2.ids.nome_usuario_label.text = f"Bem vindo(a) {login}"  # Atualiza a label
            
            # Obtendo a conta e o saldo
            conta = criar_contas.contas[login]
            tela2.info_update(conta)  # Passamos o objeto conta diretamente

            self.manager.current = "Tela2"
        else:
            mensagem.color = (1, 0, 0, 1)  # Define a cor da mensagem como vermelho
            mensagem.text = "Usuário não encontrado"  # Define o texto da mensagem de erro



class Tela2(Screen):
    
    def on_enter(self):
        # Atualiza o saldo sempre que a tela for carregada
        conta = criar_contas.contas.get(self.manager.get_screen("Tela1").ids.campo_usuario.text.strip())
        if conta:
            self.info_update(conta)
    
    def info_update(self, conta):
        self.ids.saldo_usuario.text = f"Saldo: R$ {conta.saldo:.2f}"
        # Armazenando a conta bancária em uma variável da Tela2
        self.conta = conta




class Tela3(Screen):
    def criar_contas(self):
        mmsg = self.ids.Msg
        nome_user = self.ids.campo_novo_user.text.strip()
        resultado = criar_contas.criar_conta(nome_user, saldo_inicial=0)
        mmsg.text = resultado  # Exibe a mensagem retornada pela função




#tela de trasnferir
class Tela4(Screen):
    def transferencia(self):
        try:
            valor = float(self.ids.valor_transferencia.text.strip())
            destinario = self.ids.destinatario.text
            user = self.manager.get_screen('Tela2').conta
            
            if destinario in criar_contas.contas:
                destino = criar_contas.contas[destinario]
                
                if user.saldo >= valor:
                    destino.saldo += valor
                    user.saldo -= valor
                    self.ids.msg_erro_t.text = "Transferencia concluida !"
                else:
                    self.ids.msg_erro_t.text = "Ops ! Saldo insuficiente."
            else:
                self.ids.msg_erro_t.text = "Destino não encontrado."
                    
        except ValueError:
                    self.ids.msg_erro_t.text = "Erro."
                        
    
#Tela de sacar.
class Tela5(Screen):
    def saque(self):
        try:
            valor = float(self.ids.valor_saque.text.strip())
            
            # Verifica se a conta está armazenada corretamente na Tela2
            if hasattr(self.manager.get_screen('Tela2'), 'conta'):
                conta = self.manager.get_screen('Tela2').conta
                conta.sacar(valor)  # Chama o método sacar da conta
                self.ids.msg_erro_s.text = "Saque concluído!"
            
        except ValueError:
            self.ids.msg_erro_s.text = "Ops! Você digitou um valor inválido!"


#Tela deposito.
class Tela6(Screen):
    def deposito(self):
        try:
            valor = float(self.ids.valor_deposito.text.strip())
            
            # Acessando a conta da Tela2 e chamando a função depositar
            if hasattr(self.manager.get_screen('Tela2'), 'conta'):
                conta = self.manager.get_screen('Tela2').conta
                conta.depositar(valor)  # Chama o método depositar da conta
                self.ids.msg_erros.text = "Depósito concluído!"
            
        except ValueError:
            self.ids.msg_erros.text = "Ops! Você digitou um valor inválido!"


# Carrega o arquivo KV
KV = Builder.load_file("tela.kv")

class MeuApp(App):
    def build(self):
        return KV

# Roda o aplicativo
if __name__ == "__main__":
    MeuApp().run()
