# 🤖 Discord Bot Template - 完全ガイド

**📚 完全初心者対応：フォルダを読んで30分でDiscord Botが完成！**

## 🎊 スタートアップクイック

**初めての方はここから：**
1. 📖 **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - 30分で完成する詳細手順
2. 🔧 **[DISCORD_SETUP.md](DISCORD_SETUP.md)** - Discord設定の画像解説
3. 🆘 **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - 困った時の解決集

## 🎯 このテンプレートでできること

- **基本Bot**: メッセージ送受信、リアクション処理
- **機能追加**: エコー、ヘルプ、カスタム機能
- **簡単デプロイ**: ローカル開発→本番環境へ1コマンド
- **学習支援**: コメント豊富なコードで理解しやすい

## 🚀 クイックスタート

### Step 1: 環境準備
```bash
# 1. 必要なファイルをコピー
cp config/config.example.json config.json
cp config/.env.example .env

# 2. Discord Bot Tokenを設定
# .env ファイルを編集:
# DISCORD_BOT_TOKEN=あなたのボットトークン
```

### Step 2: Bot作成（Discord Developer Portal）
1. https://discord.com/developers/applications にアクセス
2. 「New Application」でアプリ作成
3. 「Bot」タブでBot Tokenを取得
4. 「OAuth2」→「URL Generator」でBot招待リンク生成
5. サーバーにBotを招待

### Step 3: 起動
```bash
# 依存関係インストール
pip install -r requirements.txt

# Bot起動
python bot.py
```

## 📁 フォルダ構成詳細

```
template/
├── 📄 bot.py                 # メインBot（ここから開始）
├── 📁 core/                  # コアシステム
│   ├── base_bot.py          # Bot基底クラス
│   ├── message_handler.py   # メッセージ処理
│   └── reaction_handler.py  # リアクション処理
├── 📁 features/             # 機能テンプレート
│   ├── echo.py             # エコー機能（学習用）
│   ├── help.py             # ヘルプ機能
│   └── template_feature.py # 新機能追加用テンプレート
├── 📁 deploy/              # デプロイ用
│   ├── deploy.sh           # ワンクリックデプロイ
│   ├── docker/             # Docker設定
│   └── requirements.txt    # Python依存関係
├── 📁 config/              # 設定ファイル
│   ├── config.example.json # 設定例
│   └── .env.example        # 環境変数例
└── 📁 docs/                # 学習ガイド
    ├── basic_concepts.md   # Discord Bot基礎
    ├── adding_features.md  # 機能追加方法
    └── deployment.md       # デプロイガイド
```

## 💡 機能追加の3パターン

### 1. **コマンド型**
```python
@bot.command(name='weather')
async def weather_command(ctx, city):
    await ctx.send(f'{city}の天気を調べています...')
```

### 2. **リアクション型**  
```python
@bot.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == '👍':
        await reaction.message.channel.send('いいね！')
```

### 3. **自動応答型**
```python
@bot.event
async def on_message(message):
    if 'おはよう' in message.content:
        await message.channel.send('おはようございます！')
```

## 🔧 カスタマイズポイント

### 設定ファイル（config.json）
```json
{
  "bot_name": "あなたのBot名",
  "prefix": "!",
  "features": {
    "echo": true,
    "help": true,
    "custom": false
  }
}
```

### 環境変数（.env）
```env
DISCORD_BOT_TOKEN=your_bot_token_here
OPENAI_API_KEY=your_openai_key_here  # AI機能使用時
```

## 🚀 デプロイ方法

### ローカル開発
```bash
python bot.py
```

### 本番デプロイ（VPS）
```bash
./deploy/deploy.sh your-server-ip
```

### Docker使用
```bash
cd deploy/docker/
docker-compose up -d
```

## 📚 学習ガイド

1. **初心者**: `docs/basic_concepts.md` から開始
2. **機能追加**: `docs/adding_features.md` を参照
3. **デプロイ**: `docs/deployment.md` でサーバー設定
4. **参考実装**: `../reference/ai-Darari-nu/` で本格例を確認

## ❓ よくある質問

**Q: エラーが出ます**
A: `bot.py` のコメントとエラーメッセージを確認。大抵は設定不備です。

**Q: 機能を追加したい**
A: Claude.codeに「○○の機能が欲しい」と自然言語で依頼してください。

**Q: デプロイが難しい**
A: まずローカルで動作確認後、`deploy/deploy.sh` を使用してください。

## 🛠️ トラブルシューティング

- **Bot Token不正**: Discord Developer Portalで再生成
- **権限不足**: Bot招待時に必要な権限を選択
- **依存関係エラー**: `pip install -r requirements.txt` を再実行
- **Port使用中**: 別のポート番号を使用

---

**🎉 Discord Bot開発を楽しもう！**

次のステップ: `bot.py` を実行して、最初のBotを動かしてみましょう！