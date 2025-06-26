f# 🐍 Servidor Python - Backend API

Este diretório contém o servidor backend Python Flask que fornece a API para o aplicativo Flutter.

## 🚀 Execução Rápida

### Pré-requisitos
- Python 3.7+
- pip (gerenciador de pacotes Python)

### Instalação e Execução

```bash
# 1. Instalar dependências
pip install flask flask-cors

# 2. Executar o servidor
python app.py

# 3. Acessar a API
# Servidor rodando em: http://localhost:5000
```

## 📁 Estrutura do Servidor

```
python_server/
├── app.py                    # Servidor Flask principal
├── data/                     # Dados JSON
│   ├── products.json         # Produtos cadastrados
│   ├── users.json           # Usuários registrados
│   ├── sessions.json        # Sessões ativas
│   └── notifications.json   # Notificações do sistema
├── images/                   # Imagens enviadas pelos usuários
└── server.log               # Logs do servidor
```

## 🔧 Configuração

### Variáveis de Ambiente
O servidor usa as seguintes configurações padrão:
- **Porta**: 5000
- **Host**: 0.0.0.0 (aceita conexões de qualquer IP)
- **Modo**: Debug (desenvolvimento)

### Alterando a Porta
Edite o arquivo `app.py` na linha final:
```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## 📊 Endpoints da API

### 🔐 Autenticação

#### POST /api/register
Registra um novo usuário.
```json
{
  "name": "Nome do Usuário",
  "email": "usuario@email.com",
  "password": "senha123"
}
```

#### POST /api/login
Faz login do usuário.
```json
{
  "email": "usuario@email.com",
  "password": "senha123"
}
```

#### POST /api/logout
Faz logout do usuário (requer token de autenticação).

#### POST /api/reset-password
Solicita redefinição de senha.
```json
{
  "email": "usuario@email.com"
}
```

### 📦 Produtos

#### GET /api/products
Lista produtos com paginação e busca.
```
Parâmetros:
- page: número da página (padrão: 1)
- limit: itens por página (padrão: 10)
- search: termo de busca (opcional)
```

#### POST /api/products
Adiciona um novo produto (requer autenticação).
```json
{
  "name": "Nome do Produto",
  "description": "Descrição do produto",
  "price": 99.99,
  "image_url": "http://exemplo.com/imagem.jpg"
}
```

#### GET /api/products/<id>
Obtém detalhes de um produto específico.

### 👤 Usuário

#### GET /api/profile
Obtém perfil do usuário (requer autenticação).

#### PUT /api/profile
Atualiza perfil do usuário (requer autenticação).
```json
{
  "name": "Novo Nome",
  "phone": "+5511999999999",
  "password": "nova_senha"
}
```

### 📸 Imagens

#### POST /api/upload-image
Faz upload de uma imagem (requer autenticação).
```json
{
  "image_data": "base64_encoded_image_data"
}
```

#### GET /images/<filename>
Serve uma imagem específica.

### 🔔 Notificações

#### GET /api/notifications
Lista notificações do usuário.

#### PUT /api/notifications/<id>/read
Marca uma notificação como lida.

## 🔒 Segurança

### Implementado
- ✅ Criptografia de senhas (SHA-256)
- ✅ Tokens de sessão com expiração (24h)
- ✅ Validação de entrada
- ✅ CORS configurado
- ✅ Sanitização de dados

### Autenticação
O servidor usa tokens Bearer para autenticação:
```
Authorization: Bearer <token>
```

## 📊 Dados

### Estrutura dos Arquivos JSON

#### users.json
```json
{
  "user_id": {
    "id": "user_id",
    "name": "Nome do Usuário",
    "email": "usuario@email.com",
    "password": "hash_da_senha",
    "phone": "+5511999999999",
    "profile_image": "url_da_imagem",
    "created_at": "2024-01-01T00:00:00"
  }
}
```

#### products.json
```json
{
  "product_id": {
    "id": "product_id",
    "name": "Nome do Produto",
    "description": "Descrição do produto",
    "price": 99.99,
    "image_url": "url_da_imagem",
    "created_at": "2024-01-01T00:00:00",
    "created_by": "user_id"
  }
}
```

## 🐛 Debugging

### Logs
O servidor gera logs em `server.log`:
```bash
tail -f server.log
```

### Modo Debug
O servidor roda em modo debug por padrão, mostrando:
- Logs detalhados
- Stack traces de erros
- Auto-reload em mudanças

### Testando Endpoints
Use curl ou Postman para testar:
```bash
# Teste de saúde
curl http://localhost:5000/api/products

# Login
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"admin123"}'
```

## 🚀 Deploy em Produção

### Usando Gunicorn
```bash
# Instalar Gunicorn
pip install gunicorn

# Executar em produção
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Usando Docker
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Configurações de Produção
1. **Desabilitar modo debug**:
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

2. **Usar banco de dados real** (PostgreSQL, MySQL):
   - Substituir arquivos JSON por banco de dados
   - Implementar migrations

3. **Configurar HTTPS**:
   - Usar proxy reverso (Nginx)
   - Configurar certificados SSL

4. **Monitoramento**:
   - Implementar logging estruturado
   - Adicionar métricas de performance
   - Configurar alertas

