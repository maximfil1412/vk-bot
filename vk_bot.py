from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, \
                                    Text, OpenLink, Location, EMPTY_KEKEYBOARD

bot = bot(token=)



@bot.on.private_message()
async def handler(message: Начать):
    admin_page = Keyboard()
    keyboard.add(Text("Страница владельца"), color=KeyboardButtonColor.POSITIVE)

    moder_help = Keyboard()
    keyboard.add(Text("Помощь млдератора"), color=KeyboardButtonColor.POSITIVE)
    
    cooperation = Keyboard()
    keyboard.add(Text("Сотрудничество"), color=KeyboardButtonColor.POSITIVE)

    buy_product = Keyboard()
    keyboard.add(Text("Купить товар"), color=KeyboardButtonColor.POSITIVE)



        await message.answer("Страница владельца сообщества:\nhttps://vk.com/official.edikso2", admin_page=keyboard)
        await message.answer("Опишите в краткой форме вашу проблему чтобы вас обслужили как можно быстрее", moder_help=keyboard)
        await message.answer("Для быстрого обслуживания вашей просьбы, прошу вас описать тип сотрудничества который вас интересует! В скором времени вам напишет владелец сообщества", cooperation=keyboard)
        await message.answer("Чтобы приобрести товар от сообщества, просьба заказывать через магазин вк. Заходите на товар, ложите в корзину и оплачиваете если данная услуга платная! Так же, иногда модераторы сообщества кидают промокоды на скидку или бесплатный предмет из товаров, следите за сообществом и за новостями!", buy_product=keyboard)





bot.run_forever()