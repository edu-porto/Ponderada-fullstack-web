# 📱 Aplicativo de Produtos - Flutter

Este é o diretório principal do aplicativo Flutter para gerenciamento de produtos.

## 🚀 Execução Rápida

### Pré-requisitos
- Flutter SDK instalado
- Servidor Python rodando em `http://localhost:5000`

### Comandos para Executar

```bash
# 1. Instalar dependências
flutter pub get

# 2. Executar no navegador (web)
flutter run -d chrome

# 3. Executar no dispositivo móvel
flutter run

# 4. Executar no emulador Android
flutter run -d android

# 5. Executar no simulador iOS (macOS)
flutter run -d ios
```

## 📁 Estrutura do Código

```
lib/
├── main.dart                    # Arquivo principal do aplicativo
└── add_product_screen.dart      # Tela de adicionar produto

android/                         # Configurações Android
ios/                            # Configurações iOS
web/                            # Configurações Web
windows/                        # Configurações Windows
macos/                          # Configurações macOS
linux/                          # Configurações Linux
```

## 🔧 Dependências

### Principais
- `flutter` - Framework principal
- `http` - Requisições HTTP para API
- `shared_preferences` - Armazenamento local
- `image_picker` - Seleção de imagens
- `path_provider` - Gerenciamento de arquivos

### Desenvolvimento
- `flutter_test` - Testes
- `flutter_lints` - Linting e boas práticas

## 🌐 Funcionalidades Web

### Upload de Imagens
O aplicativo foi otimizado para funcionar na web:
- ✅ Upload de imagens via câmera/galeria
- ✅ Visualização de imagens selecionadas
- ✅ Compatibilidade com todos os navegadores modernos

### Responsividade
- ✅ Interface adaptável para diferentes tamanhos de tela
- ✅ Navegação otimizada para mouse e touch
- ✅ Design Material Design 3

## 📱 Funcionalidades Mobile

### Android/iOS
- ✅ Acesso à câmera e galeria
- ✅ Armazenamento local seguro
- ✅ Notificações push (preparado)
- ✅ Gestos nativos

## 🔧 Configurações

### Variáveis de Ambiente
O aplicativo se conecta ao backend em `http://localhost:5000` por padrão.

Para alterar a URL do servidor, edite o arquivo `main.dart` e substitua todas as ocorrências de:
```dart
Uri.parse('http://localhost:5000/api/...')
```

### Build de Produção

```bash
# Web
flutter build web --release

# Android
flutter build apk --release

# iOS
flutter build ios --release

# Windows
flutter build windows --release

# macOS
flutter build macos --release

# Linux
flutter build linux --release
```

## 🐛 Debugging

### Logs do Flutter
```bash
flutter logs
```

### Hot Reload
Durante o desenvolvimento, use `r` no terminal para hot reload:
```bash
Flutter run key commands.
r Hot reload. 🔥
R Hot restart.
h List all available interactive commands.
d Detach (terminate "flutter run" but leave application running).
c Clear the screen
q Quit (terminate the application on the device).
```

### DevTools
```bash
flutter pub global activate devtools
flutter pub global run devtools
```

## 📊 Performance

### Otimizações Implementadas
- ✅ Lazy loading de imagens
- ✅ Paginação de produtos
- ✅ Cache de dados locais
- ✅ Compressão de imagens antes do upload

### Métricas Recomendadas
- Tempo de carregamento inicial: < 3s
- Tempo de resposta da API: < 1s
- Tamanho do bundle: < 10MB

## 🔒 Segurança

### Implementado
- ✅ Validação de entrada em todos os formulários
- ✅ Sanitização de dados
- ✅ Tokens de autenticação seguros
- ✅ HTTPS para produção (recomendado)

### Recomendações para Produção
- Use HTTPS em produção
- Implemente rate limiting no backend
- Configure CORS adequadamente
- Use variáveis de ambiente para configurações sensíveis

## 📈 Próximas Melhorias

- [ ] Testes unitários e de widget
- [ ] Temas escuro/claro
- [ ] Internacionalização (i18n)
- [ ] Offline mode
- [ ] Push notifications
- [ ] Analytics
- [ ] Crash reporting

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte técnico:
1. Verifique a documentação do Flutter
2. Consulte os logs de erro
3. Teste em diferentes dispositivos
4. Verifique a conectividade com o backend

---

**Desenvolvido com Flutter ❤️**
