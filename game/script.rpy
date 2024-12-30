﻿define e = Character('Костя', color="#FFFFFF", image="..")
define k = Character('Коля', color="0000FF", image="kol")
define v = Character('Вова', color="FF0000", image = "vova")
define g = Character('Голоса в голове!?', color="#9400D3", image="..")
define n = Character('Неизвестный номер', color="#696969", image="..")
define b = Character('Вирус', color = "#44944A", image = "zlo")


define successCount = 0
define healthCount = 100
define greenCount = 0




# Игра начинается здесь:
label start:
    play music misunderstanding
    
    "Что же теперь...? "
    "..."
    "Чувство свободы смешивается с неопределённостью."
    "..."
    "С одной стороны, можно расслабиться и отдохнуть после всех этих бессонных ночей и нервных моментов."
    "..."
    "Но с другой — впереди лето, и как же его провести?"
    "Я вспоминаю, сколько времени потратил на учёбу, и сейчас, когда всё позади, я не знаю, чем заняться."
    "..."
    "Может, стоит встретиться с друзьями?"
    "..."
    "Погулять по городу, сходить в кино или просто посидеть в кафе?"
    "Но ведь я хочу сделать что-то значимое, что-то, что запомнится."
    "Куда бы я хотел пойти?"
    "Кем я хочу стать?"
    "Сейчас время подумать, время действовать."
    "С этой мыслью я прихожу в себя...."

    scene bg uni
    with fade
    play music peaceful

    "Что-то я совсем погрузился в свои мысли."

    "Наконец-то я написал этот гребанный последний экзамен, но что же мне сейчас делать?"

    "Этот преподаватель был просто ужасен, столько людей завалил!"

    "У него такие жесткие требования, что даже самые подготовленные не могли с ним справиться."

    "Поеду-ка пока домой и потом подумаю над тем, что же дальше делать."

    scene bg room
    with fade

    "..."

    play sound "sms.ogg"

    window show
    "У вас новое сообщение!"
    v "Васап, бро! У нас тут этажом выше празднуют окончание первого курса, давай подлетай."
    e "Ща буду, брачо."
    "Кстати, может, у наставника спросить, чем заняться? Возможно, что-то хорошее посоветует."
    "Как раз схожу на вечеринку в честь окончания первого курса, ну надо же как-то это отметить."
    e "Блин, надо хоть немного расслабиться, пойду пообщаюсь с ребятами, да и музыку послушаю."
     
    window hide

    pause 2.0

    scene bg party
    show kol at left
    with fade
    play music party

    e "Вова, а ты уже знаешь, чем заняться летом?"

    v "Да, я стажируюсь в одной из IT-компаний уже год."

    v "Там неплохо платят, а мне как раз коплю деньги, чтобы закрывать аренду квартиры. Плюс это для меня как дополнительная практика."
    
    v "Если хочешь чем-то заняться, можешь тоже пойти на стажировку."

    e "Блин, крутая мысль! Я как раз думал, как не пропустить лето. Может, тоже попробовать?"

    "Подумаю над этим дома."

    v "А ты смотрел новости? Там говорят, что что-то непонятное происходит в главном офисе Wargaming"

    v "Вход и окна здания полностью закрылись, и люди странно там начали себя вести, не разговаривают и не хотят открывать дверь"

    e "Нет, не слышал. Да бред какой-то, наверное, опять очередной розыгрыш от этой компании. Скоро же день независимости."

    v "Я тоже так думаю."

    stop music

    play music peaceful
    scene bg room
    with fade

    "Так, теперь надо решиться, проспать мне всё лето или же попробовать что-то новое?"

    menu:

        "Что ты хочешь сделать дальше?"
        
        "Не хочу эти стажировки":

            jump end_1

        "Пойду все таки на стажировку":

            jump continue_1

label end_1:

    e "не хочу ничего делать!"

    $ renpy.notify("Получено достижение - Ленивец")

    pause
    
    return

stop music
scene 



