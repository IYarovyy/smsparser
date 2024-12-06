def str_start_validator(time, sender, recipient, text, lac, cell, address):
    invalid_starts = [
        "web_connect resp",
        "Код авторизації дій в системі eHealth:",
        "REG-REQ",
        "Тревога.Охр.зона",
        "Code Ver:",
        "+RESP:",
        "iMetos Alarm Service",
        "GPS:",
        "Bat:",
        "Param ID",
        "GETSET",
        "New value ",
        "atc res:",
        "InCars:",
        "PAYTEST ",
        "Привет! Пообщаемся в Viber? ",
        "Спілкуймось у Viber. Я пишу й безкоштовно",
        "ограмі. Ось посилання https://vb.me",
        "Я пользуюсь Viber для сообщений и бесплатных звонков",
        "Привіт, переходьмо на Viber. ",
        "VIP ACCESS ",
        "PRIVATE ZONE ",
        "VERIFY NUMBER ",
        "‎Let's chat on WhatsApp!",
        "‎Приєднуйтеся до WhatsApp!",
        "Приєднуйтеся до WhatsApp! Завантажте на сайті https:",
        "‎WhatsApp — звонки и сообщения. Бесплатно: ",
        "‎Chatten wir auf WhatsApp! Damit können wir uns schnell, einfach",
        "WhatsApp — звонки и сообщения. Бесплатно:",
        "Привет, я использую Telegram для переписки",
        "Привіт, я користуюся Telegram для спілкування. ",
        "его можно здесь: https://telegram.org",
        "ити тут: https://telegram.org",
        "Привет, я использую Telegram X для переписки. Присоединяйся",
        "//telegram.org/dlx",
        "Добавьте меня в Meet, и мы сможем общаться ",
        "https://vb.me/letsUseViber",
        "Привет, я использую VK Мессенджер для переписки. Присоединяйся!",
        "Я хочу посмотреть видео.#",
        "SOS! (",
        "IDENTIFICATION SMS\\n\\nWeather station",
        "GSM связь восстановлена",
        "AC/",
        "ALARM GUARD; ",
        "$GPRMC,",
        "Код получения ",
        "Vash odnorazoviy parol: ",
        "Привіт, переходьмо на Vibрп https",
        "Післязавтра знімається оплата за тариф",
        "Спасибо, что позволили мне ввести код проверки ",
        "нтификатор пользователя",
        "SET OK",
        "imsi=",
        "BPL\\n",
        "BIRD-LK ",
        "CMD RESTART",
        "Оповещение о смене SIMОт",
        "Попробуйте Messenger: https://fb.me/getmessenger",
        "  setparam ",
        "ERR:Bad Synta",
        "Server Domain Name:",
        "Выбран ответ: ",
        "Я выбираю вариант ",
        "Я настоящий, я не робот",
        "Я не бот, я настоящий пользователь ",
        "Мой доступ готов с моим номером ",
        "Мои учетные данные ",
        "Позвольте мне продолжить ",
        "Я хочу продолжить ",
        "Так я хочу отримати свій приз",
        "Access content  ",
        "STR",
        "Ожидайте СМС с местоположением ",
        "<PM0>",
        "CAN VIN",
        "Добавьте меня в Duo,",
        "Chatid:",
        "Я вижу игрушки на картинке. Мой код",
        "[TikTok] Мой аккаунт в TikTok ",
        "Rav4\\n",
        "RTC:",
        "Збережіть це повідомлення.Від:",
        "Let's chat on Viber. It's my main app for messaging and free calls. Here's the link https://vb.me/letsUseViber",
        "номеромПожалуйста проинформируйте ",
        "<!> Сработала зона предупреждения",
        "Для поновлення вигідних умов вашого тарифу поповніть рахунок",
        "+ACK:GTGBC"
    ]
    return all(not text.startswith(invalidStart) for invalidStart in invalid_starts)


def str_contains_validator(time, sender, recipient, text, lac, cell, address):
    invalid_contains = [
        " Моє ім'я :",
        " Моя відповідь: ",
        " Моя домашня адреса : ",
        " Так, я хочу отримати свій приз!",
        "nNOGUARD",
        "https://duo.app.goo.gl"
        "https://whatsapp.com/dl",
        "https://telegram.org/dl",
        "https://vb.me/switchToViber",
        "nGPS_LEN",
        "Низкий баланс лицевого счета",
        " WAW-TLL ",
        "дочекайтесь SMS про нарахування пакету послуг. Поповнити",
        "SIM1TEL=+ ",
        " gsa=",
        " gde",
        " мой идентификатор доступа ",
        "Код подтверждения:",
        "Neispravnost' seti",
        "Razryajen akkumulyator",
        "Vosstanovlenie seti",
        "Zaryajen akkumulyator",
        "Izmeneniye Vremeni",
        "Verification code is",
        ". Я настоящий человек.",
        "BankKarti zablokirovanomtsbank.ru",
        "Телефон был украден, используется с",
        " ОШИБКА! Указан неверный пароль!",
        "згода на обробку персональних даних https:"
    ]
    return all(text.find(invalid_contain) == -1 for invalid_contain in invalid_contains)


def recipient_validator(time, sender, recipient, text, lac, cell, address):
    invalid_recipients = [
        "900",
        "3003",
        "9100",
        "95746",
        "2500",
        "999",
        "2283",
        "32858",
        "1212",
        "333",
        "9560",
        "9575",
        "987",
        "4719",
        "4730",
        "4811",
        "9553"
    ]
    return all(recipient != invalid_recipient for invalid_recipient in invalid_recipients)


def empty_validator(time, sender, recipient, text, lac, cell, address):
    return \
            time != "" and \
            sender != "" and \
            recipient != "" and \
            text != "" and \
            lac != "" and \
            cell != "" and \
            address != ""


validators = [empty_validator,
              recipient_validator,
              str_start_validator,
              str_contains_validator]


def is_valid(time, sender, recipient, text, lac, cell, address):
    return all(valid(time, sender, recipient, text, lac, cell, address) for valid in validators)
