from src.ia.mistral_chat import MistralChat

def main():
    """Função principal"""
    try:
        chat = MistralChat()
        chat.run()
    except Exception as e:
        print(f"{Fore.RED}❌ Erro ao inicializar o chat: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