label continue_1:

    "здесь будут еще реплики..."

    "....."

    scene bg room
    with fade

    e "Настало время поменять свою жизнь!"

    "Я нашёл 3 IT компании (кисулькиIT, шутерPK, мышьIT)"

    "Таак, тут нужно написать какими языками программирования я владею и какие проекты я делал."

    "Может все те проекты связанные с DevOps, над которыми я работал, мне сейчас пригодятся"

    "Сейчас бы еще вспомнить чем я там занимался..."

    scene
    with fade
    play music scary
    

    "......"

    g "Пути, по которым ты идешь, будут освещаться лишь отражениями твоих слов..."

    "....."

    g "Не забывай, что следы, оставленные в песке, могут измениться, если ветер изменит свой путь."

    "...."

    e "Что это сейчас было....?"

    g "Чувак сохраняйся и думай над выбором"

    e "Походу я совсем крышей поехал"

    stop music

    scene bg room
    with fade

    e "Так ладно, сейчас нужно просто заполнить портфолио для стажировки"

    

    menu:
        "На каких языках я прогал?"
        
        "Bash, Ruby, Pearl":
            $ successCount += 2
            "Они все используются в девопсе, отлично!"
        "Swift,Haskell,Scala":
            $ successCount += 0
            "Сомневаюсь что я найду им применение.... Очень специфичные языки"
        "Java,С#,PHP":
            $ successCount += 1
            "Думаю что в каких то проектах они точно понадобятся!"
    

    

    menu:
        "Чем же я там занимался?"

        "Разработка чат-бота с использованием NLP":
            $ successCount += 1
            "Помню было такое...."
            "Думаю такой проект может показать мои знания в программировании"
        "Создание прототипа для нового веб-сайта с использованием Figma или Sketch":
            $ successCount += 0
            "Помню было такое...."
            "Сомневаюсь что это как то пригодится, но лучше чем ничего"
        "Автоматизация развертывания приложения с CI/CD в облаке.":
            $ successCount += 2
            "Это как раз по моей специальности, то что надо!"


    "Фухх, наконец то все заполнил и отправил, надеюсь меня пригласят на собеседование."

    "Блин, что-то поздно уже, пора ложиться спать и ждать завтрашнего дня."

    scene 
    with fade

    "…"

    "Проходит неделя…"

    "…"

    play music phone

    "…"

    pause 3.0

    "Кто решил меня с утра пораньше разбудить…"

    "Похоже, опять мошенники звонят. Сгораю от интереса послушать, что на этот раз…)"

    stop music

    e "Слушаю."

    n "Здрасте, это… Костантин Огузков, правильно?"  
    n "Или, эм… оговорился?"

    e "Он самый."

    n "А, ну, супер!"  
    n "Это… мы вас ждём на собеседовенее."  
    n "Ой, на собеседовании, конечно же!"  
    n "Вы, наверно, застряли в пробкех?"  
    n "Пробки, в смысле. Это… бывает."

    "Похоже, я совсем забыл проверить почту…"

    e "Да! Да! Тут невероятный затор, буквально 20 минут, и я буду!"

    n "Двадцать... минут? У-уф, это долго."  
    n "Хотя нет, нормально, наверное?"  
    n "Только быстрее, если можно!"  
    n "Не то, ну, хе-хе, директор рассердится, знаете…"  
    n "Хотя он и так злой… ой!"  
    n "Ой, не это хотел сказать! Всё-всё хорошо."

    e "…Эм, понял. Буду как можно скорее."

    n "Да-да, спасибо, спасибо."  
    n "Ждём... мы... э-ээ, с кофе!"  
    n "Ой, без кофе. Просто ждём."  
    n "Вы постарайтесь, пожалуйста, ага?"

    e "Похоже, они сбросили звонок… Странно, ну да ладно."

    "Так, вызываю такси и быстренько одеваюсь."

    "…"



    scene

    "Как же я волнуюсь…"

    "Ещё и этот фейл с почтой."

    "Ладно, у меня всё получится."

    scene bg ent
    with fade

    e "Ну чтож, вперед!"

    scene entrance
    with fade

    "Я захожу в здание, как вдруг дверь за моей спиной громко захлопывается."

    play music dver

    "..."

    stop music
    
    play music scary

    e "Что это было?"  
    e "Наверное… так и должно быть. Автоматические двери или что-то такое."  

    "Я оглядываюсь вокруг."  

    e "Блин, а где все?"  
    e "Я думал, тут меня кто-то встретит. А, ну правильно, я же опоздал."  

    "Ничего не подозревая, я направляюсь к ресепшену. Но вдруг…"  

    "Я в шоке. Передо мной женщина, которая лежит без сознания за стойкой."  

    e "Что за… Она без сознания?!"  

    "Я торопливо подбегаю к женщине, пытаясь привести её в чувство, и начинаю звать на помощь."  

    e "Эй! Вы слышите меня? Кто-нибудь! Помогите!"  

    "Но никто не отвечает, и женщина продолжает лежать неподвижно."  

    "Я достаю телефон и набираю скорую."
    "Однако, как только звонок начинает идти, связь резко обрывается." 

    e "Чёрт! Связь пропала?!"  

    "Я оборачиваюсь и замечаю мониторы, висящие на стене. На них виден весь этаж."  

    "На экранах я вижу странное: часть людей лежит без сознания, а некоторые... двигаются, но неестественно."
    "Их движения чёткие, механические. А ещё..."  

    e "Они… без зрачков?! Что за черт?! Они как… как зомби?!"  
    e "И ходят только группами… Господи, это что, какой-то странный розыгрыш?!"  

    "Дрожащими руками я достаю телефон и проверяю звонки."  
    "Вижу, что мне недавно звонил мой наставник. На автоответчике оставлено голосовое сообщение."  

    "Сообщение от Вовы:"  

    v "Алё! Не заходи в здание! Ты меня слышишь? Тут какой-то кошмар творится!"  
    v "Помнишь новость, которую я тебе неделю назад рассказывал? Это был не фейк!"  
    v "Это всё реально! Если ты уже внутри, то слушай внимательно: ПРЯЧЬСЯ!!!"  

    "Я резко осматриваюсь вокруг и замечаю шкаф возле лестницы."
    "Торопливо открываю его, залезаю внутрь и начинаю читать дальше сообщение."  

    scene second
    with fade

    "Я поднимаюсь на второй этаж и вдруг вокруг наступает странная тишина."  
    e "Что за... Почему все замолчали?"  
    "Некоторые люди падают на пол, лежат без сознания, а другие…"  
    e "Они… превращаются в зомби?! Как это возможно?!"  

    "Я замечаю, что все, кто стал зомби, сидели за компьютерами. Я пытаюсь обратиться к ним."  
    e "Эй! Вы меня слышите?!"  
    "Но никакого ответа. Вдруг они резко набрасываются на моего друга, который шел со мной."  
    e "Нет! Черт… Ему не помочь…"  
    "Я, не оглядываясь, бегу прочь."  

    "Прячусь в укромном месте, достаю телефон и пробиваю камеры."  
    e "Так… это вирус. Он действует через компьютеры прямо на мозг!"  
    e "И этими зомби управляет этот вирус… Черт возьми!"  

    "Сообщение от Вовы:"  
    v "Я тут понял одну вещь. Я спрятался на втором этаже, во втором отсеке, в комнате для уборочного инвентаря."  
    v "Этот вирус заражает через главный компьютер."
    v "Я попробую сделать антивирус — он временно заморозит систему, чтобы её можно было перезагрузить. Это должно очистить главный ПК."  
    v "Твоя задача — найти момент и подняться ко мне. Но будь предельно осторожен, похоже, что всех, кто не сидел за компьютерами, уже схватили."

    e "От такого количества информации уже мозг кипит… Ладно, суть я вроде понял. Но как мне тайминги-то поймать?! Что здесь вообще творится?!"  

    "Я осматриваюсь вокруг."  
    e "Вроде никого… Похоже, чисто. Ладно, пора быстро подняться на второй этаж."  
    "Я вспоминаю сообщение."  
    e "Так, он говорил, что находится справа от лестницы… Но сначала нужно осмотреться и прислушаться."  

    "Вдруг слышны шаги."  
    e "Кто-то идёт… Похоже, прямо в мою сторону! Надо срочно спрятаться!"  


    menu:
        "Куда спрятаться?"

        "Быстро запрыгнуть за диван.":
            "Сомневаюсь что меня тут найдут."
            jump continue_2
        "Не буду вдруг это кто то добрый.":
            jump end_2
        "Запрыгнуть под офисный стол.":
            "Сомневаюсь что меня тут найдут."
            jump continue_2

