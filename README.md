# 📱 Aplicativo de Produtos - Flutter + Python

Um aplicativo completo de gerenciamento de produtos desenvolvido com **Flutter** para o frontend e **Python Flask** para o backend, utilizando **Docker** para containerização.

## 🚀 Funcionalidades

- **🔐 Autenticação**: Login e registro de usuários com JWT
- **📦 Gerenciamento de Produtos**: Visualizar, pesquisar e adicionar produtos
- **👤 Perfil do Usuário**: Editar informações do perfil
- **🔔 Notificações**: Sistema de notificações em tempo real
- **📸 Upload de Imagens**: Adicionar imagens aos produtos (câmera/galeria)
- **🌐 Suporte Multiplataforma**: Funciona em Android, iOS e Web
- **🐳 Containerização**: Deploy com Docker e Docker Compose

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
docker-compose up -d
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

## 🧪 Testando a Aplicação

### 1. Verificar Conectividade
```bash
python test_docker_connection.py
```

### 2. Credenciais de Teste
- **Email**: `admin@example.com`
- **Senha**: `admin123`

### 3. Fluxo de Teste
1. **Login** com as credenciais acima
2. **Adicionar produto** usando o botão "+"
3. **Verificar notificação** no perfil
4. **Editar perfil** e verificar atualizações

## 🐛 Solução de Problemas

### Problemas Comuns

#### 1. "Connection refused" no Flutter
- **Causa**: Servidor não está rodando
- **Solução**: Verifique se o Docker está ativo
  ```bash
  docker-compose ps
  docker-compose logs -f
  ```

#### 2. "Invalid response format" nas notificações
- **Causa**: Formato de resposta incorreto
- **Solução**: Reinicie o Docker para recriar os dados
  ```bash
  docker-compose down
  docker-compose up -d
  ```

#### 3. "Type error" nos produtos
- **Causa**: Dados corrompidos ou formato incorreto
- **Solução**: Limpe os dados e reinicie
  ```bash
  docker-compose down -v
  docker-compose up -d
  ```

#### 4. Carregamento infinito no perfil
- **Causa**: Dados de usuário corrompidos
- **Solução**: Use o botão de refresh ou faça logout/login

### Comandos Docker Úteis

```bash
# Verificar status dos containers
docker-compose ps

# Ver logs em tempo real
docker-compose logs -f

# Reiniciar serviços
docker-compose restart

# Reconstruir containers
docker-compose up --build -d

# Parar todos os serviços
docker-compose down

# Parar e remover volumes
docker-compose down -v
```

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

## 🚀 Deploy em Produção

### 1. Configurar Variáveis de Ambiente
```bash
# .env
SECRET_KEY=your-super-secret-key
DATABASE_URL=postgresql://user:password@host:5432/dbname
API_URL=https://yourdomain.com
```

### 2. Deploy com Docker
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### 3. Configurar Nginx
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://app:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🤝 Contribuindo

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Desenvolvido por

- **Nome**: [Seu Nome]
- **Email**: [seu.email@exemplo.com]
- **GitHub**: [@seu-usuario]

## 🙏 Agradecimentos

- Flutter Team pelo framework incrível
- Python Flask pela simplicidade e poder
- Docker pela facilidade de deploy
- Comunidade open source por todas as bibliotecas

---

**⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!** 