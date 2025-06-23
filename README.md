# 📱 Aplicativo de Produtos - Flutter + Python

Um aplicativo completo de gerenciamento de produtos desenvolvido com Flutter para o frontend e Python Flask para o backend.

## Atividade em Funcionamento 
https://www.youtube.com/watch?v=T3BNST0HZjM 

## 🚀 Funcionalidades

- **🔐 Autenticação**: Login e registro de usuários
- **📦 Gerenciamento de Produtos**: Visualizar, pesquisar e adicionar produtos
- **👤 Perfil do Usuário**: Editar informações do perfil
- **🔔 Notificações**: Visualizar e gerenciar notificações
- **📸 Upload de Imagens**: Adicionar imagens aos produtos
- **🌐 Suporte Web**: Funciona tanto em dispositivos móveis quanto na web

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.7+**
- **Flutter SDK** (versão estável)
- **Git**

### Instalando o Flutter

1. **Baixe o Flutter SDK:**
   - Acesse: https://flutter.dev/docs/get-started/install
   - Baixe a versão para Windows

2. **Extraia e configure:**
   ```bash
   # Extraia o arquivo zip para C:\flutter
   # Adicione C:\flutter\bin ao PATH do sistema
   ```

3. **Verifique a instalação:**
   ```bash
   flutter doctor
   ```

## 🛠️ Configuração do Projeto

### 1. Clone o Repositório

```bash
git clone <url-do-repositorio>
cd pond_flutter
```

### 2. Configurar o Backend Python

1. **Instalar dependências Python:**
   ```bash
   pip install flask flask-cors
   ```

2. **Iniciar o servidor backend:**
   ```bash
   python app.py
   ```

   O servidor estará rodando em: `http://localhost:5000`

### 3. Configurar o Aplicativo Flutter

1. **Navegar para o diretório do projeto Flutter:**
   ```bash
   cd product_app/product_app
   ```

2. **Instalar dependências Flutter:**
   ```bash
   flutter pub get
   ```

3. **Executar o aplicativo:**
   ```bash
   flutter run
   ```

## 🎯 Como Usar

### Credenciais Padrão

O sistema cria automaticamente um usuário administrador:
- **Email**: `admin@example.com`
- **Senha**: `admin123`

### Funcionalidades Principais

#### 🔐 Autenticação
1. **Login**: Use suas credenciais para acessar o sistema
2. **Registro**: Crie uma nova conta se necessário
3. **Recuperação de Senha**: Use a opção "Esqueci a senha"

#### 📦 Produtos
1. **Visualizar Produtos**: Lista paginada de todos os produtos
2. **Pesquisar**: Use a barra de pesquisa para encontrar produtos específicos
3. **Adicionar Produto**: Clique no botão "+" para adicionar um novo produto
4. **Upload de Imagem**: Selecione uma imagem do seu dispositivo ou forneça uma URL

#### 👤 Perfil
1. **Visualizar Perfil**: Acesse suas informações pessoais
2. **Editar Perfil**: Modifique nome, telefone e senha
3. **Notificações**: Visualize suas notificações

## 🌐 Executando na Web

Para executar o aplicativo na web:

```bash
flutter run -d chrome
```

**Nota**: O upload de imagens funciona perfeitamente na web com as correções implementadas.

## 📁 Estrutura do Projeto

```
pond_flutter/
├── app.py                          # Servidor Python Flask
├── main.dart                       # Aplicativo Flutter principal
├── add_product_screen.dart         # Tela de adicionar produto
├── product_app/                    # Projeto Flutter
│   └── product_app/
│       ├── lib/
│       │   ├── main.dart
│       │   └── add_product_screen.dart
│       ├── pubspec.yaml
│       └── ...
├── python_server/                  # Dados do servidor
│   ├── data/
│   │   ├── products.json
│   │   ├── users.json
│   │   └── ...
│   └── images/                     # Imagens enviadas
└── README.md
```

## 🔧 Endpoints da API

### Autenticação
- `POST /api/register` - Registro de usuário
- `POST /api/login` - Login de usuário
- `POST /api/logout` - Logout
- `POST /api/reset-password` - Recuperação de senha

### Produtos
- `GET /api/products` - Listar produtos (com paginação e busca)
- `POST /api/products` - Adicionar novo produto
- `GET /api/products/<id>` - Obter produto específico

### Usuário
- `GET /api/profile` - Obter perfil do usuário
- `PUT /api/profile` - Atualizar perfil

### Imagens
- `POST /api/upload-image` - Upload de imagem
- `GET /images/<filename>` - Servir imagem

### Notificações
- `GET /api/notifications` - Listar notificações
- `PUT /api/notifications/<id>/read` - Marcar como lida

## 🐛 Solução de Problemas

### Erro de SDK do Dart
Se você encontrar erro de versão do SDK:
```bash
# O arquivo pubspec.yaml já está configurado corretamente
# Se necessário, execute:
flutter clean
flutter pub get
```

### Erro de Upload de Imagem na Web
O problema de `Image.file` na web foi corrigido. O aplicativo agora:
- Usa `Image.memory` para web
- Usa `Image.file` para dispositivos móveis

### Servidor não Inicia
```bash
# Verifique se as dependências estão instaladas
pip install flask flask-cors

# Verifique se a porta 5000 está livre
# Se necessário, altere a porta no app.py
```

### Flutter não Executa
```bash
# Verifique se o Flutter está instalado
flutter doctor

# Limpe o cache se necessário
flutter clean
flutter pub get
```

## 📱 Plataformas Suportadas

- ✅ **Android**
- ✅ **iOS**
- ✅ **Web** (Chrome, Firefox, Safari, Edge)
- ✅ **Windows**
- ✅ **macOS**
- ✅ **Linux**

## 🔒 Segurança

- Senhas são criptografadas usando SHA-256
- Tokens de autenticação com expiração
- Validação de entrada em todos os formulários
- CORS configurado para desenvolvimento

## 🚀 Deploy

### Backend (Python)
Para produção, use um servidor WSGI como Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Frontend (Flutter)
Para build de produção:
```bash
# Web
flutter build web

# Android
flutter build apk --release

# iOS
flutter build ios --release
```


## 📄 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

**Desenvolvido com ❤️ usando Flutter e Python** 