label end_2:
    "Похоже это несколько врагов..."
    e "Думаю это мой конец."
    $ renpy.notify("Получено достижение - Доверчивый")
    pause
    return



label continue_2:
    e "Ага, они реально ходят только группами… Но, похоже, они не очень внимательные."  
    e "Пора идти дальше. Вроде, они ушли."
    scene cor
    with fade
    e "О, первый отсек. Наставник говорил, что он находится на втором. Значит, я в правильном направлении."  
    e "Блин, похоже, дальше просто так не пройти. Нужно выбрать, что делать дальше."  

    "Вдруг я слышу сзади звуки шагов, а спрятаться тут негде."  
    e "Это что, опять они? Надо быстрее решиться!"

    menu:  
        "Что делать?"

        "Попытаться силой открыть вентиляционный люк.":  
            "Я подхожу к вентиляционному люку и пытаюсь его открыть, но…"  
            e "Черт, он слишком крепкий! У меня не хватает сил…"  
            "В этот момент меня ловят."  
            jump end_3  
        "Разбить окно стулом из соседней комнаты.":  
            "Я хватаю стул из соседней комнаты и со всей силы бью по окну. Стекло разбивается, и я выбираюсь наружу."
            $ successCount += 2  
            jump continue_3  
        "Попытаться взломать дверь.":  
            if successCount > 2.5:  
                jump success1
            else:
                jump lowskill1


