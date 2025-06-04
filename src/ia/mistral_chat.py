import os
import sys

from dotenv import load_dotenv
from mistralai import Mistral
from colorama import init, Fore

# Inicializar colorama para cores no terminal
init(autoreset=True)

class MistralChat:
    def __init__(self):
        """Inicializa o cliente Mistral com a API key do arquivo .env"""
        load_dotenv()
        
        self.api_key = os.getenv('MISTRAL_API_KEY')
        if not self.api_key:
            print(f"{Fore.RED}❌ Erro: MISTRAL_API_KEY não encontrada no arquivo .env")
            sys.exit(1)
        
        try:
            self.client = Mistral(api_key=self.api_key)
            print(f"{Fore.GREEN}✅ Cliente Mistral inicializado com sucesso!")
        except Exception as e:
            print(f"{Fore.RED}❌ Erro ao inicializar cliente Mistral: {e}")
            sys.exit(1)
        
        # Histórico da conversa
        self.conversation_history = []
        
        # Modelos disponíveis
        self.available_models = [
            "mistral-tiny",
            "mistral-small", 
            "mistral-medium",
            "mistral-large-latest"
        ]
        
        self.current_model = "mistral-small"  # Modelo padrão
    
    def add_message(self, role: str, content: str):
        """Adiciona uma mensagem ao histórico da conversa"""
        message = {
            "role": role,
            "content": content
        }
        self.conversation_history.append(message)
    
    def send_message(self, user_message: str) -> str:
        """Envia uma mensagem para a IA e retorna a resposta"""
        try:
            self.add_message("user", user_message)
            response = self.client.chat.complete(
                model=self.current_model,
                messages=self.conversation_history,
                max_tokens=1000
            )
            ai_response = response.choices[0].message.content
            self.add_message("assistant", ai_response)
            return ai_response
        except Exception as e:
            return f"{Fore.RED}❌ Erro ao enviar mensagem: {e}"

    def change_model(self, model_name: str) -> bool:
        """Muda o modelo da IA"""
        if model_name in self.available_models:
            self.current_model = model_name
            return True
        return False
    
    def clear_history(self):
        """Limpa o histórico da conversa"""
        self.conversation_history = []
        print(f"{Fore.YELLOW}🗑️  Histórico da conversa limpo!")
    
    def show_help(self):
        """Mostra os comandos disponíveis"""
        help_text = f"""
{Fore.CYAN}📋 Comandos disponíveis:
{Fore.WHITE}/help{Fore.CYAN} - Mostra esta ajuda
{Fore.WHITE}/model <nome>{Fore.CYAN} - Muda o modelo da IA
{Fore.WHITE}/models{Fore.CYAN} - Lista modelos disponíveis
{Fore.WHITE}/clear{Fore.CYAN} - Limpa o histórico da conversa
{Fore.WHITE}/history{Fore.CYAN} - Mostra o histórico da conversa
{Fore.WHITE}/quit{Fore.CYAN} ou {Fore.WHITE}/exit{Fore.CYAN} - Sai do programa

{Fore.GREEN}💡 Dica: Digite sua mensagem normalmente para conversar com a IA!
"""
        print(help_text)
    
    def show_models(self):
        """Mostra os modelos disponíveis"""
        print(f"\n{Fore.CYAN}🤖 Modelos disponíveis:")
        for model in self.available_models:
            marker = f"{Fore.GREEN}➤ " if model == self.current_model else f"{Fore.WHITE}  "
            print(f"{marker}{model}")
        print(f"\n{Fore.YELLOW}Modelo atual: {Fore.GREEN}{self.current_model}")
    
    def show_history(self):
        """Mostra o histórico da conversa"""
        if not self.conversation_history:
            print(f"{Fore.YELLOW}📝 Nenhuma conversa no histórico.")
            return
        
        print(f"\n{Fore.CYAN}📝 Histórico da conversa:")
        print("-" * 50)
        
        for message in self.conversation_history:
            role = message.get("role", "unknown")
            content = message.get("content", "")
            
            if role == "user":
                role_color = Fore.BLUE
                role_icon = "👤"
                role_name = "Você"
            elif role == "assistant":
                role_color = Fore.GREEN
                role_icon = "🤖"
                role_name = "Mistral"
            elif role == "system":
                role_color = Fore.YELLOW
                role_icon = "⚙️"
                role_name = "Sistema"
            else:
                role_color = Fore.WHITE
                role_icon = "❓"
                role_name = "Desconhecido"
            
            print(f"\n{role_color}{role_icon} {role_name}: {Fore.WHITE}{content}")
        
        print("-" * 50)
    
    def run(self):
        """Executa o loop principal do chat"""
        print(f"{Fore.MAGENTA}🚀 Chat com Mistral AI iniciado!")
        print(f"{Fore.CYAN}Modelo atual: {Fore.GREEN}{self.current_model}")
        print(f"{Fore.YELLOW}Digite /help para ver os comandos disponíveis.")
        print(f"{Fore.YELLOW}Digite /quit ou /exit para sair.\n")
        
        while True:
            try:
                user_input = input(f"{Fore.BLUE}👤 Você: {Fore.WHITE}").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['/quit', '/exit']:
                    print(f"{Fore.MAGENTA}👋 Até logo!")
                    break
                elif user_input.lower() == '/help':
                    self.show_help()
                elif user_input.lower() == '/models':
                    self.show_models()
                elif user_input.lower() == '/clear':
                    self.clear_history()
                elif user_input.lower() == '/history':
                    self.show_history()
                elif user_input.lower().startswith('/model '):
                    model_name = user_input[7:].strip()
                    if self.change_model(model_name):
                        print(f"{Fore.GREEN}✅ Modelo alterado para: {model_name}")
                    else:
                        print(f"{Fore.RED}❌ Modelo '{model_name}' não encontrado.")
                        print(f"{Fore.YELLOW}Use /models para ver os modelos disponíveis.")
                else:
                    print(f"{Fore.YELLOW}🤖 Mistral está a pensar...")
                    response = self.send_message(user_input)
                    print(f"{Fore.GREEN}🤖 Mistral: {Fore.WHITE}{response}\n")
            except KeyboardInterrupt:
                print(f"\n{Fore.MAGENTA}👋 Chat interrompido. Até logo!")
                break
            except Exception as e:
                print(f"{Fore.RED}❌ Erro inesperado: {e}")