## 📈 Performance

### Otimizações Implementadas
- ✅ Paginação de resultados
- ✅ Compressão de imagens
- ✅ Cache de sessões
- ✅ Validação eficiente

### Métricas Recomendadas
- Tempo de resposta: < 200ms
- Throughput: > 1000 req/s
- Uptime: > 99.9%

## 🔧 Manutenção

### Backup dos Dados
```bash
# Backup dos arquivos JSON
cp -r data/ backup/data_$(date +%Y%m%d_%H%M%S)/

# Backup das imagens
cp -r images/ backup/images_$(date +%Y%m%d_%H%M%S)/
```

### Limpeza de Dados
- Sessões expiradas são removidas automaticamente
- Imagens não utilizadas podem ser limpas manualmente
- Logs antigos podem ser rotacionados

## 📞 Suporte

Para problemas com o servidor:
1. Verifique os logs em `server.log`
2. Confirme se as dependências estão instaladas
3. Teste a conectividade da rede
4. Verifique as permissões de arquivo

---

**Desenvolvido com Flask ❤️** 

## 🚀 How to Run the Flutter App on Android

### Step 1: Check Flutter Setup

First, verify your Flutter installation and Android setup:

```bash
flutter doctor
```

This will show you what's missing. You should see:
- ✅ Flutter SDK
- ✅ Android toolchain
- ✅ Android Studio (optional but recommended)
- ✅ Connected devices

### Step 2: Set Up Android Development

If you don't have Android development set up:

1. **Install Android Studio** (recommended):
   - Download from: https://developer.android.com/studio
   - Install and set up Android SDK

2. **Or use command line only**:
   ```bash
   # Install Android SDK command line tools
   flutter doctor --android-licenses
   ```

### Step 3: Connect Android Device or Emulator

#### Option A: Physical Android Device
1. **Enable Developer Options**:
   - Go to Settings → About Phone
   - Tap "Build Number" 7 times
   - Go back to Settings → Developer Options
   - Enable "USB Debugging"

2. **Connect via USB**:
   ```bash
   # Check if device is detected
   flutter devices
   ```

#### Option B: Android Emulator
1. **Create an emulator**:
   ```bash
   # List available emulators
   flutter emulators
   
   # Create a new emulator (if needed)
   flutter emulators --create --name Pixel_4_API_30
   
   # Launch emulator
   flutter emulators --launch Pixel_4_API_30
   ```

### Step 4: Start the Backend Server

Make sure your Python backend is running:

```bash
# In the main project directory
python app.py
```

The server should be running on `http://localhost:5000`

### Step 5: Run the Flutter App

Navigate to the Flutter project directory and run:

```bash
# Navigate to the Flutter project
cd product_app/product_app

# Get dependencies
flutter pub get

# Run on Android
flutter run
```

### Step 6: Alternative Commands

If you have multiple devices connected:

```bash
# List available devices
flutter devices

# Run on specific device
flutter run -d <device-id>

# Run in release mode (faster)
flutter run --release

# Run with specific flavor
flutter run --flavor development
```

## 🔧 Troubleshooting Common Issues

### Issue 1: "No connected devices"
```bash
# Check if devices are detected
flutter devices

# If using physical device, make sure:
# - USB debugging is enabled
# - Device is connected via USB
# - You've accepted the USB debugging prompt on your phone
```

### Issue 2: "Android SDK not found"
```bash
# Set ANDROID_HOME environment variable
export ANDROID_HOME=/path/to/your/android/sdk

# Or install Android Studio and let it set up the SDK
```

### Issue 3: "Gradle build failed"
```bash
# Clean and rebuild
flutter clean
flutter pub get
flutter run
```

### Issue 4: "Backend connection failed"
Make sure:
- Python server is running on `http://localhost:5000`
- Your Android device/emulator can access localhost
- For emulator, use `10.0.2.2:5000` instead of `localhost:5000`

## 📱 Building APK for Distribution

To create an APK file for distribution:

```bash
# Build APK
flutter build apk

# Build APK with specific flavor
flutter build apk --flavor production

# Build split APKs (smaller size)
flutter build apk --split-per-abi
```

The APK will be created at: `build/app/outputs/flutter-apk/app-release.apk`

## 🎯 Quick Start Commands

Here's the complete sequence to run on Android:

```bash
# 1. Start backend (in one terminal)
python app.py

# 2. Run Flutter app (in another terminal)
cd product_app/product_app
flutter pub get
flutter run
```

## 📋 Android-Specific Features

The app includes these Android-specific features:
- ✅ Camera access for product photos
- ✅ Gallery access for image selection
- ✅ Local storage for user preferences
- ✅ Material Design 3 UI
- ✅ Native Android navigation
- ✅ Push notifications (ready for implementation)

## 🔍 Testing on Different Android Versions

To test on different Android API levels:

```bash
# Create emulators with different API levels
flutter emulators --create --name Pixel_4_API_21  # Android 5.0
flutter emulators --create --name Pixel_4_API_30  # Android 11
flutter emulators --create --name Pixel_4_API_33  # Android 13
```

Would you like me to help you with any specific step, or do you have an Android device/emulator ready to test with? 