label success1:
    "Я начинаю взламывать дверь, но это занимает слишком много времени."
    "Но благодаря своим знаниям у меня все таки получается!"
    e "У меня получилось взломать дверь!"
    jump continue_3

label lowskill1:
    "Я начинаю взламывать дверь, но это занимает слишком много времени."  
    e "Давай же, давай! Почти получилось…"  
    "Но шаги становятся всё ближе, и меня ловят."
    jump end_3
    


label end_3:
    e "Похоже, это конец…"  
    $ renpy.notify("Получено достижение - Слабак ")  
    pause  
    return

label continue_3: 
    e "Черт! Шум привлек их внимание!"  
    "Зомби замечают меня и устремляются в погоню."  

    "Тем временем Вова, услышав странный звук, выглядывает из своей комнаты и замечает меня."
    show kol at right #(_fps=10., glitch_strength=.1, color_range1="#0a00", color_range2="0f0")
    with fade
    v "ЗАКРЫВАЙ ДВЕРЬ, ТУТ ИХ ОЧЕНЬ МНОГО ЗА МНОЙ!"   
    "Я резко забегаю внутрь, и Вова захлопывает дверь, запирая её."  

    e "Фух… Чуть не попались!"    
    e "Что тут, мать твою, происходит?!"  
    v "Я сам в шоке, но, похоже, этот офис и всех этих людей можем спасти только мы."  
    v "Я уже почти закончил писать код. Времени терять нельзя — нас скоро найдут."  
    v "Нужно попасть на четвёртый этаж и запустить программу на главном серверном компьютере."  
    e "Да, но как мы пройдём через всю эту толпу?"  
    v "Не волнуйся, у меня есть идея."  
    v "Я давно здесь работаю и знаю все проходы, но для этих путей нужен ключ."
    v "Проблема в том, что у меня их нет, и придётся тебе взламывать двери."  
    v "Я слышал, ты этим увлекался?"
    hide kol
    with dissolve
    scene
    with fade
    "..."
    "..."
    "..."
    v "Я доделал код, пора спешить, пока нас не поймали."
    scene cor
    with fade

    "Я осматриваюсь вокруг, никого не видно."  
    e "Вперед, вперед!" 

    v "Это третий отсек второго этажа. Пробежав его, мы выйдем на лестницу, которая ведёт на третий этаж."
    v "Но проблема в том, что по пути будут двери, которые просто так не открыть."  
    v "Вот, например, эта дверь."  

    e "Не проблема, я знаю способ."  
    e "Дай-ка свой ноутбук."  
    e "Сейчас попробую через уязвимость на сервере зайти в систему безопасности и незаметно открыть дверь."
    e "Как-то же он сюда попал, значит, и мы сможем."  
    e "Я как раз занимался этим, пока ты дописывал антивирус."  

    v "Ого! И ты этому научился всего за год учёбы в УРФУ на ИБшника?"  

    e "Не всё так просто. Кроме университета, я ещё много учился сам."  
    e "С детства мне это было очень интересно."  

    e "Всё, вроде готово. Я подключился к серверу… Надеюсь, вирус меня не заметил."

    play music dver

    "..."

    stop music

    v "Вау, да ты крут!"  
    e "Хехе."
    scene boss
    with fade

    e "Что это?!"  
    "Я слышу звуки зомби со всех сторон."  
    e "Нам нужно срочно спрятаться!"
    show zlo
    with fade
    b "Ахахахаха, вот и закончился ваш путь!"  
    "Зомби окружили нас со всех сторон."  
    v "Я так понимаю, ты и есть вирус?"  
    b "Да, всё верно."  
    b "Ты хорошо спрятался, мальчик. Я бы тебя не нашёл, если бы не этот сопляк."
    b "Ахахахаха, с самого начала его пути я следил за ним, и не зря!"  
    b "Вы глупые создания, даже не додумались, что я владею всеми камерами в этом здании... Ахахаха!"  

    e "Блин, жесткий провал."  
    e "Ну что ж, похоже, нам пришёл конец, друг мой."  

    b "Но меня впечатлил этот мальчик, который смог каким-то образом открыть эту дверь."
    b "Мне даже стало интересно, как он это сделал."  
    b "Поэтому я дам вам шанс... Ахахаха! Попробуйте добраться до меня, если не умрёте по пути."  
    b "Хочу поиграть с вами... Ахахаха! Увидимся на следующем этаже!"
    e "Похоже, я только что наложил в штаны."  
    e "Какой жуткий тип…"  

    v "Вот это мы попали… что-то мы явно не продумали."  
    v "Но теперь нам нечего терять. Пора идти вперёд."  
    v "Попробуем пройти его испытания."
    hide zlo
    with dissolve
    scene office
    with fade

    e "И что, куда дальше?"  
    v "Смотри,"  
    v "Если направо — путь вроде как короче, но намного опаснее"  
    v "Но ты же понимаешь, там наверняка какие-то пакости или ловушки."
    e "О, ну конечно, как же без этого. А если налево?"
    v "Налево будет длиннее."
    v "Решай, у нас времени мало."
    menu:
        "Куда пойдем?"

        "Идем направо":
            "Я верю в свои силы, так что лучшее пойдем быстрее"
            if successCount > 3.5:  
                jump success2
            else:
                jump lowskill2


        "Идем налево":
            e "Лучше уж долго но зато безопасно."
            jump continue_4

