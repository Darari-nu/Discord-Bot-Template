# 🔧 トラブルシューティングガイド

**Discord Bot で発生する問題の診断と解決方法**

## 🎯 このガイドの使い方

1. **症状**から該当する問題を見つける
2. **診断**の手順で原因を特定  
3. **解決方法**を試す
4. **予防策**で再発を防ぐ

---

## 📋 よくある問題一覧

### **🚫 起動・接続関連**
- [Bot Token が無効](#bot-token-が無効)
- [DISCORD_BOT_TOKEN が設定されていません](#discord_bot_token-が設定されていません)
- [Bot が起動しない](#bot-が起動しない)
- [Python が見つからない](#python-が見つからない)

### **💬 動作・反応関連**  
- [Bot がメッセージに反応しない](#bot-がメッセージに反応しない)
- [コマンドが動かない](#コマンドが動かない)
- [リアクション機能が動かない](#リアクション機能が動かない)
- [エラーメッセージが表示される](#エラーメッセージが表示される)

### **📦 依存関係・環境関連**
- [ModuleNotFoundError](#modulenotfounderror)
- [pip コマンドが見つからない](#pip-コマンドが見つからない)
- [権限エラー](#権限エラー)

---

## 🚫 起動・接続関連の問題

### **Bot Token が無効**

**症状:**
```
discord.errors.LoginFailure: Improper token has been passed.
```

**診断:**
1. `.env`ファイルが存在するか確認
2. Token が正しく設定されているか確認
3. Token に余分なスペースがないか確認

**解決方法:**
```bash
# 1. .envファイルを確認
cat .env

# 2. Tokenを再取得
# Discord Developer Portal → あなたのBot → Bot → Reset Token

# 3. .envファイルを編集
DISCORD_BOT_TOKEN=新しいToken
```

**予防策:**
- Token をコピーする際は前後の空白を含めない
- Token は定期的に再生成（セキュリティ）

---

### **DISCORD_BOT_TOKEN が設定されていません**

**症状:**
```
DISCORD_BOT_TOKENが設定されていません。.envファイルを確認してください。
```

**診断:**
```bash
# .envファイルの存在確認
ls -la | grep .env

# .envファイルの内容確認  
cat .env
```

**解決方法:**
```bash
# 1. .envファイルが存在しない場合
cp .env.example .env

# 2. .envファイルを編集
# テキストエディタで開いて以下を設定：
DISCORD_BOT_TOKEN=あなたのBotToken
```

**予防策:**
- `.env.example`から必ずコピーして使用
- `.env`ファイルを`.gitignore`に追加（公開防止）

---

### **Bot が起動しない**

**症状:**
- プログラムが途中で止まる
- エラー無しで終了する
- 無限ループ状態

**診断:**
```bash
# 詳細ログを有効にして実行
python bot.py --debug

# または .env に追加
LOG_LEVEL=DEBUG
```

**解決方法:**
1. **依存関係の再インストール**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Python バージョン確認**
   ```bash
   python --version  # 3.8以上必要
   ```

3. **ファイルの権限確認**
   ```bash
   chmod +x bot.py
   ```

**予防策:**
- 定期的な依存関係更新
- ログファイルの定期確認

---

### **Python が見つからない**

**症状:**
```
'python' is not recognized as an internal or external command
python: command not found
```

**診断:**
```bash
# PATH の確認
echo $PATH  # Mac/Linux
echo %PATH%  # Windows

# Python の場所確認
which python   # Mac/Linux  
where python   # Windows
```

**解決方法:**

**Windows:**
1. Python を再インストール
2. **「Add Python to PATH」にチェック**
3. コマンドプロンプトを再起動

**Mac:**
```bash
# python3 を使用
python3 bot.py

# または pyenv を使用
brew install pyenv
pyenv install 3.12.0
pyenv global 3.12.0
```

**Linux:**
```bash
# Python3 をインストール
sudo apt update
sudo apt install python3 python3-pip
```

**予防策:**
- インストール時にPATH設定を必ず確認
- `python3`コマンドも試す

---

## 💬 動作・反応関連の問題

### **Bot がメッセージに反応しない**

**症状:**
- `!ping` コマンドに反応しない
- 自動応答機能が動かない
- Bot はオンラインだが無反応

**診断:**
```bash
# Bot の起動ログを確認
tail -f bot.log

# Discord Developer Portal で Intents 確認
# Bot → Privileged Gateway Intents
```

**解決方法:**
1. **Message Content Intent を有効化**
   - Discord Developer Portal → Bot
   - MESSAGE CONTENT INTENT をON
   - Save Changes
   - Bot 再起動

2. **Bot 権限の確認**
   - サーバーでBot権限を確認
   - 「メッセージの送信」権限が必要

3. **チャンネル権限の確認**
   - Bot がそのチャンネルを見れるか確認
   - プライベートチャンネルの場合は個別権限付与

**予防策:**
- 新しいサーバーに招待時は権限を再確認
- 定期的な権限監査

---

### **コマンドが動かない**

**症状:**
- `!help` に反応しない
- 特定のコマンドだけ動かない
- エラーメッセージも出ない

**診断:**
```python
# bot.py に一時的にデバッグコードを追加
@bot.event
async def on_message(message):
    print(f"メッセージ受信: {message.content}")  # デバッグ
    if message.author.bot:
        return
    await bot.process_commands(message)
```

**解決方法:**
1. **プレフィックスの確認**
   ```json
   // config.json
   {
     "prefix": "!"  // これが正しいか確認
   }
   ```

2. **コマンド構文の確認**
   ```
   正しい: !ping
   間違い: ！ping（全角）
   間違い: ! ping（スペース）
   ```

3. **config.json の features 確認**
   ```json
   {
     "features": {
       "echo": true,  // false だと動かない
       "help": true
     }
   }
   ```

**予防策:**
- コマンドテスト時は大文字小文字に注意
- 定期的な設定ファイル確認

---

### **リアクション機能が動かない**

**症状:**
- 👋 リアクションに反応しない
- リアクション追加は検知されない

**診断:**
```python
# on_reaction_add のデバッグ
@bot.event
async def on_reaction_add(reaction, user):
    print(f"リアクション検知: {reaction.emoji}, ユーザー: {user}")
    # 既存の処理...
```

**解決方法:**
1. **Intents の確認**
   ```python
   # bot.py で確認
   intents.reactions = True  # これが必要
   ```

2. **Bot 権限の確認**
   - 「リアクションの追加」権限
   - 「メッセージ履歴の閲覧」権限

3. **絵文字の種類確認**
   ```python
   # カスタム絵文字の場合は別処理
   if str(reaction.emoji) == '👋':  # 標準絵文字
   if reaction.emoji.name == 'custom_emoji':  # カスタム絵文字
   ```

**予防策:**
- 標準的な絵文字を使用
- カスタム絵文字は慎重にテスト

---

## 📦 依存関係・環境関連の問題

### **ModuleNotFoundError**

**症状:**
```
ModuleNotFoundError: No module named 'discord'
ModuleNotFoundError: No module named 'dotenv'
```

**診断:**
```bash
# インストール済みパッケージ確認
pip list
pip show discord.py

# 仮想環境の確認
which python
```

**解決方法:**
```bash
# 1. 依存関係の再インストール
pip install -r requirements.txt

# 2. 個別インストール
pip install discord.py python-dotenv

# 3. アップグレード
pip install --upgrade discord.py

# 4. 仮想環境の使用（推奨）
python -m venv bot_env
source bot_env/bin/activate  # Mac/Linux
bot_env\Scripts\activate     # Windows
pip install -r requirements.txt
```

**予防策:**
- requirements.txt を最新に保つ
- 仮想環境の使用
- 定期的なパッケージ更新

---

### **pip コマンドが見つからない**

**症状:**
```
'pip' is not recognized as an internal or external command
pip: command not found
```

**解決方法:**

**Windows:**
```cmd
# python -m pip を使用
python -m pip install -r requirements.txt

# pip の再インストール
python -m ensurepip --upgrade
```

**Mac/Linux:**
```bash
# pip3 を使用
pip3 install -r requirements.txt

# pip のインストール
sudo apt install python3-pip  # Ubuntu
brew install python3          # Mac
```

**予防策:**
- Python インストール時に pip も同時インストール
- 複数の Python 環境がある場合は注意

---

## 🆘 緊急時の対処法

### **完全リセット手順**

**全て動かない場合の最終手段:**

```bash
# 1. 環境のクリーンアップ
rm -rf __pycache__/
rm bot.log
rm config.json

# 2. 依存関係の再インストール  
pip uninstall discord.py python-dotenv
pip install -r requirements.txt

# 3. 設定ファイルの再作成
cp .env.example .env
# .env を編集してToken設定

# 4. Bot の再起動
python bot.py
```

### **サポートに連絡する前のチェックリスト**

問題が解決しない場合、以下を準備：

- ✅ **エラーメッセージ全文**
- ✅ **実行環境情報**
  ```bash
  python --version
  pip --version
  cat .env  # Token部分は隠す
  ```
- ✅ **実行した手順**
- ✅ **期待した動作 vs 実際の動作**

---

## 📞 サポート・質問方法

### **Claude.codeに質問する際のテンプレート**

```
【問題】
Bot が○○しない

【エラーメッセージ】
```
エラーメッセージをここに貼り付け
```

【環境】
- OS: Windows 11 / macOS / Ubuntu
- Python: バージョン
- 実行場所: C:\Users\xxx\my-bot\

【試したこと】  
- requirements.txt の再インストール
- .env ファイルの確認
- etc...

【期待する動作】
○○したい
```

### **よくある質問（FAQ）**

**Q: 複数のサーバーで同じBotを使える？**
A: はい。同じBotを複数サーバーに招待できます。

**Q: 24時間稼働させるには？**
A: VPSやクラウドサービスが必要。`deploy/`フォルダを参照。

**Q: コードを改造しても大丈夫？**
A: はい！自由に改造してください。バックアップ推奨。

**Q: Token が漏れたらどうする？**
A: すぐに Discord Developer Portal で Reset Token。

---

**🔧 問題解決のコツ: エラーメッセージをよく読み、一つずつ確認！**

*Troubleshooting Guide Ver.1.0 | 初心者対応版*