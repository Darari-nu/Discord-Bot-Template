# 🔧 Discord Developer Portal 詳細手順書

**Discord Botアプリケーションの作成手順（画像解説付き）**

## 🎯 この手順でできること

- Discord Bot アプリケーションの作成
- Bot Token の取得
- Bot権限の設定
- サーバーへの招待リンク生成

---

## 📋 Step 1: Discord Developer Portal にアクセス

### **1-1. サイトにアクセス**
- URL: https://discord.com/developers/applications
- Discordアカウントでログイン

### **1-2. 画面の確認**
ログイン後、以下のような画面が表示されます：
```
Discord Developer Portal
├── My Applications (左側)
├── New Application (右上の青いボタン)
└── 既存のアプリケーション一覧（初回は空）
```

---

## 🤖 Step 2: 新しいアプリケーションを作成

### **2-1. アプリケーション作成**
1. **「New Application」**ボタンをクリック
2. ポップアップが表示される：
   ```
   CREATE AN APPLICATION
   NAME: [ここにBot名を入力]
   □ I agree to the Discord Developer Terms of Service
   [Cancel] [Create]
   ```
3. **NAME欄**に好きなBot名を入力（例：「My First Bot」）
4. **利用規約にチェック**を入れる
5. **「Create」**をクリック

### **2-2. アプリケーション設定画面**
作成後、以下の画面に移動します：
```
左側メニュー:
├── General Information ← 現在ここ
├── Bot
├── OAuth2
└── その他...

右側エリア:
├── APPLICATION ID: 1234567890... (後で使用)
├── PUBLIC KEY: abcd1234... 
└── DESCRIPTION: Bot の説明（オプション）
```

---

## 🔑 Step 3: Bot ユーザーの作成とToken取得

### **3-1. Botページに移動**
- 左側メニューの**「Bot」**をクリック

### **3-2. Botユーザーを作成**
初回は以下の画面が表示されます：
```
BUILD-A-BOT

You can use bots on Discord to automate tasks and improve your server.

[Add Bot]
```
1. **「Add Bot」**ボタンをクリック
2. 確認ダイアログ：**「Yes, do it!」**をクリック

### **3-3. Bot Token の取得**
Bot作成後、以下のセクションが表示されます：
```
TOKEN
Use this token to give your application access to the Discord API

[Copy] [Regenerate]

⚠️ Warning: Keep your token secret! Anyone with your token can control your bot.
```

**重要な操作：**
1. **「Copy」**をクリックしてTokenをコピー
2. **安全な場所にメモ**（.envファイルで使用）
3. **誰にも教えない**（Tokenは秘密情報）

**Token例：**
```
YOUR_BOT_APPLICATION_ID.TOKEN_PART_1.TOKEN_PART_2_KEEP_THIS_SECRET
```

---

## ⚙️ Step 4: Bot権限の設定

### **4-1. Privileged Gateway Intents の設定**
同じBotページで下にスクロールすると：
```
Privileged Gateway Intents

□ PRESENCE INTENT
   Allows your app to receive presence update events
   
□ SERVER MEMBERS INTENT  
   Allows your app to receive guild member events
   
□ MESSAGE CONTENT INTENT ← これを必ずONに！
   Allows your app to receive message content in guild messages
```

**必須設定：**
- ✅ **MESSAGE CONTENT INTENT** をONにする
- （オプション）SERVER MEMBERS INTENT もONにしてもOK

### **4-2. 設定の保存**
- ページ下部の**「Save Changes」**をクリック

---

## 🔗 Step 5: Bot招待リンクの生成

### **5-1. OAuth2 URL Generator に移動**
- 左側メニュー：**「OAuth2」** → **「URL Generator」**

### **5-2. Scopes の選択**
```
SCOPES
□ applications.commands
□ bot ← これを必ずチェック！
□ connections
□ email
□ identify
□ guilds
□ guilds.join
```
- **「bot」**にチェックを入れる

### **5-3. Bot Permissions の選択**
`bot`をチェックすると下に権限リストが表示されます：

**必須権限（必ずチェック）:**
- ✅ **View Channels** （チャンネルを見る）
- ✅ **Send Messages** （メッセージを送信）
- ✅ **Read Message History** （メッセージ履歴を読む）
- ✅ **Add Reactions** （リアクションを追加）

**推奨権限（あると便利）:**
- ✅ **Embed Links** （埋め込みリンク）
- ✅ **Attach Files** （ファイル添付）
- ✅ **Use External Emojis** （外部絵文字使用）

### **5-4. 招待URLの取得**
権限選択後、ページ下部に**GENERATED URL**が表示されます：
```
GENERATED URL
https://discord.com/api/oauth2/authorize?client_id=1234567890&permissions=274878286848&scope=bot

[Copy]
```
- **「Copy」**をクリックしてURLをコピー

---

## 🎪 Step 6: Botをサーバーに招待

### **6-1. 招待URLにアクセス**
- コピーしたURLをブラウザで開く

### **6-2. サーバー選択**
```
Botを次に追加:
[サーバー選択プルダウン]
- My Server 1
- My Server 2  
- 新しいサーバーを作成
```
- Botを追加したいサーバーを選択

### **6-3. 権限確認**
```
My First Bot が以下の権限を要求しています:

✅ チャンネルを見る
✅ メッセージを送信する  
✅ メッセージ履歴を読む
✅ リアクションを追加する

[キャンセル] [認証]
```
- 権限を確認して**「認証」**をクリック

### **6-4. 招待完了**
```
成功！
My First Bot があなたのサーバーに追加されました。
```
- Discord サーバーでBotがオフライン状態で表示される

---

## ✅ 設定完了チェックリスト

完了後、以下を確認してください：

### **Discord Developer Portal側:**
- ✅ アプリケーションが作成済み
- ✅ Botユーザーが作成済み  
- ✅ Bot Token をコピー済み
- ✅ MESSAGE CONTENT INTENT がON
- ✅ 招待URL を生成済み

### **Discord サーバー側:**
- ✅ Bot がサーバーメンバーリストに表示
- ✅ Bot がオフライン状態（正常）
- ✅ Bot に必要な権限が付与済み

---

## 🔄 Token を忘れた/紛失した場合

### **Tokenの再生成手順:**
1. Discord Developer Portal → あなたのアプリ → Bot
2. TOKEN セクションで**「Regenerate」**をクリック
3. 確認ダイアログで**「Yes, do it!」**
4. 新しいTokenを**「Copy」**
5. `.env`ファイルを新しいTokenで更新
6. Bot を再起動

⚠️ **注意:** Token を再生成すると、古いTokenは無効になります。

---

## 🚨 よくある間違い

### **1. Message Content Intent を有効にしていない**
**症状:** Botがメッセージに反応しない
**解決:** Bot設定でMESSAGE CONTENT INTENTをONにする

### **2. 権限不足**
**症状:** Botがメッセージを送信できない
**解決:** 招待時に適切なBot権限を選択する

### **3. Token の間違い**
**症状:** 「Bot Tokenが無効です」エラー
**解決:** Token を再コピーするか、再生成する

### **4. 招待リンクの権限不足**
**症状:** 一部機能が動かない
**解決:** 新しい招待リンクを生成し、Botを一度キック→再招待

---

## 🎯 次のステップ

Discord側の設定が完了したら：
1. **SETUP_GUIDE.md** の「Step 3: Botファイルの準備」に進む
2. `.env`ファイルに取得したTokenを設定
3. `python bot.py` でBot起動

---

**🎉 Discord Bot アプリケーションの設定完了！**

*Discord Setup Guide Ver.1.0 | Discord Developer Portal 対応版*