label lowskill2:
    "Зайдя в комнату я не заметил расставленных ловушек и врагов которые спрятались"
    e "Похоже это наш конец..."
    $ renpy.notify("Получено достижение - Это была ловушка ")
    pause
    return

label success2:
    "Слегка приоткрыв дверь я понял что здесь что то не так"
    e "Не стоит нам идти сюда"
    e "Я вижу ловушки и мне кажется в этой комнате будет облава"
    jump continue_4

label continue_4:
    show zlo at right
    with fade
    b "Ну привет, я подготовил комнату для испытания, но вы не сможете пройти дальше."
    b "Удачи не умереть .. АХАХАХАХ"
    e "Это что за большая летающая машина…"
    v "Нам нельзя терять время Костя. Пора действовать."
    v "Я возьму на себя внимание дрона, а ты пока попробуй взломать его."
    e "Ок будет сделано."
    v "Ого, он оснащен пушками, нужно быть осторожней."
    v "Костя, сколько времени потребуется, чтобы его хакнуть?"
    e "Не знаю, я никогда не взламывал роботов."
    v "Давай быстрее, а то я похоже долго не протяну."
    e "Не попадайся под огонь, просто тяни время"
    v "Сам знаю"
    "О нет, похоже он приближается."
    hide zlo
    with dissolve
    menu:
        "Что делать?"
        "Зайти за угол.":
            e "Не буду рисковать, лучше спрячусь."
            e "Так вроде увернулся от его атаки."
            $ successCount += 1

        "Подобрать трубу и попробовать ударить дрон":
            e "Сейчас я разберусь с ним!"
            "..."
            "Дрон попадает в ногу Косте"
            $ healthCount -= 25
            e "Ай, как же больно"
            v "Ты в порядке?"
            e "Пойдет, только теперь буду хромать"

    "..."
    v "Опять он приближается."
    menu:
        "Что делать?"
        "Спярятаться за креслом.":
            "Пули пробили кресло..."
            "И ранили Костю"
            $ healthCount -= 25
            if healthCount > 74:
                e "Ай, как же больно"
                v "Ты в порядке?"
                e "Пойдет, только теперь буду хромать"
            else:
                e "Кх..."
                e "Опять он в меня попал..."
                v "Ты в порядке?"
                e "Не очень, но дальше смогу идти."
        "Спрятаться за железной пластиной":
            $ successCount += 1
            "Пули не смогли пробить железную пластину"
            e "Фух, хорошо"

    "Робот резко перестает стрелять"
    v "Ура, получилось."    
    if healthCount < 76:
        e "Ты не мог побыстрее? Ты видел? я чуть не помер."
    else:
        e "Отлично я даже ссадины не получил!"
    v "Пошли в другой отсек."
    scene entrance
    with fade
    show kol at left
    show zlo at right
    "..."
    b "Поздравляю!"
    b "Первое испытание позади, но это испытание будет последним для вас. АХАХАХАХА"
    b "А вот и моё любимое испытание, здесь обычно многие превращаются в курочку гриль."
    b "Это не просто лазеры, они разрезают всё на своем пути, температура примерно 2000 градусов"
    "..."
    e "Это похоже на лазеры из глаз супермена."
    v "ахпзахпза, я тоже об этом подумал."
    v "Ну чтож, похоже что вперед мы не пройдем, между лазерами тела не пролезут."
    b "АХПАХАХАХА, забыл сказать, что лазеры медленно смещаются, они меняют угол своего направления."
    e "Херово, очень херово"
    "Вперед нам не пройти, на месте тоже не постоишь."
    e "Надо что-то делать."
    v "Вон смотри сзади можно пройти."
    e "Смотри, слева тоже есть какая-та большая кнопка, может она что-то делает?"
    v "Выглядит странно."
    hide kol with dissolve
    hide zlo with dissolve
    menu:
        "Что делаем?"
        "Хакнуть лазеры":
            if successCount > 5.5:
                "Лазеры отключились"
                e "Неплохо я постарался."
                v "Ай какой же ты молодец."
                jump final_1
            else: 
                "Что то у меня не особо получается..."
                e "Давай лучше вернемся назад"
                v "Кстати я там заметил люк через который можно попробовать пробраться дальше"
                e "Отлично тогда идем"
                jump continue_5
        "Возращаемся обратно":
            "Не стоит рисковать"
            e "Не могу понять как пройти дальше так что возвращаемся назад"
            v "Кстати я там заметил люк через который можно попробовать пробраться дальше"
            e "Отлично тогда идем"
            jump continue_5
        "Пожертвовать Вовой и пройти сквозь лазеры...":
            e "Слушай у меня есть план."
            e "Подойди поближе к лазерам."
            v "Тааак, мне даже интересно."
            e "Ага вот да буквально чтобы ты в паре сантиметров был."
            "Толкнуть Вову и пробежать в момент когда лазеры перекрыты его телом..."
            e "Прости но так надо..."
            v "Кхе...Кхее... Я... Ве..."
            v "Вери... Верил тебе..."
            e "Прости но так нужно."
            $ renpy.notify("Получено достижение - Лучший друг! ")
            jump final_2






