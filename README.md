# 📱 Ponderada Flutter & Python

Um aplicativo completo de gerenciamento de produtos desenvolvido com **Flutter** para o frontend e **Python Flask** para o backend, utilizando **Docker** para containerização.

## 🚀 Funcionalidades

- **🔐 Autenticação**: Login e registro de usuários com JWT
- **📦 Gerenciamento de Produtos**: Visualizar, pesquisar e adicionar produtos
- **👤 Perfil do Usuário**: Editar informações do perfil
- **🔔 Notificações**: Sistema de notificações em tempo real
- **📸 Upload de Imagens**: Adicionar imagens aos produtos (câmera/galeria)
- **🌐 Suporte Multiplataforma**: Funciona em Android, iOS e Web
- **🐳 Containerização**: Deploy com Docker e Docker Compose

## Demonstração 
[![Watch the video](https://img.youtube.com/vi/d1HSaqe9Oc0/0.jpg)](https://www.youtube.com/watch?v=d1HSaqe9Oc0)

## 🛠️ Tecnologias Utilizadas

### Frontend (Flutter)
- **Flutter SDK** - Framework de desenvolvimento multiplataforma
- **HTTP** - Cliente HTTP para comunicação com API
- **SharedPreferences** - Armazenamento local de dados
- **Image Picker** - Seleção de imagens da câmera/galeria

### Backend (Python)
- **Flask** - Framework web Python
- **SQLAlchemy** - ORM para banco de dados
- **PostgreSQL** - Banco de dados (opcional, atualmente usando JSON)
- **JWT** - Autenticação com tokens
- **CORS** - Cross-Origin Resource Sharing

### Infraestrutura
- **Docker** - Containerização da aplicação
- **Docker Compose** - Orquestração de containers
- **Nginx** - Proxy reverso para produção

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Docker** e **Docker Compose**
- **Flutter SDK** (versão estável)
- **Git**
- **Python 3.7+** (para desenvolvimento local)

### Instalando o Flutter

1. **Baixe o Flutter SDK:**
   - Acesse: https://flutter.dev/docs/get-started/install
   - Baixe a versão para seu sistema operacional

2. **Configure o ambiente:**
   ```bash
   # Adicione o Flutter ao PATH
   export PATH="$PATH:`pwd`/flutter/bin"
   
   # Verifique a instalação
   flutter doctor
   ```

## 🚀 Configuração Rápida

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd pond_flutter
```

### 2. Inicie o Backend com Docker
```bash
cd python_server
docker-compose up 
```

### 3. Execute o Aplicativo Flutter
```bash
cd product_app/product_app
flutter pub get
flutter run
```

## 📁 Estrutura do Projeto

```
pond_flutter/
├── 📁 python_server/              # Backend Python
│   ├── 📄 docker-compose.yml      # Configuração Docker
│   ├── 📄 Dockerfile              # Container Flask
│   ├── 📁 nginx/                  # Configuração Nginx
│   └── 📁 python_server/
│       ├── 📄 app.py              # Aplicação Flask principal
│       ├── 📄 config.py           # Configurações
│       ├── 📁 controllers/        # Controladores da API
│       ├── 📁 models/             # Modelos de dados
│       ├── 📁 routes/             # Rotas da API
│       ├── 📁 utils/              # Utilitários
│       └── 📁 data/               # Dados JSON (banco temporário)
├── 📁 product_app/                # Aplicativo Flutter
│   └── 📁 product_app/
│       ├── 📁 lib/                # Código Dart
│       │   ├── 📄 main.dart       # Arquivo principal
│       │   ├── 📄 config.dart     # Configurações
│       │   └── 📄 add_product_screen.dart
│       ├── 📄 pubspec.yaml        # Dependências Flutter
│       └── 📁 android/            # Configuração Android
├── 📄 start_server.py             # Script de desenvolvimento
├── 📄 test_docker_connection.py   # Teste de conectividade
└── 📄 README.md                   # Este arquivo
```

## 🔧 Configuração Detalhada

### Opção 1: Deploy com Docker (Recomendado)

#### Backend
```bash
cd python_server
docker-compose up -d
```

O servidor estará disponível em:
- **Web**: `http://localhost:80`
- **Android Emulator**: `http://10.0.2.2:80`
- **iOS Simulator**: `http://localhost:80`

#### Frontend
```bash
cd product_app/product_app
flutter pub get
flutter run
```

### Opção 2: Desenvolvimento Local

#### Backend
```bash
cd python_server/python_server
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd product_app/product_app
flutter pub get
flutter run
```

## 🔌 Endpoints da API

### Autenticação
- `POST /api/register` - Registro de usuário
- `POST /api/login` - Login de usuário
- `POST /api/logout` - Logout
- `PUT /api/profile` - Atualizar perfil

### Produtos
- `GET /api/products` - Listar produtos (com paginação e busca)
- `POST /api/products` - Adicionar novo produto
- `GET /api/products/{id}` - Detalhes do produto
- `POST /api/upload-image` - Upload de imagem

### Notificações
- `GET /api/notifications` - Listar notificações
- `PUT /api/notifications/{id}/read` - Marcar como lida


## 🔒 Segurança

- **JWT Tokens** para autenticação
- **CORS** configurado para desenvolvimento
- **Validação de entrada** em todos os endpoints
- **Sanitização de dados** antes do armazenamento

## 📱 Funcionalidades do App

### Tela de Login/Registro
- ✅ Validação de email e senha
- ✅ Recuperação de senha
- ✅ Registro de novos usuários

### Tela Principal (Produtos)
- ✅ Lista de produtos com paginação
- ✅ Busca por nome
- ✅ Pull-to-refresh
- ✅ Carregamento infinito
- ✅ Detalhes do produto

### Adicionar Produto
- ✅ Formulário completo
- ✅ Upload de imagem (câmera/galeria)
- ✅ URL de imagem alternativa
- ✅ Validação de campos

### Perfil do Usuário
- ✅ Informações do usuário
- ✅ Edição de perfil
- ✅ Sistema de notificações
- ✅ Logout seguro

### Notificações
- ✅ Lista de notificações
- ✅ Marcar como lida
- ✅ Indicadores visuais
- ✅ Timestamps relativos

