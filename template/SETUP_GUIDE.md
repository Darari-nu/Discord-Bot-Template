# 🚀 Discord Bot 完全セットアップガイド

**完全初心者向け：30分でDiscord Botを動かそう！**

## 📋 必要なもの

- **パソコン**（Windows/Mac/Linux）
- **インターネット接続**
- **Discordアカウント**
- **Python 3.8以上**（インストール方法は後述）

## 🎯 完成イメージ

このガイドを完了すると：
- ✅ あなた専用のDiscord Botが完成
- ✅ `!ping` で「Pong!」と返事
- ✅ `!echo こんにちは` で「こんにちは」とエコー
- ✅ 👋 リアクションで挨拶を返す
- ✅ 「おはよう」「おやすみ」に自動返事

---

## 📝 Step 1: Python環境の準備

### **Pythonがインストールされているか確認**

**Windows:**
```cmd
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

### **Pythonが入っていない場合**

**Windows:**
1. https://python.org/downloads/ にアクセス
2. 「Download Python 3.12.x」をクリック
3. ダウンロードしたファイルを実行
4. **「Add Python to PATH」にチェックを入れる**←重要！
5. 「Install Now」をクリック

**Mac:**
```bash
# Homebrewがある場合（推奨）
brew install python

# Homebrewがない場合はpython.orgからダウンロード
```

**Linux（Ubuntu/Debian）:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 🤖 Step 2: Discord Botアプリケーションの作成

### **2-1. Discord Developer Portalにアクセス**
1. https://discord.com/developers/applications にアクセス
2. Discordアカウントでログイン

### **2-2. 新しいアプリケーションを作成**
1. 「**New Application**」ボタンをクリック
2. Bot名を入力（例：「My First Bot」）
3. 「**Create**」をクリック

### **2-3. Botユーザーを作成**
1. 左側メニューの「**Bot**」をクリック
2. 「**Add Bot**」→「**Yes, do it!**」をクリック
3. **Bot Token**をコピー（後で使います）
   - 「**Reset Token**」→「**Copy**」
   - ⚠️ **このTokenは秘密！誰にも教えない！**

### **2-4. Bot権限の設定**
1. 同じページで下にスクロール
2. 「**Privileged Gateway Intents**」セクションで以下をON：
   - ✅ **Message Content Intent**
   - ✅ **Server Members Intent**（オプション）

### **2-5. Bot招待リンクの作成**
1. 左側メニューの「**OAuth2**」→「**URL Generator**」
2. **Scopes**で「**bot**」にチェック
3. **Bot Permissions**で以下にチェック：
   - ✅ **Send Messages**
   - ✅ **Read Messages/View Channels**
   - ✅ **Add Reactions**
   - ✅ **Read Message History**
4. 生成されたURLをコピー

### **2-6. Botをサーバーに招待**
1. コピーしたURLをブラウザで開く
2. Botを追加したいサーバーを選択
3. 「**認証**」をクリック

---

## ⚙️ Step 3: Botファイルの準備

### **3-1. ファイルのダウンロード・配置**
```bash
# このテンプレートフォルダを任意の場所にコピー
# 例：デスクトップに「my-discord-bot」フォルダを作成
```

### **3-2. 環境変数ファイルの作成**
```bash
# templateフォルダ内で実行
cp .env.example .env
```

### **3-3. Bot Tokenの設定**
`.env`ファイルを**テキストエディタ**で開いて編集：

**編集前：**
```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
```

**編集後：**
```
DISCORD_BOT_TOKEN=実際のBotToken
```

💡 **Tokenの例：**
```
DISCORD_BOT_TOKEN=YOUR_BOT_APPLICATION_ID.TOKEN_PART_1.TOKEN_PART_2_KEEP_THIS_SECRET
```

---

## 🎯 Step 4: Botの起動

### **4-1. 依存関係のインストール**
```bash
# templateフォルダ内で実行
pip install -r requirements.txt

# Macの場合はpip3を使う場合があります
pip3 install -r requirements.txt
```

### **4-2. Botの起動**
```bash
python bot.py

# Macの場合
python3 bot.py
```

### **4-3. 起動成功の確認**
以下のようなメッセージが表示されれば成功：
```
2025-07-25 10:30:45 - __main__ - INFO - Template Bot#1234 としてログインしました
2025-07-25 10:30:45 - __main__ - INFO - Bot名: Template Bot
2025-07-25 10:30:45 - __main__ - INFO - コマンドプレフィックス: !
2025-07-25 10:30:45 - __main__ - INFO - サーバー数: 1
```

---

## 🎉 Step 5: 動作確認

### **Discord上でテスト**

**1. pingコマンド**
```
!ping
```
→ 「🏓 Pong! レイテンシ: XXms」と返答

**2. echoコマンド**
```
!echo Hello World!
```
→ 「📢 エコー Hello World!」と返答

**3. ヘルプコマンド**
```
!help
```
→ コマンド一覧が表示

**4. リアクション機能**
- 任意のメッセージに👋でリアクション
- → Botが「👋 こんにちは、@あなた さん！」と返答

**5. 自動応答**
```
おはよう
```
→ 「おはようございます、@あなた さん！ ☀️」

---

## ❌ トラブルシューティング

### **よくあるエラーと解決方法**

#### **エラー1: `DISCORD_BOT_TOKENが設定されていません`**
**原因：** `.env`ファイルの設定が間違っている
**解決：**
1. `.env`ファイルが存在するか確認
2. Bot Tokenが正しく設定されているか確認
3. Token前後に余分なスペースがないか確認

#### **エラー2: `Bot Tokenが無効です`**
**原因：** Discord Developer PortalのTokenが間違っている
**解決：**
1. Discord Developer Portalで「Reset Token」
2. 新しいTokenを`.env`に設定

#### **エラー3: `ModuleNotFoundError: No module named 'discord'`**
**原因：** 依存関係がインストールされていない
**解決：**
```bash
pip install -r requirements.txt
```

#### **エラー4: Botがメッセージに反応しない**
**原因：** Bot権限またはIntentsの設定問題
**解決：**
1. Discord Developer Portal → Bot → Privileged Gateway Intents
2. 「Message Content Intent」をONにする
3. Botを再起動

#### **エラー5: `python: command not found`**
**原因：** PythonがPATHに設定されていない
**解決：**
- Windows: Pythonを再インストール（「Add to PATH」チェック）
- Mac/Linux: `python3`コマンドを使用

---

## 🎊 成功！次は何をする？

### **機能を追加したい場合**
Claude.codeに以下のように依頼：
```
「天気予報機能を追加したい」
「音楽Bot機能を追加したい」
「管理者コマンドを追加したい」
```

### **デプロイしたい場合**
`deploy/` フォルダの手順に従ってサーバーにデプロイ

### **コードを理解したい場合**
`docs/` フォルダの学習ガイドを参照

---

## 📞 サポート

**問題が解決しない場合：**
1. **エラーメッセージ全文**をコピー
2. **実行環境**（Windows/Mac/Linux、Pythonバージョン）を明記
3. Claude.codeに質問

**よくある質問:**
- Q: 複数サーバーで使える？ → A: はい、同じBotを複数サーバーに招待可能
- Q: 24時間稼働させるには？ → A: `deploy/` フォルダのVPS手順を参照
- Q: コードを改造しても大丈夫？ → A: はい！自由に改造してください

---

**🎉 お疲れ様でした！Discord Bot開発の世界へようこそ！**

*セットアップガイド Ver.1.0 | 想定時間: 30分*