label continue_5:
    e "Так, ты говорил есть какой то люк?"
    v "Да, где то тут он был."
    v "Во, смотри"
    scene luk
    with fade
    v "Ща болты снимем и попозли."
    e "Ты уверен что нам сюда?"
    v "А выбора больше и нет"
    scene
    with fade
    "..."
    "..."
    scene lab
    with fade
    show zlo at right
    with fade
    e "Йоу где это мы?"
    b "И так, перед вами испытание, которое будет очень непросто пройти АХАХАХА. "
    e "Опять ты..."
    b "Эта комната как мини лабиринт, в конце которой стоит дверь."
    b "Чтобы ее открыть, вам придется изрядно попотеть, а именно воздействовать все свои навыки программирования"
    b "комната с компьютером должна загореться зеленым, чтобы открылась дверь, и так 2 раза."
    b "Но учтите, что есть и фейковые компьютеры, при активации которых, будем бум… АХАХАХАХА."
    b "Сейчас перед вами откроется карта, постарайтесь запомнить её, иначе будет БУМ.. АХАХАХА."
    e "Бум?"
    e "Что это значит?"
    "Мне это совсем не нравится."
    v "Наверное он хотел сказать, что будет реальный бум."
    v "То есть взрыв!"
    e "Что-то я перехотел это проходить."
    e "Может свалим?"
    v "Второй раз свалить не получится, путь назад теперь закрыт"
    "..."
    e "Какого хрена, как ориентировать в этом лабиринте..."
    g "Сейчас у тебя в голове появится картинка, попробуй запомнить ее"
    scene map
    with fade
    pause 1.0
    g "Пройдешь всего 2 комнаты и у тебя получится отключить вирус!"
    scene
    with fade
    e "Опять голоса..."
    v "Чувак о чем ты?"
    e "Забей братан, побежали"
    scene 
    with fade 
    "..."
    menu:
        "Куда повернуть?"

        "Направо.":
            e "Бежим сюда"
            jump lab_1minusright
        "Налево.":
            e "Быстро сюда."
            jump lab_10plusleft    





