# 🐍 Servidor Python - Backend API

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