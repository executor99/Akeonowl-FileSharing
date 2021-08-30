# @ZonaKimochi Copyright
from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/ZonaKimochi).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**🚨 Silahkan Join Terlebih Dahulu Ke Channel @videotiktok69 Untuk MengAkses File nya,Jika Tidak Join Maka Akses BOT Di Tolak!**\n\n Hanya yang Sudah Join Dapat Menggunakan Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Gabung Update Channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Muat Ulang File 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Terjadi Kesalahan. Contact my [Support Group](https://t.me/penikmatmemew).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