label lab_1minusright:
    scene office
    with fade
    e "Хм, это комната с компьютером."
    v "Похоже, здесь установлена защита, которую нужно обойти."
    e "Ну что ж, приступим."
    e "Только не торопись и будь внимателен."
    "..."
    "Внезапно комната озарилась красным светом."
    $ healthCount -= 25
    e "БЕГИМ!"
    "Грохот..."
    v "Ты цел, Костян?"
    e "Да, в этот раз повезло."
    e "Задело только ногу, но в следующий раз может быть хуже."
    e "Надо помнить карту и не ошибаться дальше."
    v "Побежали скорее!"
    menu:
        "Куда повернуть?"

        "Направо.":
            e "Бежим сюда."
            jump lab_2plusright
        "Налево.":
            e "Скорее сюда!"
            jump lab_2minusleft 

label lab_2minusleft:
    scene second
    with fade
    e "Эта комната тоже с компьютером."
    v "И снова защита, которую нужно взломать."
    e "Приступаем."
    e "Но будь осторожен."
    "..."
    "Красный свет заливает комнату."
    "Дверь захлопнулась, и пути к отступлению нет..."
    e "Похоже, это конец нашего пути по лабиринту..."
    $ renpy.notify("Получено достижение - Невероятная память")
    pause
    return

label lab_2plusright:
    scene second
    with fade
    e "Еще одна комната с компьютером."
    v "И снова здесь стоит защита."
    e "Начинаем взлом."
    "..."
    "Зеленый свет наполняет комнату."
    e "Вперед, не останавливаемся!"
    menu:
        "Куда повернуть?"

        "Направо.":
            e "Сюда, быстрее!"
            jump lab_3minusright
        "Налево.":
            e "Давай сюда!"
            jump lab_3plusleft

label lab_3plusleft:
    scene third
    with fade
    e "И снова комната с компьютером."
    v "Не расслабляйся, защита здесь точно есть."
    e "Беремся за дело."
    "..."
    "Зеленый свет вспыхнул."
    e "Уходим отсюда!"
    menu:
        "Что делаем дальше?"
        
        "Сбегаем из здания!":
            "Хватит с нас этого!"
            jump final_4
        "Идем драться с Вирусом!":
            if successCount > 4.5:
                jump final_1
            else:
                jump final_3



label lab_3minusright:
    scene third
    with fade
    e "Еще одна комната с компьютером."
    v "Похоже, защита тут сложнее."
    e "Постараемся справиться."
    e "Не забывай быть осторожным."
    "..."
    "Комната заливается красным светом."
    "Дверь захлопнулась, и выбраться не получится..."
    e "Видимо, на этом наш путь закончился..."
    $ renpy.notify("Получено достижение - Невероятная память")
    pause
    return

label lab_10plusleft:
    scene office
    with fade
    e "Очередная комната с компьютером."
    v "И здесь тоже защита, без взлома не пройти."
    e "Приступаем."
    "..."
    "Зеленый свет зажегся."
    e "Бежим дальше, времени нет!"
    menu:
        "Куда повернуть?"

        "Направо.":
            e "Давай сюда!"
            jump lab_20plusright
        "Налево.":
            e "Бежим налево!"
            jump lab_20minusleft  

label lab_20minusleft:
    scene second
    with fade
    e "Мы снова в комнате с компьютером."
    v "И здесь есть защита, которую нужно сломать."
    e "Давай начнем."
    e "Только аккуратнее."
    "..."
    "Комната заливается красным светом."
    $ healthCount -= 25
    e "БЕГИИИ!"
    "Грохот раздается позади..."
    v "Ты как, живой?"
    e "Да, на этот раз повезло."
    e "Но следующий взрыв может стать для нас последним."
    e "Надо запомнить карту и двигаться дальше без ошибок."
    v "Побежали!"
    menu:
        "Куда повернуть?"

        "Направо.":
            e "Скорее сюда!"
            jump lab_30minusright
        "Налево.":
            e "Бежим налево!"
            jump lab_30plusleft  

