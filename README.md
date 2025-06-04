# Chat com Mistral AI

Este projeto permite conversar com a IA Mistral através de uma interface de linha de comando, usando a API key armazenada no arquivo `.env`.

## 🚀 Configuração

### 1. Instalar dependências

```bash
# Se estiver usando uv (recomendado)
uv sync

# Ou usando pip
pip install mistralai python-dotenv colorama
```

### 2. Configurar API Key

Certifique-se de que o arquivo `.env` contém sua chave da API do Mistral:

```
MISTRAL_API_KEY=sua_chave_api_aqui
```

## 🎯 Como usar

Execute o programa:

```bash
python main.py
```

## 📋 Comandos disponíveis

- **Conversa normal**: Digite sua mensagem e pressione Enter
- `/help` - Mostra a lista de comandos
- `/models` - Lista os modelos disponíveis
- `/model <nome>` - Muda o modelo da IA (ex: `/model mistral-large-latest`)
- `/clear` - Limpa o histórico da conversa
- `/history` - Mostra o histórico da conversa atual
- `/quit` ou `/exit` - Sai do programa

## 🤖 Modelos disponíveis

- `mistral-tiny` - Modelo mais rápido e econômico
- `mistral-small` - Modelo padrão (boa relação custo/benefício)
- `mistral-medium` - Modelo intermediário
- `mistral-large-latest` - Modelo mais avançado
- `open-mistral-7b` - Modelo open source 7B parâmetros
- `open-mixtral-8x7b` - Modelo open source Mixtral 8x7B
- `open-mixtral-8x22b` - Modelo open source Mixtral 8x22B

## ✨ Funcionalidades

- 💬 **Conversa interativa**: Mantenha uma conversa contínua com a IA
- 🎨 **Interface colorida**: Terminal com cores para melhor experiência
- 📝 **Histórico**: Mantém o contexto da conversa
- 🔄 **Múltiplos modelos**: Troque entre diferentes modelos do Mistral
- ⚙️ **Configurável**: Fácil configuração através do arquivo .env

## 🛠️ Exemplo de uso

```
👤 Você: Olá! Como você está?
🤖 Mistral: Olá! Estou funcionando perfeitamente e pronto para ajudar você. Como posso ser útil hoje?

👤 Você: /model mistral-large-latest
✅ Modelo alterado para: mistral-large-latest

👤 Você: Explique como funciona machine learning
🤖 Mistral: Machine learning é uma área da inteligência artificial...
```

## 🔧 Troubleshooting

### Erro de API Key
Se você receber um erro sobre a API key:
1. Verifique se o arquivo `.env` existe
2. Confirme se a variável `MISTRAL_API_KEY` está definida
3. Verifique se sua API key é válida no painel do Mistral

### Erro de conexão
- Verifique sua conexão com a internet
- Confirme se a API do Mistral está funcionando

## 📦 Dependências

- `mistralai>=1.0.0` - Cliente oficial da API Mistral (nova versão)
- `python-dotenv` - Para carregar variáveis do arquivo .env
- `colorama` - Para cores no terminal
## 🔄 Migração da versão antiga

Este projeto foi atualizado para usar a nova versão da biblioteca `mistralai` (1.0+). Se você estava usando a versão antiga (0.4.x), as principais mudanças são:

- Uso de `Mistral` em vez de `MistralClient`
- Chamadas de API atualizadas para `client.chat.complete()`
- Formato de mensagem simplificado usando dicionários
- Novos modelos open source disponíveis