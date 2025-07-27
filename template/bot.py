#!/usr/bin/env python3
"""
🤖 Discord Bot Template - メインBot

Discord Bot開発の学習・開発用テンプレート
このファイルから開始して、段階的に機能を追加していきます。

使い方:
1. .envファイルにBOT_TOKENを設定
2. python bot.py で起動
3. Claude.codeに「○○の機能が欲しい」と依頼して機能追加

Author: Discord Bot Template
Version: 1.0.0
"""

import discord
from discord.ext import commands
import os
import json
import logging
from pathlib import Path
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 設定ファイル読み込み
def load_config():
    """設定ファイルを読み込む"""
    config_path = Path('config.json')
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # デフォルト設定
        default_config = {
            "bot_name": "Template Bot",
            "prefix": "!",
            "features": {
                "echo": True,
                "help": True,
                "reactions": True
            },
            "embed_color": 0x00ff00
        }
        # 設定ファイルを作成
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        logger.info("デフォルト設定ファイル config.json を作成しました")
        return default_config

# 設定読み込み
config = load_config()

# Bot設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容を読み取るために必要
intents.reactions = True        # リアクション機能のために必要

bot = commands.Bot(
    command_prefix=config['prefix'], 
    intents=intents,
    help_command=None  # デフォルトのhelpコマンドを無効化
)

# Bot起動時のイベント
@bot.event
async def on_ready():
    """Botが起動した時に実行される"""
    logger.info(f'{bot.user} としてログインしました')
    logger.info(f'Bot名: {config["bot_name"]}')
    logger.info(f'コマンドプレフィックス: {config["prefix"]}')
    logger.info(f'サーバー数: {len(bot.guilds)}')
    
    # アクティビティ設定
    activity = discord.Game(name="Template Bot 稼働中")
    await bot.change_presence(activity=activity)

# エラーハンドリング
@bot.event
async def on_command_error(ctx, error):
    """コマンドエラーが発生した時の処理"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ コマンド `{ctx.invoked_with}` は見つかりません。`{config['prefix']}help` でヘルプを確認してください。")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ 必要な引数が不足しています。`{config['prefix']}help {ctx.command}` で使い方を確認してください。")
    else:
        logger.error(f"エラーが発生しました: {error}")
        await ctx.send("❌ エラーが発生しました。管理者に報告してください。")

# === 基本機能 ===

@bot.command(name='ping')
async def ping_command(ctx):
    """Bot応答テスト"""
    latency = round(bot.latency * 1000)
    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"レイテンシ: {latency}ms",
        color=config['embed_color']
    )
    await ctx.send(embed=embed)

@bot.command(name='echo')
async def echo_command(ctx, *, message):
    """メッセージをエコー（繰り返し）する
    
    使い方: !echo こんにちは
    """
    if not config['features']['echo']:
        await ctx.send("❌ エコー機能は無効になっています。")
        return
    
    embed = discord.Embed(
        title="📢 エコー",
        description=message,
        color=config['embed_color']
    )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_command(ctx, command_name=None):
    """ヘルプを表示する"""
    if not config['features']['help']:
        await ctx.send("❌ ヘルプ機能は無効になっています。")
        return
    
    if command_name:
        # 特定のコマンドのヘルプ
        command = bot.get_command(command_name)
        if command:
            embed = discord.Embed(
                title=f"📚 コマンド: {config['prefix']}{command.name}",
                description=command.help or "説明がありません",
                color=config['embed_color']
            )
            if command.usage:
                embed.add_field(name="使い方", value=f"`{config['prefix']}{command.usage}`", inline=False)
        else:
            embed = discord.Embed(
                title="❌ エラー",
                description=f"コマンド `{command_name}` は見つかりません。",
                color=0xff0000
            )
    else:
        # 全コマンドのヘルプ
        embed = discord.Embed(
            title=f"📚 {config['bot_name']} ヘルプ",
            description="利用可能なコマンド一覧",
            color=config['embed_color']
        )
        
        # コマンドをカテゴリ別に整理
        commands_list = [
            f"`{config['prefix']}ping` - Bot応答テスト",
            f"`{config['prefix']}echo [メッセージ]` - メッセージをエコー",
            f"`{config['prefix']}help [コマンド名]` - ヘルプ表示",
        ]
        
        embed.add_field(
            name="基本コマンド", 
            value="\n".join(commands_list), 
            inline=False
        )
        
        embed.add_field(
            name="リアクション機能", 
            value="メッセージに👋でリアクションすると挨拶を返します", 
            inline=False
        )
        
        embed.set_footer(text=f"詳細: {config['prefix']}help [コマンド名]")
    
    await ctx.send(embed=embed)

# === リアクション機能 ===

@bot.event
async def on_reaction_add(reaction, user):
    """リアクションが追加された時の処理"""
    if user.bot:  # Bot自身のリアクションは無視
        return
    
    if not config['features']['reactions']:
        return
    
    # 👋 リアクションに対する応答
    if str(reaction.emoji) == '👋':
        await reaction.message.channel.send(f"👋 こんにちは、{user.mention}さん！")

@bot.event
async def on_message(message):
    """メッセージが送信された時の処理"""
    if message.author.bot:  # Bot自身のメッセージは無視
        return
    
    # 特定のキーワードに自動応答
    if 'おはよう' in message.content.lower():
        await message.channel.send(f'おはようございます、{message.author.mention}さん！ ☀️')
    elif 'おやすみ' in message.content.lower():
        await message.channel.send(f'おやすみなさい、{message.author.mention}さん！ 🌙')
    
    # コマンド処理を継続
    await bot.process_commands(message)

# === メイン実行部 ===

def main():
    """メイン実行関数"""
    # Bot Token取得
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        logger.error("DISCORD_BOT_TOKENが設定されていません。.envファイルを確認してください。")
        return
    
    try:
        logger.info("Botを起動しています...")
        bot.run(token)
    except discord.LoginFailure:
        logger.error("Bot Tokenが無効です。正しいトークンを設定してください。")
    except Exception as e:
        logger.error(f"Botの起動に失敗しました: {e}")

if __name__ == "__main__":
    main()