label lab_20plusright:
    scene second
    with fade
    e "Еще одна комната с компьютером."
    v "Защита тоже здесь есть."
    e "Приступаем к работе."
    "..."
    "Зеленый свет наполнил комнату."
    e "Бежим дальше, времени мало!"
    menu:
        "Что делаем дальше?"
        
        "Сбегаем из здания!":
            "Хватит с нас этого!"
            jump final_4
        "Идем драться с Вирусом!":
            if successCount > 4.5:
                jump final_1
            else:
                jump final_3

label lab_30plusleft:
    scene third
    with fade
    e "Опять комната с компьютером."
    v "Нужно аккуратно взломать защиту."
    e "Начинаем."
    "..."
    "Зеленый свет загорелся."
    e "Продолжаем движение!"
    menu:
        "Что делаем дальше?"
        
        "Сбегаем из здания!":
            "Хватит с нас этого!"
            jump final_4
        "Идем драться с Вирусом!":
            if successCount > 4.5:
                jump final_1
            else:
                jump final_3

label lab_30minusright:
    scene third
    with fade
    e "Очередная комната с компьютером."
    v "Снова защита. Похоже, что сложная."
    e "Попробуем взломать."
    e "Только будь осторожен."
    "..."
    "Красный свет заливает комнату."
    "Дверь заблокирована, выхода больше нет..."
    e "Похоже, наш путь в лабиринте завершен..."
    $ renpy.notify("Получено достижение - Невероятная память")
    pause
    return






label final_1:
    scene boss
    with fade
    show zlo at right
    with fade
    e "Вирус, это конец. Мы пришли за тобой."
    b "Два жалких человека против меня? Смешно."
    v "Не забывай, что нас двое. Это твоя ошибка."
    "Вирус начинает атаку, но слаженные действия Кости и Вовы позволяют отбить каждую угрозу."
    e "Вводи последний код, я его сдержу!"
    v "Готово! Пора заканчивать."
    "Мощный импульс проходит по системе, и Вирус распадается на части."
    hide zlo
    with dissolve
    e "Мы сделали это. Отличная работа, напарник."
    v "И тебе спасибо. Теперь всё позади."
    $ renpy.notify("Получено достижение - Лучшая концовка!")
    pause 
    return

label final_2:
    scene boss
    with fade
    show zlo at right
    with fade
    e "Вот ты и остался, Вирус. Это конец."
    b "Ты действительно думаешь, что можешь остановить меня один?"
    e "У меня нет другого выбора. Ты причинил слишком много зла."
    b "Попробуй, если хватит смелости."
    "Вирус начинает атаку, но Костя уверенно отбивает каждую попытку."
    e "Это за каждого, кого ты разрушил!"
    "Мощный разряд проходит через систему, и Вирус исчезает в потоке кода."
    hide zlo
    with dissolve
    e "Теперь всё кончено. Я справился."
    $ renpy.notify("Получено достижение - Одинокий волк")
    pause 
    return

label final_3:
    scene boss
    with fade
    e "Мы справимся, только не сдавайся!"
    v "Я пытаюсь, но он слишком силён!"
    b "Вы были глупы, думая, что сможете победить меня."
    "Вирус усиливает свою атаку, и Вова с Костей начинают терять силы."
    v "Костян, я не могу больше держать защиту!"
    e "Нет, мы не можем отступить сейчас!"
    "Но сил уже не хватает, и Вирус наносит решающий удар."
    b "Ваши жалкие попытки закончены. Теперь вы часть моей системы."
    "Экраны гаснут, оставляя лишь пустоту и холодную тишину."
    $ renpy.notify("Получено достижение - Между храбростью и глупостью есть тонкая грань")
    pause 
    return


label final_4:
    v "Наконец-то! Я уже начал думать, что это невозможно."
    e "Видимо, все наши усилия окупились."
    v "Теперь можем вздохнуть с облегчением и покинуть это место."
    e "Давай, выходим отсюда, пока ничего не изменилось."
    "Солнечный свет ослепляет вас, как только вы выходите из лабиринта."
    scene bg ent
    with fade
    e "Смотри, какая красота! Мы свободны."
    v "И кто бы мог подумать, что мы справимся?"
    e "Теперь это кажется сном, но это реальность."
    v "Что ж, пора возвращаться домой и отпраздновать."
    e "Абсолютно согласен."
    $ renpy.notify("Получено достижение - Побег из Шоушенка")
    pause 
    return


  
  
  
  




  

