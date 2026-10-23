# Іван Пендлишак — план загрузки и выжимок

**Снимок каталога:** 22–23.10.2026 (yt-dlp, вкладки «Видео» и «Трансляции» канала). **Статусы сверены:** 23.10.2026 с папками и git ветки.

**Канал:** Ivan Pendlyshak (точное имя канала YouTube). **Коллекция:** [bible/ivan-pendlishak/](./).

## Где идёт работа

- **Ветка:** `ingest/parallel-2026-10-22` — не влита в `main`. Коммиты и push только в эту ветку; в `main` по этому плану ничего не делать.
- **Рабочая папка:** `C:\xampp\htdocs\youtube-parallel` (отдельная копия репозитория на этой ветке). Основная папка `C:\xampp\htdocs\youtube` стоит на `main` и для этого плана не используется.
- **Фраза для продолжения:** «продолжи план Пендлишака» — открыть этот файл в рабочей папке и взять следующие ролики по порядку ниже.

## Как продолжать

1. **Порядок — от новых к старым.** Первым брать самый новый ролик со статусом «скачано без выжимки», затем «нет ссылки», затем «не начато» (2025 год сверху вниз).
2. **Один ролик — одна выжимка по правилам [AGENTS.md](../../AGENTS.md)**, команда «Прими и подготовь ролик»: проверка дублей по Video ID → папка и README → оригинальные субтитры и `transcript.cleaned.md` → SUMMARY.md (больше 40 000 знаков — ещё `sections.yaml` и `sections/`) → теги и «О чём» → строка в [INDEX.md](../../INDEX.md).
3. **Если папка уже есть** («скачано без выжимки») — субтитры заново не качать, сразу готовить выжимку по существующему `transcript.cleaned.md`.
4. **После каждой партии** — в этой таблице сменить статус на «готово», обновить счётчики, коммит и push в `ingest/parallel-2026-10-22`. Сообщение коммита в стиле ветки: «Пендлишак 2026: выжимки трансляций 2026-06-12, 06-05».
**Этапы (по ~30 мин скачивания):**

| Этап | Что | Роликов | Состояние |
|---|---|---:|---|
| 1 | «скачано без выжимки»: 20 роликов 2026 + 20 роликов 2025 (2025-12-31 … 2025-11-21) | 40 | скачан, ждёт подготовки |
| 2 | 2025-11-19 … 2025-05-21 | 86 | не скачан |
| 3 | 2025-05-18 … 2025-01-14 | 86 | не скачан |

5. **Скачивание «не начато»** — командой «Скачай субтитры по плану Пендлишака» (`tools/download_subs.py`, см. раздел «Планы» в [AGENTS.md](../../AGENTS.md)). Других скриптов в репозиторий не класть.

**Статусы:** «готово» — `SUMMARY.md` есть в git; «скачано без выжимки» — папка с `transcript.cleaned.md` есть на диске, выжимки нет; «нет ссылки» — папка есть, но Video ID неизвестен; «не начато» — папки нет.

## Сводка

| Год | Всего | Видео | Трансляции | Готово | Скачано без выжимки | Нет ссылки | Не начато |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 174 | 134 | 39 | 153 | 20 | 1 | 0 |
| 2025 | 192 | 163 | 29 | 0 | 126 | 0 | 66 |
| **Итого** | **366** | **297** | **68** | **153** | **146** | **1** | **66** |

Пояснения к числам:

- **2026: 174 ролика, а не 179 строк исходного списка.** В рабочем списке сессии пять роликов записаны дважды — строкой без ID и строкой с ID, подтверждённым по субтитрам; в плане они по одному разу.
- **«Нет ссылки» — «Слава Богові, а не собі» (2026-08).** Папка в git с расшифровкой и разделами, но без Video ID, точной даты и SUMMARY. Найти ролик на канале по названию или фразе из расшифровки, вписать ID и дату в README, затем сделать выжимку. Все 365 ID из вкладок канала уже сопоставлены другим строкам плана, поэтому в текущих списках канала этого ролика, скорее всего, нет (удалён, скрыт или опубликован не на этом канале) — искать через поиск YouTube по названию.
- **2025:** в очереди все 192 ролика вкладок «Видео» и «Трансляции»; четыре из них короче трёх минут, но опубликованы как обычные видео, поэтому оставлены (тип помечен «короткое»). Shorts канала в план не входят. Ни один ID 2025 года в репозитории ещё не встречается.

## 2026

Всего **174**: готово — 153, скачано без выжимки — 20, нет ссылки — 1. От новых к старым.

| Video ID | Дата | Ролик | Тип | Статус | Папка |
|---|---|---|---|---|---|
| `W3rcVLhGJ4Q` | 2026-10-22 | [Духовні ліки від Господа - Іван Пендлишак](https://www.youtube.com/watch?v=W3rcVLhGJ4Q) | трансляция | готово | [2026-10-22-dukhovni-liky-vid-hospoda](2026-10-22-dukhovni-liky-vid-hospoda/) |
| `MZrxdm5FYaQ` | 2026-10-21 | [Коли сумління не дає спокою - Іван Пендлишак](https://www.youtube.com/watch?v=MZrxdm5FYaQ) | видео | готово | [2026-10-21-koly-sumlinnya-ne-daie-spokoyu](2026-10-21-koly-sumlinnya-ne-daie-spokoyu/) |
| `rn4Nj1QLLT4` | 2026-10-18 | [Проси Господа берегти твої думки - Іван Пендлишак](https://www.youtube.com/watch?v=rn4Nj1QLLT4) | видео | готово | [2026-10-18-prosy-hospoda-berehty-tvoi-dumky](2026-10-18-prosy-hospoda-berehty-tvoi-dumky/) |
| `Y2Sf9KO9-cY` | 2026-10-16 | [Ти не туди пливеш - Іван Пендлишак](https://www.youtube.com/watch?v=Y2Sf9KO9-cY) | видео | готово | [2026-10-16-ty-ne-tudy-plyvesh](2026-10-16-ty-ne-tudy-plyvesh/) |
| `hYTVYvoxGxo` | 2026-10-15 | [Жорстокий серцем потрапить в біду - Іван Пендлишак](https://www.youtube.com/watch?v=hYTVYvoxGxo) | трансляция | готово | [2026-10-15-zhorstokyi-sertsem-potrapyt-v-bidu](2026-10-15-zhorstokyi-sertsem-potrapyt-v-bidu/) |
| `w8xYFKX1vV8` | 2026-10-14 | [Це було не зрозуміло царю Давиду - Іван Пендлишак](https://www.youtube.com/watch?v=w8xYFKX1vV8) | видео | готово | [2026-10-14-tse-bulo-ne-zrozumilo-tsaryu-davydu](2026-10-14-tse-bulo-ne-zrozumilo-tsaryu-davydu/) |
| `CyAaSmHchKA` | 2026-10-11 | [Чи існує звільнення від гріха? - Іван Пендлишак](https://www.youtube.com/watch?v=CyAaSmHchKA) | видео | готово | [2026-10-11-chy-isnuie-zvilnennya-vid-hrikha](2026-10-11-chy-isnuie-zvilnennya-vid-hrikha/) |
| `9QH6oQrhe9U` | 2026-10-09 | [Ми молимось, а Ти не чуєш - Іван Пендлишак](https://www.youtube.com/watch?v=9QH6oQrhe9U) | видео | готово | [2026-10-09-my-molymos-a-ty-ne-chuiesh](2026-10-09-my-molymos-a-ty-ne-chuiesh/) |
| `60nsVx5v8pw` | 2026-10-08 | [Терпіння веде до царювання - Іван Пендлишак](https://www.youtube.com/watch?v=60nsVx5v8pw) | трансляция | готово | [2026-10-08-terpinnya-vede-do-tsaryuvannya](2026-10-08-terpinnya-vede-do-tsaryuvannya/) |
| `K4o8uvAchFg` | 2026-10-07 | [Історія для порівняння - Іван Пендлишак](https://www.youtube.com/watch?v=K4o8uvAchFg) | видео | готово | [2026-10-07-istoriya-dlya-porivnyannya](2026-10-07-istoriya-dlya-porivnyannya/) |
| `LN0BR0JQm2A` | 2026-10-04 | [Мудрий не повторює чужих помилок - Іван Пендлишак](https://www.youtube.com/watch?v=LN0BR0JQm2A) | видео | готово | [2026-10-04-mudryi-ne-povtoryuie-chuzhykh-pomylok](2026-10-04-mudryi-ne-povtoryuie-chuzhykh-pomylok/) |
| `YIL5RHC5Znk` | 2026-10-02 | [Віра зараховується в праведність - Іван Пендлишак \| Спомин смерті Ісуса Христа](https://www.youtube.com/watch?v=YIL5RHC5Znk) | видео | готово | [2026-10-02-vira-zarakhovuietsya-v-pravednist-ivan-pendlyshak-spomyn-smerti-isusa](2026-10-02-vira-zarakhovuietsya-v-pravednist-ivan-pendlyshak-spomyn-smerti-isusa/) |
| `_g699b2fd3k` | 2026-10-01 | [Комплекси не дають бути щасливим - Іван Пендлишак](https://www.youtube.com/watch?v=_g699b2fd3k) | трансляция | готово | [2026-10-01-kompleksy-ne-dayut-buty-shchaslyvym](2026-10-01-kompleksy-ne-dayut-buty-shchaslyvym/) |
| `BfCM-Mjmp88` | 2026-09-30 | [Що заважає нам бути вдячними? - Іван Пендлишак](https://www.youtube.com/watch?v=BfCM-Mjmp88) | видео | готово | [2026-09-30-shcho-zavazhaie-nam-buty-vdyachnymy](2026-09-30-shcho-zavazhaie-nam-buty-vdyachnymy/) |
| `YD0FQB81luc` | 2026-09-27 | [Хто може бути Божим служителем? - Іван Пендлишак](https://www.youtube.com/watch?v=YD0FQB81luc) | видео | готово | [2026-09-27-khto-mozhe-buty-bozhym-sluzhytelem](2026-09-27-khto-mozhe-buty-bozhym-sluzhytelem/) |
| `EnuK5ki4mMc` | 2026-09-25 | [Хто ти, коли ніхто не бачить? - Іван Пендлишак](https://www.youtube.com/watch?v=EnuK5ki4mMc) | видео | готово | [2026-09-25-hto-ti-koli-nihto-ne-bachit-ivan-pendlishak](2026-09-25-hto-ti-koli-nihto-ne-bachit-ivan-pendlishak/) |
| `5KOQHyDKXJ4` | 2026-09-24 | [Життя в повному рабстві - Іван Пендлишак](https://www.youtube.com/watch?v=5KOQHyDKXJ4) | трансляция | готово | [2026-09-24-zhyttya-v-povnomu-rabstvi](2026-09-24-zhyttya-v-povnomu-rabstvi/) |
| `01IopeaAu8c` | 2026-09-23 | [Відповідальність і постійність - Іван Пендлишак](https://www.youtube.com/watch?v=01IopeaAu8c) | видео | готово | [2026-09-23-vidpovidalnist-i-postiinist-ivan-pendlishak](2026-09-23-vidpovidalnist-i-postiinist-ivan-pendlishak/) |
| `dLZ_ZUyJ4r4` | 2026-09-21 | [Небезпека релігійних крайнощів - Іван Пендлишак](https://www.youtube.com/watch?v=dLZ_ZUyJ4r4) | видео | готово | [2026-09-21-nebezpeka-religiinih-krainoshchiv-ivan-pendlishak](2026-09-21-nebezpeka-religiinih-krainoshchiv-ivan-pendlishak/) |
| `AzJASY-1Bd4` | 2026-09-20 | [Зважений на вагах Божої справедливості - Іван Пендлишак](https://www.youtube.com/watch?v=AzJASY-1Bd4) | видео | готово | [2026-09-20-zvazhenii-na-vagah-bozhoi-spravedlivosti-ivan-pendlishak](2026-09-20-zvazhenii-na-vagah-bozhoi-spravedlivosti-ivan-pendlishak/) |
| `fAtRb3n3BdI` | 2026-09-18 | [Чим людина грішить тим і наказується - Іван Пендлишак](https://www.youtube.com/watch?v=fAtRb3n3BdI) | видео | готово | [2026-09-18-chim-lyudina-grishit-tim-i-nakazuietsya-ivan-pendlishak](2026-09-18-chim-lyudina-grishit-tim-i-nakazuietsya-ivan-pendlishak/) |
| `wrdUDp1Yg48` | 2026-09-17 | [Як перевірити справжню святість - Іван Пендлишак](https://www.youtube.com/watch?v=wrdUDp1Yg48) | трансляция | готово | [2026-09-17-yak-pereviryty-spravzhnyu-svyatist](2026-09-17-yak-pereviryty-spravzhnyu-svyatist/) |
| `rlWM0pZfMic` | 2026-09-16 | [Проблема пророка - Іван Пендлишак](https://www.youtube.com/watch?v=rlWM0pZfMic) | видео | готово | [2026-09-16-problema-proroka-ivan-pendlishak](2026-09-16-problema-proroka-ivan-pendlishak/) |
| `fpRQK4hnaHU` | 2026-09-14 | [Закрили вуха і не хочуть чути - Іван Пендлишак](https://www.youtube.com/watch?v=fpRQK4hnaHU) | видео | готово | [2026-09-14-zakrili-vuha-i-ne-hochut-chuti-ivan-pendlishak](2026-09-14-zakrili-vuha-i-ne-hochut-chuti-ivan-pendlishak/) |
| `IDKXqY1KNgs` | 2026-09-13 | [Випробовуйте пророків - Іван Пендлишак](https://www.youtube.com/watch?v=IDKXqY1KNgs) | видео | готово | [2026-09-13-viprobovuite-prorokiv-ivan-pendlishak](2026-09-13-viprobovuite-prorokiv-ivan-pendlishak/) |
| `rf0GAxbV4Sw` | 2026-09-11 | [До чого приводить впертість - Іван Пендлишак](https://www.youtube.com/watch?v=rf0GAxbV4Sw) | видео | готово | [2026-09-11-do-chogo-pryvodyt-vpertist](2026-09-11-do-chogo-pryvodyt-vpertist/) |
| `uyhhFSML9Ds` | 2026-09-10 | [Переможець успадкує все - Іван Пендлишак](https://www.youtube.com/watch?v=uyhhFSML9Ds) | трансляция | готово | [2026-09-10-peremozhets-uspadkuie-vse](2026-09-10-peremozhets-uspadkuie-vse/) |
| `JQxvlXsLv6w` | 2026-09-09 | [Запитати Бога, але не послухати Його - Іван Пендлишак](https://www.youtube.com/watch?v=JQxvlXsLv6w) | видео | готово | [2026-09-09-zapytaty-boga-ale-ne-posluhaty-yogo](2026-09-09-zapytaty-boga-ale-ne-posluhaty-yogo/) |
| `L9qoor72A5w` | 2026-09-07 | [Коли приходить час пожинати - Іван Пендлишак](https://www.youtube.com/watch?v=L9qoor72A5w) | видео | готово | [2026-09-07-koly-prykhodyt-chas-pozhynaty](2026-09-07-koly-prykhodyt-chas-pozhynaty/) |
| `3_l6HGcgm_w` | 2026-09-06 | [Хто розсіяв Той і збере - Іван Пендлишак](https://www.youtube.com/watch?v=3_l6HGcgm_w) | видео | готово | [2026-09-06-hto-rozsiyav-toy-i-zbere](2026-09-06-hto-rozsiyav-toy-i-zbere/) |
| `0_R8wbaNBHs` | 2026-09-04 | [Бог повертає втрачене - Іван Пендлишак](https://www.youtube.com/watch?v=0_R8wbaNBHs) | видео | готово | [2026-09-04-bog-povertaie-vtrachene](2026-09-04-bog-povertaie-vtrachene/) |
| `gKAgRJ_reAg` | 2026-09-03 | [Духовний закон який діє для всіх - Іван Пендлишак](https://www.youtube.com/watch?v=gKAgRJ_reAg) | трансляция | готово | [2026-09-03-dukhovnyi-zakon-yakyi-diie-dlya-vsikh](2026-09-03-dukhovnyi-zakon-yakyi-diie-dlya-vsikh/) |
| `3U1JbZE3YdU` | 2026-09-02 | [Моліться за цю землю - Іван Пендлишак](https://www.youtube.com/watch?v=3U1JbZE3YdU) | видео | готово | [2026-09-02-molitsya-za-tsyu-zemlyu](2026-09-02-molitsya-za-tsyu-zemlyu/) |
| `gj6n52huefA` | 2026-08-31 | [Чому Бог так робить - Іван Пендлишак](https://www.youtube.com/watch?v=gj6n52huefA) | видео | готово | [2026-08-31-chomu-boh-tak-robyt](2026-08-31-chomu-boh-tak-robyt/) |
| `H5h0uGM1PXg` | 2026-08-30 | [Час покаже - Іван Пендлишак](https://www.youtube.com/watch?v=H5h0uGM1PXg) | видео | готово | [2026-08-30-chas-pokazhe](2026-08-30-chas-pokazhe/) |
| `tmSVa5cNCZc` | 2026-08-28 | [Кожен знає свій злий путь - Іван Пендлишак](https://www.youtube.com/watch?v=tmSVa5cNCZc) | видео | готово | [2026-08-28-kozhen-znaie-sviy-zliy-put](2026-08-28-kozhen-znaie-sviy-zliy-put/) |
| `3Dl-WpL2RyI` | 2026-08-27 | [Страх мучить і виснажує - Іван Пендлишак](https://www.youtube.com/watch?v=3Dl-WpL2RyI) | трансляция | готово | [2026-08-27-strakh-muchyt-i-vysnazhuie](2026-08-27-strakh-muchyt-i-vysnazhuie/) |
| `BMwuoWbRa6I` | 2026-08-26 | [Роби те на що ти призначений - Іван Пендлишак](https://www.youtube.com/watch?v=BMwuoWbRa6I) | видео | готово | [2026-08-26-robi-te-na-shcho-ty-pryznachenyy](2026-08-26-robi-te-na-shcho-ty-pryznachenyy/) |
| `OT4e-r61czE` | 2026-08-24 | [Вплив порадників - Іван Пендлишак](https://www.youtube.com/watch?v=OT4e-r61czE) | видео | готово | [2026-08-24-vplyv-poradnykiv](2026-08-24-vplyv-poradnykiv/) |
| `cvwWi6EcXFs` | 2026-08-23 | [Служіння докору і виявлення гріхів - Іван Пендлишак](https://www.youtube.com/watch?v=cvwWi6EcXFs) | видео | готово | [2026-08-23-sluzhinnya-dokoru-i-vyyavlennya-grihiv](2026-08-23-sluzhinnya-dokoru-i-vyyavlennya-grihiv/) |
| `j2-AmM-5za0` | 2026-08-21 | [Звернення до пасторів - Іван Пендлишак](https://www.youtube.com/watch?v=j2-AmM-5za0) | видео | готово | [2026-08-21-zvernennya-do-pastoriv](2026-08-21-zvernennya-do-pastoriv/) |
| `jXQC8wsHJXA` | 2026-08-20 | [Не здавайся посеред дороги - Іван Пендлишак](https://www.youtube.com/watch?v=jXQC8wsHJXA) | трансляция | готово | [2026-08-20-ne-zdavaisya-posered-dorohy](2026-08-20-ne-zdavaisya-posered-dorohy/) |
| `TEPlPyvhnBw` | 2026-08-19 | [Поступайте по правді та справедливості - Іван Пендлишак](https://www.youtube.com/watch?v=TEPlPyvhnBw) | видео | готово | [2026-08-19-postupaite-po-pravdi-ta-spravedlyvosti](2026-08-19-postupaite-po-pravdi-ta-spravedlyvosti/) |
| `yU8Y0w5gkPI` | 2026-08-17 | [Бог може це зробити - Іван Пендлишак](https://www.youtube.com/watch?v=yU8Y0w5gkPI) | видео | готово | [2026-08-17-boh-mozhe-tse-zrobyty](2026-08-17-boh-mozhe-tse-zrobyty/) |
| `a675DU3bb7Y` | 2026-08-16 | [Я відвідаю вас - Іван Пендлишак](https://www.youtube.com/watch?v=a675DU3bb7Y) | видео | готово | [2026-08-16-ya-vidvidayu-vas](2026-08-16-ya-vidvidayu-vas/) |
| `JuHfZcU0oA8` | 2026-08-14 | [Правда відводить від гріха - Іван Пендлишак](https://www.youtube.com/watch?v=JuHfZcU0oA8) | видео | готово | [2026-08-14-pravda-vidvodyt-vid-hrikha](2026-08-14-pravda-vidvodyt-vid-hrikha/) |
| `S3pPG327CdI` | 2026-08-13 | [Як Господь утішає нас у важкі часи - Іван Пендлишак](https://www.youtube.com/watch?v=S3pPG327CdI) | трансляция | готово | [2026-08-13-yak-hospod-utishaie-nas-u-vazhki-chasy](2026-08-13-yak-hospod-utishaie-nas-u-vazhki-chasy/) |
| `AWZrsWkT1GI` | 2026-08-12 | [Лукаве серце людини - Іван Пендлишак](https://www.youtube.com/watch?v=AWZrsWkT1GI) | видео | готово | [2026-08-12-lukave-sertse-lyudyny](2026-08-12-lukave-sertse-lyudyny/) |
| `CpQpzyNyAc0` | 2026-08-10 | [Вони мене не чують - Іван Пендлишак](https://www.youtube.com/watch?v=CpQpzyNyAc0) | видео | готово | [2026-08-10-vony-mene-ne-chuyut](2026-08-10-vony-mene-ne-chuyut/) |
| `JSywDlDXN_c` | 2026-08-09 | [Чому Господь говорить притчами - Іван Пендлишак](https://www.youtube.com/watch?v=JSywDlDXN_c) | видео | готово | [2026-08-09-chomu-hospod-hovoryt-prytchamy](2026-08-09-chomu-hospod-hovoryt-prytchamy/) |
| `zHvyEHOIk6g` | 2026-08-07 | [Просто визнай свою вину - Іван Пендлишак](https://www.youtube.com/watch?v=zHvyEHOIk6g) | видео | готово | [2026-08-07-prosto-vyznai-svoyu-vynu](2026-08-07-prosto-vyznai-svoyu-vynu/) |
| `oEeHLoq_BDE` | 2026-08-06 | [Ворог краде сьогодення, нагадуючи про минуле і лякаючи майбутнім - Іван Пендлишак](https://www.youtube.com/watch?v=oEeHLoq_BDE) | трансляция | готово | [2026-08-06-voroh-krade-sohodennya-nahaduyuchy-pro-mynule-i-lyakayuchy-maibutnim](2026-08-06-voroh-krade-sohodennya-nahaduyuchy-pro-mynule-i-lyakayuchy-maibutnim/) |
| `xG2XcQGYs30` | 2026-08-05 | [Звичаї, які противні Богу - Іван Пендлишак](https://www.youtube.com/watch?v=xG2XcQGYs30) | видео | готово | [2026-08-05-zvychai-yaki-protyvni-bohu](2026-08-05-zvychai-yaki-protyvni-bohu/) |
| `wjizRiwWDrw` | 2026-08-03 | [Слово до мудрих сильних багатих успішних - Іван Пендлишак](https://www.youtube.com/watch?v=wjizRiwWDrw) | видео | готово | [2026-08-03-slovo-do-mudrykh-sylnykh-bahatykh-uspishnykh](2026-08-03-slovo-do-mudrykh-sylnykh-bahatykh-uspishnykh/) |
| `bPKSKQbxwXI` | 2026-08-02 | [Треба вставати і йти - Іван Пендлишак](https://www.youtube.com/watch?v=bPKSKQbxwXI) | видео | готово | [2026-08-02-treba-vstavaty-i-ity](2026-08-02-treba-vstavaty-i-ity/) |
| — | 2026-08 | 2026-08-slava-bogovi-a-ne-sobi | — | **нет ссылки** | [2026-08-slava-bogovi-a-ne-sobi](2026-08-slava-bogovi-a-ne-sobi/) |
| `rd3b7gYJXk4` | 2026-07-31 | [Якщо перестануть робити гріх - Іван Пендлишак](https://www.youtube.com/watch?v=rd3b7gYJXk4) | видео | готово | [2026-07-31-yakshcho-perestanut-robyty-hrikh](2026-07-31-yakshcho-perestanut-robyty-hrikh/) |
| `Rb-_m_bMX7Q` | 2026-07-30 | [Здоровий глузд - Іван Пендлишак](https://www.youtube.com/watch?v=Rb-_m_bMX7Q) | трансляция | готово | [2026-07-30-zdorovyi-hluzd](2026-07-30-zdorovyi-hluzd/) |
| `MRIf67er9_s` | 2026-07-29 | [Знайдіть хоч одного праведника - Іван Пендлишак](https://www.youtube.com/watch?v=MRIf67er9_s) | видео | готово | [2026-07-29-znaidit-khoch-odnoho-pravednyka](2026-07-29-znaidit-khoch-odnoho-pravednyka/) |
| `wXA8NfguR-8` | 2026-07-27 | [Якщо хочеш - покайся - Іван Пендлишак](https://www.youtube.com/watch?v=wXA8NfguR-8) | видео | готово | [2026-07-27-yakshcho-khochesh-pokaisya](2026-07-27-yakshcho-khochesh-pokaisya/) |
| `Gv_U4dGEYRw` | 2026-07-26 | [Як правило така не повертається - Іван Пендлишак](https://www.youtube.com/watch?v=Gv_U4dGEYRw) | видео | готово | [2026-07-26-yak-pravylo-taka-ne-povertaietsya](2026-07-26-yak-pravylo-taka-ne-povertaietsya/) |
| `gzo_9dWHy6Q` | 2026-07-24 | [Два зла зробили - Іван Пендлишак](https://www.youtube.com/watch?v=gzo_9dWHy6Q) | видео | готово | [2026-07-24-dva-zla-zrobyly](2026-07-24-dva-zla-zrobyly/) |
| `hqV9OgPC_7c` | 2026-07-24 | [Час виконати обіцянку - Іван Пендлишак](https://www.youtube.com/watch?v=hqV9OgPC_7c) | трансляция | готово | [2026-07-24-chas-vykonaty-obitsyanku](2026-07-24-chas-vykonaty-obitsyanku/) |
| `-NBcUQ_rvss` | 2026-07-22 | [Бог дасть що говорити - Іван Пендлишак](https://www.youtube.com/watch?v=-NBcUQ_rvss) | видео | готово | [2026-07-22-boh-dast-shcho-hovoryty](2026-07-22-boh-dast-shcho-hovoryty/) |
| `wz0NmvMMsmg` | 2026-07-20 | [Вони всі в одному списку - Іван Пендлишак](https://www.youtube.com/watch?v=wz0NmvMMsmg) | видео | готово | [2026-07-20-vony-vsi-v-odnomu-spysku](2026-07-20-vony-vsi-v-odnomu-spysku/) |
| `npHexby0yzk` | 2026-07-19 | [Мене знайшли ті, що не шукали - Іван Пендлишак](https://www.youtube.com/watch?v=npHexby0yzk) | видео | готово | [2026-07-19-mene-znaishly-ti-shcho-ne-shukaly](2026-07-19-mene-znaishly-ti-shcho-ne-shukaly/) |
| `Dx_KUkwINsY` | 2026-07-17 | [Ніхто не зможе кинути камінь - Іван Пендлишак](https://www.youtube.com/watch?v=Dx_KUkwINsY) | видео | готово | [2026-07-17-nikhto-ne-zmozhe-kynuty-kamin](2026-07-17-nikhto-ne-zmozhe-kynuty-kamin/) |
| `DvlCdxiYTYw` | 2026-07-17 | [Чи витримає твоя віра час випробувань? - Іван Пендлишак](https://www.youtube.com/watch?v=DvlCdxiYTYw) | трансляция | готово | [2026-07-17-chy-vytrymaie-tvoya-vira-chas-vyprobuvan](2026-07-17-chy-vytrymaie-tvoya-vira-chas-vyprobuvan/) |
| `yr5R2TiGIJo` | 2026-07-15 | [Поставлені попередити про небезпеку - Іван Пендлишак](https://www.youtube.com/watch?v=yr5R2TiGIJo) | видео | готово | [2026-07-15-postavleni-poperedyty-pro-nebezpeku](2026-07-15-postavleni-poperedyty-pro-nebezpeku/) |
| `ZxYw8CsbRxw` | 2026-07-13 | [Бог може відновити навіть те, що здається втраченим - Іван Пендлишак](https://www.youtube.com/watch?v=ZxYw8CsbRxw) | видео | готово | [2026-07-13-boh-mozhe-vidnovyty-navit-te-shcho-zdaietsya-vtrachenym](2026-07-13-boh-mozhe-vidnovyty-navit-te-shcho-zdaietsya-vtrachenym/) |
| `xeAs1Og1jdk` | 2026-07-12 | [Чому Бог каже: «Устань і світи» - Іван Пендлишак](https://www.youtube.com/watch?v=xeAs1Og1jdk) | видео | готово | [2026-07-12-chomu-boh-kazhe-ustan-i-svity](2026-07-12-chomu-boh-kazhe-ustan-i-svity/) |
| `uvliKKks28A` | 2026-07-10 | [Є ще одна причина, чому Бог не чує - Іван Пендлишак](https://www.youtube.com/watch?v=uvliKKks28A) | видео | готово | [2026-07-10-ie-shche-odna-prychyna-chomu-boh-ne-chuie](2026-07-10-ie-shche-odna-prychyna-chomu-boh-ne-chuie/) |
| `uFA-ARDc1-E` | 2026-07-10 | [Ознаки духовного падіння, які не можна ігнорувати - Іван Пендлишак](https://www.youtube.com/watch?v=uFA-ARDc1-E) | трансляция | готово | [2026-07-10-oznaky-dukhovnoho-padinnya-yaki-ne-mozhna-ihnoruvaty](2026-07-10-oznaky-dukhovnoho-padinnya-yaki-ne-mozhna-ihnoruvaty/) |
| `9ADtizGkxKg` | 2026-07-08 | [Бог шукає вірних, а не досконалих - Іван Пендлишак](https://www.youtube.com/watch?v=9ADtizGkxKg) | видео | готово | [2026-07-08-boh-shukaie-virnykh-a-ne-doskonalykh](2026-07-08-boh-shukaie-virnykh-a-ne-doskonalykh/) |
| `KS-zV2SWM2c` | 2026-07-06 | [Бог повертає втрачене - Іван Пендлишак](https://www.youtube.com/watch?v=KS-zV2SWM2c) | видео | готово | [2026-07-06-boh-povertaie-vtrachene](2026-07-06-boh-povertaie-vtrachene/) |
| `ORBWXun_aJc` | 2026-07-05 | [Ще один шанс - Іван Пендлишак](https://www.youtube.com/watch?v=ORBWXun_aJc) | видео | готово | [2026-07-05-shche-odyn-shans](2026-07-05-shche-odyn-shans/) |
| `7er7uKNM2Vg` | 2026-07-03 | [З Ним не рахувались - Іван Пендлишак](https://www.youtube.com/watch?v=7er7uKNM2Vg) | видео | готово | [2026-07-03-z-nym-ne-rakhuvalys](2026-07-03-z-nym-ne-rakhuvalys/) |
| `xscBcPXwA2o` | 2026-07-03 | [Відступлення починається не там, де ти думаєш - Іван Пендлишак](https://www.youtube.com/watch?v=xscBcPXwA2o) | трансляция | готово | [2026-07-03-vidstuplennya-pochynaietsya-ne-tam-de-ty-dumaiesh](2026-07-03-vidstuplennya-pochynaietsya-ne-tam-de-ty-dumaiesh/) |
| `CKhY5Qez0tg` | 2026-07-01 | [Залиш старе життя позаду - Іван Пендлишак](https://www.youtube.com/watch?v=CKhY5Qez0tg) | видео | готово | [2026-07-01-zalysh-stare-zhyttya-pozadu](2026-07-01-zalysh-stare-zhyttya-pozadu/) |
| `Aof_HLdJTxQ` | 2026-06-29 | [Бог не забув про тебе - Іван Пендлишак](https://www.youtube.com/watch?v=Aof_HLdJTxQ) | видео | готово | [2026-06-29-boh-ne-zabuv-pro-tebe](2026-06-29-boh-ne-zabuv-pro-tebe/) |
| `WBBnqWaM6BY` | 2026-06-28 | [З твоєї праці є толк - Іван Пендлишак](https://www.youtube.com/watch?v=WBBnqWaM6BY) | видео | готово | [2026-06-28-z-tvoiei-pratsi-ie-tolk](2026-06-28-z-tvoiei-pratsi-ie-tolk/) |
| `nP7cOA7vo0k` | 2026-06-26 | [Ніхто не скаже: Я знав про це - Іван Пендлишак](https://www.youtube.com/watch?v=nP7cOA7vo0k) | видео | готово | [2026-06-26-nikhto-ne-skazhe-ya-znav-pro-tse](2026-06-26-nikhto-ne-skazhe-ya-znav-pro-tse/) |
| `H9-qk7cr7oc` | 2026-06-26 | [Секрет духовної зрілості - Іван Пендлишак](https://www.youtube.com/watch?v=H9-qk7cr7oc) | трансляция | готово | [2026-06-26-sekret-dukhovnoi-zrilosti](2026-06-26-sekret-dukhovnoi-zrilosti/) |
| `Dw8SKecBlxY` | 2026-06-24 | [Як дерево чи метал може бути богом - Іван Пендлишак](https://www.youtube.com/watch?v=Dw8SKecBlxY) | видео | готово | [2026-06-24-yak-derevo-chy-metal-mozhe-buty-bohom](2026-06-24-yak-derevo-chy-metal-mozhe-buty-bohom/) |
| `DeHD_-MxOj8` | 2026-06-23 | [Не бійся - Господь з тобою - Іван Пендлишак](https://www.youtube.com/watch?v=DeHD_-MxOj8) | видео | готово | [2026-06-23-ne-biisya-hospod-z-toboyu](2026-06-23-ne-biisya-hospod-z-toboyu/) |
| `q88JzxWZLxg` | 2026-06-19 | [Не хочуть бачити і чути - Іван Пендлишак](https://www.youtube.com/watch?v=q88JzxWZLxg) | видео | готово | [2026-06-19-ne-khochut-bachyty-i-chuty](2026-06-19-ne-khochut-bachyty-i-chuty/) |
| `ebJiX3Sg0ok` | 2026-06-18 | [Як зберігати спокій, коли навколо неспокій - Іван Пендлишак](https://www.youtube.com/watch?v=ebJiX3Sg0ok) | трансляция | готово | [2026-06-18-yak-zberihaty-spokii-koly-navkolo-nespokii](2026-06-18-yak-zberihaty-spokii-koly-navkolo-nespokii/) |
| `c3DYWO6MY88` | 2026-06-17 | [Не надійтесь на людину - Іван Пендлишак](https://www.youtube.com/watch?v=c3DYWO6MY88) | видео | готово | [2026-06-17-ne-nadiites-na-lyudynu](2026-06-17-ne-nadiites-na-lyudynu/) |
| `GgtkNXMYtXk` | 2026-06-14 | [Він тростини надламаної не переломить - Іван Пендлишак](https://www.youtube.com/watch?v=GgtkNXMYtXk) | видео | готово | [2026-06-14-vin-trostyny-nadlamanoi-ne-perelomyt](2026-06-14-vin-trostyny-nadlamanoi-ne-perelomyt/) |
| `E4U7mStI7g8` | 2026-06-12 | [Тих, що надіються на Господа, Бог підніме - Іван Пендлишак](https://www.youtube.com/watch?v=E4U7mStI7g8) | видео | готово | [2026-06-12-tykh-shcho-nadiyutsya-na-hospoda-boh-pidnime](2026-06-12-tykh-shcho-nadiyutsya-na-hospoda-boh-pidnime/) |
| `90lq5x3Dcys` | 2026-06-12 | [Як Бог потішає людину? - Іван Пендлишак](https://www.youtube.com/watch?v=90lq5x3Dcys) | трансляция | готово | [2026-06-12-yak-boh-potishaie-lyudynu](2026-06-12-yak-boh-potishaie-lyudynu/) |
| `nOsFST_n7T4` | 2026-06-10 | [Приготуйтеся до приходу Христа - Іван Пендлишак](https://www.youtube.com/watch?v=nOsFST_n7T4) | видео | готово | [2026-06-10-pryhotuitesya-do-prykhodu-khrysta](2026-06-10-pryhotuitesya-do-prykhodu-khrysta/) |
| `gO1hTLeunH4` | 2026-06-07 | [Не хвалися речами - хвалися Господом - Іван Пендлишак](https://www.youtube.com/watch?v=gO1hTLeunH4) | видео | готово | [2026-06-07-ne-khvalysya-rechamy-khvalysya-hospodom](2026-06-07-ne-khvalysya-rechamy-khvalysya-hospodom/) |
| `jIXKNUy8RRg` | 2026-06-05 | [Хто не боїться Божого суда - Іван Пендлишак](https://www.youtube.com/watch?v=jIXKNUy8RRg) | видео | готово | [2026-06-05-khto-ne-boitsya-bozhoho-suda](2026-06-05-khto-ne-boitsya-bozhoho-suda/) |
| `HbwYMCjOCOA` | 2026-06-05 | [Що люди шукають у Божому домі? - Іван Пендлишак](https://www.youtube.com/watch?v=HbwYMCjOCOA) | трансляция | готово | [2026-06-05-shcho-lyudy-shukayut-u-bozhomu-domi](2026-06-05-shcho-lyudy-shukayut-u-bozhomu-domi/) |
| `yEYw2Pz_PBo` | 2026-06-03 | [Сьогодні посієш - завтра пожнеш - Іван Пендлишак](https://www.youtube.com/watch?v=yEYw2Pz_PBo) | видео | готово | [2026-06-03-sohodni-posiiesh-zavtra-pozhnesh](2026-06-03-sohodni-posiiesh-zavtra-pozhnesh/) |
| `iCzW1YZwPBI` | 2026-06-02 | [Гординя засліплює очі. Нетверезі духовно - Іван Пендлишак](https://www.youtube.com/watch?v=iCzW1YZwPBI) | видео | готово | [2026-06-02-hordynya-zasliplyuie-ochi-netverezi-dukhovno](2026-06-02-hordynya-zasliplyuie-ochi-netverezi-dukhovno/) |
| `jm4Jwm8kp68` | 2026-05-31 | [Служіння Святого Духа - Іван Пендлишак](https://www.youtube.com/watch?v=jm4Jwm8kp68) | видео | готово | [2026-05-31-sluzhinnya-svyatoho-dukha](2026-05-31-sluzhinnya-svyatoho-dukha/) |
| `0ZlkQM1K-Yk` | 2026-05-29 | [Наскільки я знаю Духа Святого - Іван Пендлишак](https://www.youtube.com/watch?v=0ZlkQM1K-Yk) | видео | готово | [2026-05-29-naskilky-ya-znayu-dukha-svyatoho](2026-05-29-naskilky-ya-znayu-dukha-svyatoho/) |
| `i4iFthZczT8` | 2026-05-28 | [Господь оберне твої сльози на радість - Іван Пендлишак](https://www.youtube.com/watch?v=i4iFthZczT8) | трансляция | **скачано без выжимки** | [2026-05-28-hospod-oberne-tvoi-slozy-na-radist](2026-05-28-hospod-oberne-tvoi-slozy-na-radist/) |
| `LT-kVUAUs70` | 2026-05-27 | [Правило на правило, заповідь на заповідь - Іван Пендлишак](https://www.youtube.com/watch?v=LT-kVUAUs70) | видео | готово | [2026-05-27-pravylo-na-pravylo-zapovid-na-zapovid](2026-05-27-pravylo-na-pravylo-zapovid-na-zapovid/) |
| `_kgHNjVC4x4` | 2026-05-26 | [На що надіятись у війні - Іван Пендлишак](https://www.youtube.com/watch?v=_kgHNjVC4x4) | видео | готово | [2026-05-26-na-shcho-nadiyatys-u-viini](2026-05-26-na-shcho-nadiyatys-u-viini/) |
| `HoZ-dHnrMJw` | 2026-05-24 | [Скинутий у пекло - Іван Пендлишак](https://www.youtube.com/watch?v=HoZ-dHnrMJw) | видео | готово | [2026-05-24-skynutyi-u-peklo](2026-05-24-skynutyi-u-peklo/) |
| `6_rLDkbzfvc` | 2026-05-22 | [Це буде буквально? - Іван Пендлишак](https://www.youtube.com/watch?v=6_rLDkbzfvc) | видео | готово | [2026-05-22-tse-bude-bukvalno](2026-05-22-tse-bude-bukvalno/) |
| `xP9VGp_h1wg` | 2026-05-21 | [Бог дає шанс: покайся сьогодні - Іван Пендлишак](https://www.youtube.com/watch?v=xP9VGp_h1wg) | трансляция | **скачано без выжимки** | [2026-05-21-boh-daie-shans-pokaisya-sohodni](2026-05-21-boh-daie-shans-pokaisya-sohodni/) |
| `Zz4axwBuifg` | 2026-05-20 | [Спочине на ньому Дух Господній - Іван Пендлишак](https://www.youtube.com/watch?v=Zz4axwBuifg) | видео | готово | [2026-05-20-spochyne-na-nomu-dukh-hospodnii](2026-05-20-spochyne-na-nomu-dukh-hospodnii/) |
| `szbL3WtLpE0` | 2026-05-17 | [Він прийде - Іван Пендлишак](https://www.youtube.com/watch?v=szbL3WtLpE0) | видео | готово | [2026-05-17-vin-pryide](2026-05-17-vin-pryide/) |
| `upWJgdcLKv4` | 2026-05-15 | [Бог допустив покарання - Іван Пендлишак](https://www.youtube.com/watch?v=upWJgdcLKv4) | видео | готово | [2026-05-15-boh-dopustyv-pokarannya](2026-05-15-boh-dopustyv-pokarannya/) |
| `FcW3GbDhjTI` | 2026-05-14 | [Народ, що ходить у пітьмі, світло побачить - Іван Пендлишак](https://www.youtube.com/watch?v=FcW3GbDhjTI) | видео | готово | [2026-05-14-narod-shcho-khodyt-u-pitmi-svitlo-pobachyt](2026-05-14-narod-shcho-khodyt-u-pitmi-svitlo-pobachyt/) |
| `xJfme6nKdXU` | 2026-05-13 | [На кого орієнтуватись? - Іван Пендлишак](https://www.youtube.com/watch?v=xJfme6nKdXU) | видео | готово | [2026-05-13-na-koho-oriientuvatys](2026-05-13-na-koho-oriientuvatys/) |
| `aXbB6Ue1I5c` | 2026-05-10 | [Камінь спотикання - Іван Пендлишак](https://www.youtube.com/watch?v=aXbB6Ue1I5c) | видео | готово | [2026-05-10-kamin-spotykannya](2026-05-10-kamin-spotykannya/) |
| `iMYJNfgpork` | 2026-05-08 | [Возревнував я Господи - Іван Пендлишак](https://www.youtube.com/watch?v=iMYJNfgpork) | видео | готово | [2026-05-08-vozrevnuvav-ya-hospody](2026-05-08-vozrevnuvav-ya-hospody/) |
| `Vb6v1EaKGR4` | 2026-05-07 | [Не бійся того, чого всі бояться - Іван Пендлишак](https://www.youtube.com/watch?v=Vb6v1EaKGR4) | видео | готово | [2026-05-07-ne-biisya-toho-choho-vsi-boyatsya](2026-05-07-ne-biisya-toho-choho-vsi-boyatsya/) |
| `0lnT8KfKaq4` | 2026-05-01 | [Поражу пастиря і розсіються вівці - Іван Пендлишак](https://www.youtube.com/watch?v=0lnT8KfKaq4) | видео | готово | [2026-05-01-porazhu-pastyrya-i-rozsiyutsya-vivtsi](2026-05-01-porazhu-pastyrya-i-rozsiyutsya-vivtsi/) |
| `YYbCJbYtKIM` | 2026-04-29 | [Знамення від Господа - Іван Пендлишак](https://www.youtube.com/watch?v=YYbCJbYtKIM) | видео | готово | [2026-04-29-znamennya-vid-hospoda](2026-04-29-znamennya-vid-hospoda/) |
| `w6HOnnqCHrM` | 2026-04-26 | [Праця для Господа - Іван Пендлишак](https://www.youtube.com/watch?v=w6HOnnqCHrM) | видео | готово | [2026-04-26-pratsya-dlya-hospoda](2026-04-26-pratsya-dlya-hospoda/) |
| `_6dQPAbkcWA` | 2026-04-24 | [Бійся Бога, виконуй Його заповіді - Іван Пендлишак](https://www.youtube.com/watch?v=_6dQPAbkcWA) | видео | готово | [2026-04-24-biisya-boha-vykonui-ioho-zapovidi](2026-04-24-biisya-boha-vykonui-ioho-zapovidi/) |
| `PEnlilhxBUI` | 2026-04-22 | [Чи буває те, чого Бог не повелів бути - Іван Пендлишак](https://www.youtube.com/watch?v=PEnlilhxBUI) | видео | готово | [2026-04-22-chy-buvaie-te-choho-boh-ne-poveliv-buty](2026-04-22-chy-buvaie-te-choho-boh-ne-poveliv-buty/) |
| `8mtleZtnVc4` | 2026-04-17 | [Духовні досягнення вдома - Іван Пендлишак](https://www.youtube.com/watch?v=8mtleZtnVc4) | видео | готово | [2026-04-17-dukhovni-dosyahnennya-vdoma](2026-04-17-dukhovni-dosyahnennya-vdoma/) |
| `rMFLzePev4U` | 2026-04-16 | [Принципи щасливого життя - Іван Пендлишак](https://www.youtube.com/watch?v=rMFLzePev4U) | трансляция | **скачано без выжимки** | [2026-04-16-pryntsypy-shchaslyvoho-zhyttya](2026-04-16-pryntsypy-shchaslyvoho-zhyttya/) |
| `Pa3VqNXuyq8` | 2026-04-15 | [Нерукотворний храм - Іван Пендлишак](https://www.youtube.com/watch?v=Pa3VqNXuyq8) | видео | готово | [2026-04-15-nerukotvornyi-khram](2026-04-15-nerukotvornyi-khram/) |
| `0Q73EvspLc8` | 2026-04-12 | [Не поспішай засуджувати - навчися розуміти - Іван Пендлишак](https://www.youtube.com/watch?v=0Q73EvspLc8) | видео | готово | [2026-04-12-ne-pospishai-zasudzhuvaty-navchysya-rozumity](2026-04-12-ne-pospishai-zasudzhuvaty-navchysya-rozumity/) |
| `e35amjRmmM4` | 2026-04-10 | [Догодити Богові - Іван Пендлишак](https://www.youtube.com/watch?v=e35amjRmmM4) | трансляция | **скачано без выжимки** | [2026-04-10-dohodyty-bohovi](2026-04-10-dohodyty-bohovi/) |
| `XIBJRqOys0A` | 2026-04-06 | [Яке значення воскресіння Христа для нас - Іван Пендлишак](https://www.youtube.com/watch?v=XIBJRqOys0A) | видео | готово | [2026-04-06-yake-znachennya-voskresinnya-khrysta-dlya-nas](2026-04-06-yake-znachennya-voskresinnya-khrysta-dlya-nas/) |
| `oj3ExlI5ciA` | 2026-04-05 | [Буде воскресіння із мертвих - Іван Пендлишак](https://www.youtube.com/watch?v=oj3ExlI5ciA) | видео | готово | [2026-04-05-bude-voskresinnya-iz-mertvykh](2026-04-05-bude-voskresinnya-iz-mertvykh/) |
| `u1Sj5DAReG8` | 2026-04-03 | [У світі є багато добрих людей - Іван Пендлишак](https://www.youtube.com/watch?v=u1Sj5DAReG8) | видео | готово | [2026-04-03-u-sviti-ie-bahato-dobrykh-lyudei](2026-04-03-u-sviti-ie-bahato-dobrykh-lyudei/) |
| `Mdvvda0-uUk` | 2026-04-02 | [Три критерії Євангельської віри - Іван Пендлишак](https://www.youtube.com/watch?v=Mdvvda0-uUk) | трансляция | **скачано без выжимки** | [2026-04-02-try-kryterii-ievanhelskoi-viry](2026-04-02-try-kryterii-ievanhelskoi-viry/) |
| `jOcR65UVxS0` | 2026-04-01 | [Горе тим, які ... - Іван Пендлишак](https://www.youtube.com/watch?v=jOcR65UVxS0) | видео | готово | [2026-04-01-hore-tym-yaki](2026-04-01-hore-tym-yaki/) |
| `6teUGRQJZM4` | 2026-03-29 | [Бог все зробив для Свого виноградника - Іван Пендлишак](https://www.youtube.com/watch?v=6teUGRQJZM4) | видео | готово | [2026-03-29-boh-vse-zrobyv-dlya-svoho-vynohradnyka](2026-03-29-boh-vse-zrobyv-dlya-svoho-vynohradnyka/) |
| `ujJpZkxdNd8` | 2026-03-27 | [Чим допомогти людській душі - Іван Пендлишак](https://www.youtube.com/watch?v=ujJpZkxdNd8) | видео | готово | [2026-03-27-chym-dopomohty-lyudskii-dushi](2026-03-27-chym-dopomohty-lyudskii-dushi/) |
| `swGB6z8LZM4` | 2026-03-27 | [Хто любить Бога, дотримується Його слів - Іван Пендлишак](https://www.youtube.com/watch?v=swGB6z8LZM4) | трансляция | **скачано без выжимки** | [2026-03-27-khto-lyubyt-boha-dotrymuietsya-ioho-sliv](2026-03-27-khto-lyubyt-boha-dotrymuietsya-ioho-sliv/) |
| `ejLip8e_hXA` | 2026-03-25 | [В чоловіка і жінки різні ролі - Іван Пендлишак](https://www.youtube.com/watch?v=ejLip8e_hXA) | видео | готово | [2026-03-25-v-cholovika-i-zhinky-rizni-roli](2026-03-25-v-cholovika-i-zhinky-rizni-roli/) |
| `DR9V5n8z4AU` | 2026-03-22 | [Твоє терпіння не марне — буде нагорода - Іван Пендлишак](https://www.youtube.com/watch?v=DR9V5n8z4AU) | видео | готово | [2026-03-22-tvoie-terpinnya-ne-marne-bude-nahoroda](2026-03-22-tvoie-terpinnya-ne-marne-bude-nahoroda/) |
| `PLSys3Ft7j8` | 2026-03-19 | [Якщо Дух Господній живе в нас - Іван Пендлишак](https://www.youtube.com/watch?v=PLSys3Ft7j8) | трансляция | **скачано без выжимки** | [2026-03-19-yakshcho-dukh-hospodnii-zhyve-v-nas](2026-03-19-yakshcho-dukh-hospodnii-zhyve-v-nas/) |
| `xFmoiu4rrck` | 2026-03-18 | [Вони того не соромляться - Іван Пендлишак](https://www.youtube.com/watch?v=xFmoiu4rrck) | видео | готово | [2026-03-18-vony-toho-ne-soromlyatsya](2026-03-18-vony-toho-ne-soromlyatsya/) |
| `FVGr7yC8XfA` | 2026-03-15 | [Прости і прийми волю Божу - Іван Пендлишак](https://www.youtube.com/watch?v=FVGr7yC8XfA) | видео | готово | [2026-03-15-prosty-i-pryimy-volyu-bozhu](2026-03-15-prosty-i-pryimy-volyu-bozhu/) |
| `V3oKVrbBF7A` | 2026-03-13 | [Віра робить людину всемогутньою - Іван Пендлишак](https://www.youtube.com/watch?v=V3oKVrbBF7A) | видео | готово | [2026-03-13-vira-robyt-lyudynu-vsemohutnoyu](2026-03-13-vira-robyt-lyudynu-vsemohutnoyu/) |
| `OlL4tBmMKvY` | 2026-03-12 | [Як можеш судити іншого, коли сам робиш те саме - Іван Пендлишак](https://www.youtube.com/watch?v=OlL4tBmMKvY) | трансляция | **скачано без выжимки** | [2026-03-12-yak-mozhesh-sudyty-inshoho-koly-sam-robysh-te-same](2026-03-12-yak-mozhesh-sudyty-inshoho-koly-sam-robysh-te-same/) |
| `q27nozKJ0Kg` | 2026-03-11 | [Прислухайся до старших - Іван Пендлишак](https://www.youtube.com/watch?v=q27nozKJ0Kg) | видео | готово | [2026-03-11-pryslukhaisya-do-starshykh](2026-03-11-pryslukhaisya-do-starshykh/) |
| `pWu92j8e8bU` | 2026-03-08 | [Побачиш славу Божу - Іван Пендлишак](https://www.youtube.com/watch?v=pWu92j8e8bU) | видео | готово | [2026-03-08-pobachysh-slavu-bozhu](2026-03-08-pobachysh-slavu-bozhu/) |
| `DWtxKouvtqw` | 2026-03-06 | [Ті діла і ви будете робити - Іван Пендлишак](https://www.youtube.com/watch?v=DWtxKouvtqw) | видео | готово | [2026-03-06-ti-dila-i-vy-budete-robyty](2026-03-06-ti-dila-i-vy-budete-robyty/) |
| `RdeQ7lG141k` | 2026-03-05 | [Церква повинна впливати - Іван Пендлишак](https://www.youtube.com/watch?v=RdeQ7lG141k) | трансляция | **скачано без выжимки** | [2026-03-05-tserkva-povynna-vplyvaty](2026-03-05-tserkva-povynna-vplyvaty/) |
| `GThFUvuENGk` | 2026-03-01 | [Господь прийде - Іван Пендлишак](https://www.youtube.com/watch?v=GThFUvuENGk) | видео | готово | [2026-03-01-hospod-pryide](2026-03-01-hospod-pryide/) |
| `XiThcY56Zzg` | 2026-02-27 | [Великий дар від Господа - Іван Пендлишак](https://www.youtube.com/watch?v=XiThcY56Zzg) | видео | готово | [2026-02-27-velykyi-dar-vid-hospoda](2026-02-27-velykyi-dar-vid-hospoda/) |
| `yAvmYX-RT18` | 2026-02-26 | [Так роблячи ніколи не спіткнешся - Іван Пендлишак](https://www.youtube.com/watch?v=yAvmYX-RT18) | трансляция | **скачано без выжимки** | [2026-02-26-tak-roblyachy-nikoly-ne-spitkneshsya](2026-02-26-tak-roblyachy-nikoly-ne-spitkneshsya/) |
| `ISKV4YmSggg` | 2026-02-25 | [Не роби зображення з метою поклоніння - Іван Пендлишак](https://www.youtube.com/watch?v=ISKV4YmSggg) | видео | готово | [2026-02-25-ne-roby-zobrazhennya-z-metoyu-pokloninnya](2026-02-25-ne-roby-zobrazhennya-z-metoyu-pokloninnya/) |
| `muETdiIkor0` | 2026-02-22 | [Це люди придумали - Іван Пендлишак](https://www.youtube.com/watch?v=muETdiIkor0) | видео | готово | [2026-02-22-tse-lyudy-prydumaly](2026-02-22-tse-lyudy-prydumaly/) |
| `iQnyGdHXgU0` | 2026-02-20 | [Він хотів підтримати Бога - Іван Пендлишак](https://www.youtube.com/watch?v=iQnyGdHXgU0) | видео | готово | [2026-02-20-vin-khotiv-pidtrymaty-boha](2026-02-20-vin-khotiv-pidtrymaty-boha/) |
| `kJjlJ3dk1pU` | 2026-02-19 | [Межі твого служіння - Іван Пендлишак](https://www.youtube.com/watch?v=kJjlJ3dk1pU) | трансляция | **скачано без выжимки** | [2026-02-19-mezhi-tvoho-sluzhinnya](2026-02-19-mezhi-tvoho-sluzhinnya/) |
| `oUS2d69Nt34` | 2026-02-18 | [Всі народи прийдуть на Гору Святу - Іван Пендлишак](https://www.youtube.com/watch?v=oUS2d69Nt34) | видео | готово | [2026-02-18-vsi-narody-pryidut-na-horu-svyatu](2026-02-18-vsi-narody-pryidut-na-horu-svyatu/) |
| `dNAFAqBffto` | 2026-02-13 | [Він буде з тобою - Іван Пендлишак](https://www.youtube.com/watch?v=dNAFAqBffto) | видео | готово | [2026-02-13-vin-bude-z-toboyu](2026-02-13-vin-bude-z-toboyu/) |
| `_eAqD_mH4hI` | 2026-02-12 | [Як Бог реагує на милосердя - Іван Пендлишак](https://www.youtube.com/watch?v=_eAqD_mH4hI) | трансляция | **скачано без выжимки** | [2026-02-12-yak-boh-reahuie-na-myloserdya](2026-02-12-yak-boh-reahuie-na-myloserdya/) |
| `5VMgA4kpxBk` | 2026-02-11 | [Ти повинен змінитись - Іван Пендлишак](https://www.youtube.com/watch?v=5VMgA4kpxBk) | видео | готово | [2026-02-11-ty-povynen-zminytys](2026-02-11-ty-povynen-zminytys/) |
| `6YnUmh8lQdE` | 2026-02-08 | [Виклик Богу - Іван Пендлишак](https://www.youtube.com/watch?v=6YnUmh8lQdE) | видео | готово | [2026-02-08-vyklyk-bohu](2026-02-08-vyklyk-bohu/) |
| `-ZpgFHow7EE` | 2026-02-06 | [Благо буде тим, хто боїться Бога - Іван Пендлишак](https://www.youtube.com/watch?v=-ZpgFHow7EE) | видео | готово | [2026-02-06-blaho-bude-tym-khto-boitsya-boha](2026-02-06-blaho-bude-tym-khto-boitsya-boha/) |
| `_bK_KYWXJ1Y` | 2026-02-05 | [Благословіння неба і землі - Іван Пендлишак](https://www.youtube.com/watch?v=_bK_KYWXJ1Y) | трансляция | **скачано без выжимки** | [2026-02-05-blahoslovinnya-neba-i-zemli](2026-02-05-blahoslovinnya-neba-i-zemli/) |
| `L6XOxs1BdRI` | 2026-02-04 | [Не йди від Бога - Іван Пендлишак](https://www.youtube.com/watch?v=L6XOxs1BdRI) | видео | готово | [2026-02-04-ne-idy-vid-boha](2026-02-04-ne-idy-vid-boha/) |
| `udG9Qnnkokw` | 2026-01-30 | [Який образ у нас формує Господь - Іван Пендлишак](https://www.youtube.com/watch?v=udG9Qnnkokw) | видео | готово | [2026-01-30-yakyi-obraz-u-nas-formuie-hospod](2026-01-30-yakyi-obraz-u-nas-formuie-hospod/) |
| `Mwui2bprbUw` | 2026-01-29 | [Слухняність краще жертви - Іван Пендлишак](https://www.youtube.com/watch?v=Mwui2bprbUw) | трансляция | **скачано без выжимки** | [2026-01-29-slukhnyanist-krashche-zhertvy](2026-01-29-slukhnyanist-krashche-zhertvy/) |
| `VlSMjxlgJNk` | 2026-01-28 | [Є про що молитись - Іван Пендлишак](https://www.youtube.com/watch?v=VlSMjxlgJNk) | видео | готово | [2026-01-28-ie-pro-shcho-molytys](2026-01-28-ie-pro-shcho-molytys/) |
| `Ep1Fwjp5Id8` | 2026-01-25 | [Не соромся це виконувати - Іван Пендлишак](https://www.youtube.com/watch?v=Ep1Fwjp5Id8) | видео | готово | [2026-01-25-ne-soromsya-tse-vykonuvaty](2026-01-25-ne-soromsya-tse-vykonuvaty/) |
| `i6CeVbaSuMc` | 2026-01-23 | [Вони залишились самі - Іван Пендлишак](https://www.youtube.com/watch?v=i6CeVbaSuMc) | видео | готово | [2026-01-23-vony-zalyshylys-sami](2026-01-23-vony-zalyshylys-sami/) |
| `-Vi4iniO9YQ` | 2026-01-22 | [Розказати який Бог добрий - Іван Пендлишак](https://www.youtube.com/watch?v=-Vi4iniO9YQ) | трансляция | **скачано без выжимки** | [2026-01-22-rozkazaty-yakyi-boh-dobryi](2026-01-22-rozkazaty-yakyi-boh-dobryi/) |
| `ynKWrrVvZk8` | 2026-01-21 | [Істинно сором'язливий - Іван Пендлишак](https://www.youtube.com/watch?v=ynKWrrVvZk8) | видео | готово | [2026-01-21-istynno-soromyazlyvyi](2026-01-21-istynno-soromyazlyvyi/) |
| `vH7e4SjOJTM` | 2026-01-18 | [Смерть - це надбання - Іван Пендлишак](https://www.youtube.com/watch?v=vH7e4SjOJTM) | видео | готово | [2026-01-18-smert-tse-nadbannya](2026-01-18-smert-tse-nadbannya/) |
| `3tehns5NMUg` | 2026-01-16 | [Як бути радісним - Іван Пендлишак](https://www.youtube.com/watch?v=3tehns5NMUg) | видео | готово | [2026-01-16-yak-buty-radisnym](2026-01-16-yak-buty-radisnym/) |
| `dCGuYEtOk4U` | 2026-01-15 | [Щоб спастися - Іван Пендлишак](https://www.youtube.com/watch?v=dCGuYEtOk4U) | трансляция | **скачано без выжимки** | [2026-01-15-shchob-spastysya](2026-01-15-shchob-spastysya/) |
| `ebVZOz_wBpo` | 2026-01-11 | [Ти мусиш виділяти час - Іван Пендлишак](https://www.youtube.com/watch?v=ebVZOz_wBpo) | видео | готово | [2026-01-11-ty-musysh-vydilyaty-chas](2026-01-11-ty-musysh-vydilyaty-chas/) |
| `ty-h2-rsm4M` | 2026-01-09 | [Для тих, кого любить Бог - Іван Пендлишак](https://www.youtube.com/watch?v=ty-h2-rsm4M) | видео | готово | [2026-01-09-dlya-tykh-koho-lyubyt-boh](2026-01-09-dlya-tykh-koho-lyubyt-boh/) |
| `8ydARlBKras` | 2026-01-09 | [Він не став рабом речей - Іван Пендлишак](https://www.youtube.com/watch?v=8ydARlBKras) | трансляция | **скачано без выжимки** | [2026-01-09-vin-ne-stav-rabom-rechei](2026-01-09-vin-ne-stav-rabom-rechei/) |
| `I4Tkp6A6O2E` | 2026-01-07 | [Так вирішив Бог - Іван Пендлишак](https://www.youtube.com/watch?v=I4Tkp6A6O2E) | видео | готово | [2026-01-07-tak-vyrishyv-boh](2026-01-07-tak-vyrishyv-boh/) |
| `KicU9mwDuWA` | 2026-01-05 | [Навіщо звертатись до лікарів - Іван Пендлишак](https://www.youtube.com/watch?v=KicU9mwDuWA) | видео | **скачано без выжимки** | [2026-01-05-navishcho-zvertatys-do-likariv](2026-01-05-navishcho-zvertatys-do-likariv/) |
| `LzFbu6_mCBM` | 2026-01-02 | [Закон сіяння і жатви - Іван Пендлишак](https://www.youtube.com/watch?v=LzFbu6_mCBM) | видео | **скачано без выжимки** | [2026-01-02-zakon-siyannya-i-zhatvy](2026-01-02-zakon-siyannya-i-zhatvy/) |
| `Sggv5n-Y4iY` | 2026-01-01 | [Де зароджується заздрість? - Іван Пендлишак](https://www.youtube.com/watch?v=Sggv5n-Y4iY) | трансляция | **скачано без выжимки** | [2026-01-01-de-zarodzhuietsya-zazdrist](2026-01-01-de-zarodzhuietsya-zazdrist/) |

## 2025

Всего **192**: скачано без выжимки — 126, не начато — 66. От новых к старым.

| Video ID | Дата | Ролик | Тип | Статус |
|---|---|---|---|---|
| `Ja-CRR-SZfw` | 2025-12-31 | [Секрети плодоносного життя з Богом - Іван Пендлишак](https://www.youtube.com/watch?v=Ja-CRR-SZfw) | видео | **скачано без выжимки** |
| `ZqFLg7so0B8` | 2025-12-29 | [Мій мир з вами - Іван Пендлишак](https://www.youtube.com/watch?v=ZqFLg7so0B8) | видео | **скачано без выжимки** |
| `yWHCaOz-hfw` | 2025-12-28 | [Від радника охороняй душу свою - Іван Пендлишак](https://www.youtube.com/watch?v=yWHCaOz-hfw) | видео | **скачано без выжимки** |
| `og9uk76o8L0` | 2025-12-26 | [Достойний Різдвяний подарунок - Іван Пендлишак](https://www.youtube.com/watch?v=og9uk76o8L0) | видео | **скачано без выжимки** |
| `AMZ22Fljwos` | 2025-12-25 | [Чому Бог допустив це в нашому житті? - Іван Пендлишак](https://www.youtube.com/watch?v=AMZ22Fljwos) | трансляция | **скачано без выжимки** |
| `pesTl4EEjbs` | 2025-12-24 | [Є різні друзі - Іван Пендлишак](https://www.youtube.com/watch?v=pesTl4EEjbs) | видео | **скачано без выжимки** |
| `1x7AKNZHXbA` | 2025-12-21 | [Краще мати сім'ю - Іван Пендлишак](https://www.youtube.com/watch?v=1x7AKNZHXbA) | видео | **скачано без выжимки** |
| `7vhRR1ZEQkU` | 2025-12-19 | [Жорстокість серця - Іван Пендлишак](https://www.youtube.com/watch?v=7vhRR1ZEQkU) | видео | **скачано без выжимки** |
| `DsEUeztJ9jc` | 2025-12-18 | [Сумніви - Іван Пендлишак](https://www.youtube.com/watch?v=DsEUeztJ9jc) | трансляция | **скачано без выжимки** |
| `KeWtYpf68iE` | 2025-12-17 | [Не являйся перед лице Господа з порожніми руками - Іван Пендлишак](https://www.youtube.com/watch?v=KeWtYpf68iE) | видео | **скачано без выжимки** |
| `WGtzH_hR0Zc` | 2025-12-14 | [Не дивись на ближнього - Іван Пендлишак](https://www.youtube.com/watch?v=WGtzH_hR0Zc) | видео | **скачано без выжимки** |
| `_JvofRA22Yc` | 2025-12-12 | [Обітниці - Іван Пендлишак](https://www.youtube.com/watch?v=_JvofRA22Yc) | видео | **скачано без выжимки** |
| `seuookY2aV0` | 2025-12-10 | [Сновидіння - Іван Пендлишак](https://www.youtube.com/watch?v=seuookY2aV0) | видео | **скачано без выжимки** |
| `iGVpMm4hhQI` | 2025-12-07 | [Твоя молитва прийшла до Господа - Іван Пендлишак](https://www.youtube.com/watch?v=iGVpMm4hhQI) | видео | **скачано без выжимки** |
| `Le7AKg9oi9M` | 2025-12-05 | [Терпінням спасайте душі ваші - Іван Пендлишак](https://www.youtube.com/watch?v=Le7AKg9oi9M) | видео | **скачано без выжимки** |
| `uGr6N61_Dik` | 2025-11-30 | [Риси духовної зрілості - Іван Пендлишак](https://www.youtube.com/watch?v=uGr6N61_Dik) | видео | **скачано без выжимки** |
| `dUrhge5BiPs` | 2025-11-28 | [Головна ціль - Іван Пендлишак](https://www.youtube.com/watch?v=dUrhge5BiPs) | видео | **скачано без выжимки** |
| `uq1jxcipmso` | 2025-11-26 | [Завантажити роботою - Іван Пендлишак](https://www.youtube.com/watch?v=uq1jxcipmso) | видео | **скачано без выжимки** |
| `Dq-5rIHMPA8` | 2025-11-23 | [Не давай нікому владу над собою - Іван Пендлишак](https://www.youtube.com/watch?v=Dq-5rIHMPA8) | видео | **скачано без выжимки** |
| `Jkc2us3BOdE` | 2025-11-21 | [Тотальне рабство - Іван Пендлишак](https://www.youtube.com/watch?v=Jkc2us3BOdE) | видео | **скачано без выжимки** |
| `anlWVw1Tq3s` | 2025-11-19 | [А чому так? - Іван Пендлишак](https://www.youtube.com/watch?v=anlWVw1Tq3s) | видео | **скачано без выжимки** |
| `y-FUR9SpKYc` | 2025-11-16 | [Поручитися небезпечно - Іван Пендлишак](https://www.youtube.com/watch?v=y-FUR9SpKYc) | видео | **скачано без выжимки** |
| `-h8_3JYHGZo` | 2025-11-14 | [Хвалися тим, що розумієш і знаєш Господа - Іван Пендлишак](https://www.youtube.com/watch?v=-h8_3JYHGZo) | видео | **скачано без выжимки** |
| `KxPwB--0-rU` | 2025-11-12 | [Він не боїться дати в борг - Іван Пендлишак](https://www.youtube.com/watch?v=KxPwB--0-rU) | видео | **скачано без выжимки** |
| `6YYxs9yV4ts` | 2025-11-07 | [Комплекси - Іван Пендлишак](https://www.youtube.com/watch?v=6YYxs9yV4ts) | видео | **скачано без выжимки** |
| `JXButjAKwgk` | 2025-11-07 | [Вірність - Іван Пендлишак](https://www.youtube.com/watch?v=JXButjAKwgk) | трансляция | **скачано без выжимки** |
| `bW-HaKlrWX8` | 2025-10-31 | [Час особистого прикладу - Іван Пендлишак](https://www.youtube.com/watch?v=bW-HaKlrWX8) | видео | **скачано без выжимки** |
| `m-OnIpItG1k` | 2025-10-30 | [Коли ми будемо з Ним - Іван Пендлишак](https://www.youtube.com/watch?v=m-OnIpItG1k) | трансляция | **скачано без выжимки** |
| `0mhMX8DH9kQ` | 2025-10-26 | [До кого нам йти? - Іван Пендлишак](https://www.youtube.com/watch?v=0mhMX8DH9kQ) | видео | **скачано без выжимки** |
| `Vl_UdzQdr5c` | 2025-10-24 | [Реакція Бога на зухвалість - Іван Пендлишак](https://www.youtube.com/watch?v=Vl_UdzQdr5c) | видео | **скачано без выжимки** |
| `21PIAniAj78` | 2025-10-24 | [Амінь! - Іван Пендлишак](https://www.youtube.com/watch?v=21PIAniAj78) | трансляция | **скачано без выжимки** |
| `yPTtFmzqMQs` | 2025-10-22 | [Відректися від свого Я - Іван Пендлишак](https://www.youtube.com/watch?v=yPTtFmzqMQs) | видео | **скачано без выжимки** |
| `hNNlXl_Wjrk` | 2025-10-17 | [Ви є власність Христа - Іван Пендлишак](https://www.youtube.com/watch?v=hNNlXl_Wjrk) | видео | **скачано без выжимки** |
| `Q3lPKkNJCXI` | 2025-10-17 | [Для кожного є призначення від Господа - Іван Пендлишак](https://www.youtube.com/watch?v=Q3lPKkNJCXI) | трансляция | **скачано без выжимки** |
| `0ZItrRFL8mQ` | 2025-10-12 | [Що зробив Христос - Іван Пендлишак](https://www.youtube.com/watch?v=0ZItrRFL8mQ) | видео | **скачано без выжимки** |
| `de0i_c-dpW0` | 2025-10-10 | [Або здобув вічність або втратив усе - Іван Пендлишак](https://www.youtube.com/watch?v=de0i_c-dpW0) | видео | **скачано без выжимки** |
| `CS7fuhKs6fo` | 2025-10-10 | [Бог любить тих, хто не нарікає - Іван Пендлишак](https://www.youtube.com/watch?v=CS7fuhKs6fo) | трансляция | **скачано без выжимки** |
| `Q2Esa___vbc` | 2025-10-08 | [Що добре для людини - Іван Пендлишак](https://www.youtube.com/watch?v=Q2Esa___vbc) | видео | **скачано без выжимки** |
| `KeSX3Op9pxc` | 2025-10-05 | [Вміння бути задоволеним - Іван Пендлишак](https://www.youtube.com/watch?v=KeSX3Op9pxc) | видео | **скачано без выжимки** |
| `msnjNTuwC_c` | 2025-10-03 | [Чому ми падаємо - Іван Пендлишак](https://www.youtube.com/watch?v=msnjNTuwC_c) | видео | **скачано без выжимки** |
| `UZwGp99_Jsk` | 2025-10-03 | [Чи вмієш ти бути винним? - Іван Пендлишак](https://www.youtube.com/watch?v=UZwGp99_Jsk) | трансляция | **скачано без выжимки** |
| `8EC_gW5mvC0` | 2025-10-01 | [Твій духовний стан - Іван Пендлишак](https://www.youtube.com/watch?v=8EC_gW5mvC0) | видео | **скачано без выжимки** |
| `9hVHksFWyGQ` | 2025-09-28 | [Премудрість Божа цього не вміщає - Іван Пендлишак](https://www.youtube.com/watch?v=9hVHksFWyGQ) | видео | **скачано без выжимки** |
| `gBSaC6tCbYc` | 2025-09-26 | [Духовна система речей. Чистилище - Іван Пендлишак](https://www.youtube.com/watch?v=gBSaC6tCbYc) | видео | **скачано без выжимки** |
| `R8hM54HvFC4` | 2025-09-26 | [Ціль Бога: Нова людина ! - Іван Пендлишак](https://www.youtube.com/watch?v=R8hM54HvFC4) | трансляция | **скачано без выжимки** |
| `f_LUTBlDOQY` | 2025-09-24 | [Однодумність, любов і згода - Іван Пендлишак](https://www.youtube.com/watch?v=f_LUTBlDOQY) | видео | **скачано без выжимки** |
| `RJ7_lLbMTXM` | 2025-09-21 | [Коли живеш як каже Бог - Іван Пендлишак](https://www.youtube.com/watch?v=RJ7_lLbMTXM) | видео | **скачано без выжимки** |
| `P3-F4WvwJe8` | 2025-09-19 | [Не чекай поки зламаєшся під власним тягарем - Іван Пендлишак](https://www.youtube.com/watch?v=P3-F4WvwJe8) | видео | **скачано без выжимки** |
| `YYTp5ot56OA` | 2025-09-19 | [Радійте з тими хто радіє! - Іван Пендлишак](https://www.youtube.com/watch?v=YYTp5ot56OA) | трансляция | **скачано без выжимки** |
| `QyuFwUyOs00` | 2025-09-17 | [Які ознаки нерозумного - Іван Пендлишак](https://www.youtube.com/watch?v=QyuFwUyOs00) | видео | **скачано без выжимки** |
| `ssY4sOSmovQ` | 2025-09-14 | [Сатанинська атака - Іван Пендлишак](https://www.youtube.com/watch?v=ssY4sOSmovQ) | видео | **скачано без выжимки** |
| `F9iT1LtVvMs` | 2025-09-12 | [Страх мучить людину - Іван Пендлишак](https://www.youtube.com/watch?v=F9iT1LtVvMs) | видео | **скачано без выжимки** |
| `unPCJUlG_BY` | 2025-09-10 | [Я стану на сторожі серця мого - Іван Пендлишак](https://www.youtube.com/watch?v=unPCJUlG_BY) | видео, короткое (161 с) | **скачано без выжимки** |
| `JZwna-B-y-U` | 2025-09-07 | [Твоя доля найкраща! - Іван Пендлишак](https://www.youtube.com/watch?v=JZwna-B-y-U) | видео | **скачано без выжимки** |
| `aoUTq9X_xaA` | 2025-09-05 | [Людське Я - Іван Пендлишак](https://www.youtube.com/watch?v=aoUTq9X_xaA) | видео | **скачано без выжимки** |
| `g_wFXfONEdE` | 2025-08-29 | [Чи можуть віруючі впливати на хід війни? Молитва за Україну! - Іван Пендлишак](https://www.youtube.com/watch?v=g_wFXfONEdE) | видео | **скачано без выжимки** |
| `QJGMpsl_Daw` | 2025-08-24 | [Хто перетерпить до кінця, спасеться! - Іван Пендлишак](https://www.youtube.com/watch?v=QJGMpsl_Daw) | видео | **скачано без выжимки** |
| `EImgbB4bvHQ` | 2025-08-10 | [Притча про султана і його 4 дружини - Іван Пендлишак](https://www.youtube.com/watch?v=EImgbB4bvHQ) | видео | **скачано без выжимки** |
| `K0Zi9bsGwI4` | 2025-08-08 | [Хіба є межа Божій силі? - Іван Пендлишак](https://www.youtube.com/watch?v=K0Zi9bsGwI4) | видео | **скачано без выжимки** |
| `jAuggGijkA4` | 2025-08-07 | [Річ, яка береже людину від гріха - Іван Пендлишак](https://www.youtube.com/watch?v=jAuggGijkA4) | трансляция | **скачано без выжимки** |
| `zP4WO-MgUzQ` | 2025-08-06 | [Одяг, вираз лиця і хода - Іван Пендлишак](https://www.youtube.com/watch?v=zP4WO-MgUzQ) | видео | **скачано без выжимки** |
| `wblXRrQbbXQ` | 2025-08-03 | [Спомин смерті Христа - Іван Пендлишак](https://www.youtube.com/watch?v=wblXRrQbbXQ) | видео | **скачано без выжимки** |
| `sYYTofV0Uvs` | 2025-08-01 | [Чим Бог утішає людей - Іван Пендлишак](https://www.youtube.com/watch?v=sYYTofV0Uvs) | видео | **скачано без выжимки** |
| `fvzwiFaOQo0` | 2025-07-31 | [Мідний змій став прообразом - Іван Пендлишак](https://www.youtube.com/watch?v=fvzwiFaOQo0) | трансляция | **скачано без выжимки** |
| `bYVB5_4onfo` | 2025-07-30 | [Ти смакуєш недоліки ближнього? - Іван Пендлишак](https://www.youtube.com/watch?v=bYVB5_4onfo) | видео | **скачано без выжимки** |
| `r6MMY2DNHWk` | 2025-07-27 | [Гріх язика - Іван Пендлишак](https://www.youtube.com/watch?v=r6MMY2DNHWk) | видео | **скачано без выжимки** |
| `Cs26pzf_K8k` | 2025-07-25 | [Тягар минулого і страх майбутнього - Іван Пендлишак](https://www.youtube.com/watch?v=Cs26pzf_K8k) | видео | **скачано без выжимки** |
| `hLvlIP7HC80` | 2025-07-25 | [Як уникнути впливу розчарування - Іван Пендлишак](https://www.youtube.com/watch?v=hLvlIP7HC80) | трансляция | **скачано без выжимки** |
| `vvaPk26PjLs` | 2025-07-23 | [Чи покарав Бог, чи благословив - Іван Пендлишак](https://www.youtube.com/watch?v=vvaPk26PjLs) | видео | **скачано без выжимки** |
| `6mb9CbCzGIQ` | 2025-07-20 | [Не хвалися нечестивими дітьми - Іван Пендлишак](https://www.youtube.com/watch?v=6mb9CbCzGIQ) | видео | **скачано без выжимки** |
| `2U3kaylfd5A` | 2025-07-18 | [Адекватність - Іван Пендлишак](https://www.youtube.com/watch?v=2U3kaylfd5A) | видео | **скачано без выжимки** |
| `XNPLmSqIHc0` | 2025-07-17 | [Три умови спасіння - Іван Пендлишак](https://www.youtube.com/watch?v=XNPLmSqIHc0) | трансляция | **скачано без выжимки** |
| `20LgsuYa130` | 2025-07-16 | [Тому що був в присутності Божій - Іван Пендлишак](https://www.youtube.com/watch?v=20LgsuYa130) | видео | **скачано без выжимки** |
| `0qMuZynJ3gI` | 2025-07-13 | [Доля визначена наперед - Іван Пендлишак](https://www.youtube.com/watch?v=0qMuZynJ3gI) | видео | **скачано без выжимки** |
| `bbA-0jTbL_w` | 2025-07-11 | [Де початок відступлення - Іван Пендлишак](https://www.youtube.com/watch?v=bbA-0jTbL_w) | видео | **скачано без выжимки** |
| `vgCEcCCYisw` | 2025-07-10 | [Ми покликані пройти дорогою Христа - Іван Пендлишак](https://www.youtube.com/watch?v=vgCEcCCYisw) | трансляция | **скачано без выжимки** |
| `kYp1gg-87kA` | 2025-07-09 | [Використай свій акумулятор на повну - Іван Пендлишак](https://www.youtube.com/watch?v=kYp1gg-87kA) | видео | **скачано без выжимки** |
| `n4t4-KlmDxc` | 2025-07-06 | [Давай згідно своїх можливостей - Іван Пендлишак](https://www.youtube.com/watch?v=n4t4-KlmDxc) | видео | **скачано без выжимки** |
| `obDVeEtjHEQ` | 2025-07-04 | [Виконай те, що обіцяв - Іван Пендлишак](https://www.youtube.com/watch?v=obDVeEtjHEQ) | видео | **скачано без выжимки** |
| `5yDQjN_jk7s` | 2025-07-03 | [Тобі важко. Шукай Бога! - Іван Пендлишак](https://www.youtube.com/watch?v=5yDQjN_jk7s) | трансляция | **скачано без выжимки** |
| `48Tbw0PZk7Q` | 2025-06-30 | [Тримайся подалі від гордих - Іван Пендлишак](https://www.youtube.com/watch?v=48Tbw0PZk7Q) | видео | **скачано без выжимки** |
| `J6LfCXKNwhY` | 2025-06-29 | [Правда на стороні сильного - Іван Пендлишак](https://www.youtube.com/watch?v=J6LfCXKNwhY) | видео | **скачано без выжимки** |
| `GqbnwkpIRb0` | 2025-06-27 | [Люди які дані нам Богом - Іван Пендлишак](https://www.youtube.com/watch?v=GqbnwkpIRb0) | видео | **скачано без выжимки** |
| `RJHFilvGto8` | 2025-06-27 | [Приниження ради слави - Іван Пендлишак](https://www.youtube.com/watch?v=RJHFilvGto8) | трансляция | **скачано без выжимки** |
| `ISUezQc0ZVg` | 2025-06-25 | [Що я роблю для Ісуса - Іван Пендлишак](https://www.youtube.com/watch?v=ISUezQc0ZVg) | видео | **скачано без выжимки** |
| `k5Nmi_4SK4s` | 2025-06-23 | [Він дає сили йти далі - Іван Пендлишак](https://www.youtube.com/watch?v=k5Nmi_4SK4s) | видео | **скачано без выжимки** |
| `BotQhRUHbvs` | 2025-06-22 | [Людина отримує те, у що вірить - Іван Пендлишак](https://www.youtube.com/watch?v=BotQhRUHbvs) | видео | **скачано без выжимки** |
| `wmbNO9JQ2ck` | 2025-06-20 | [Як розпізнати що ти в падінні - Іван Пендлишак](https://www.youtube.com/watch?v=wmbNO9JQ2ck) | видео | **скачано без выжимки** |
| `jYsCLgdF1F4` | 2025-06-19 | [Святі грішники - Іван Пендлишак](https://www.youtube.com/watch?v=jYsCLgdF1F4) | трансляция | **скачано без выжимки** |
| `GaYtzNBVVLE` | 2025-06-18 | [Не хвали людину за її красу - Іван Пендлишак](https://www.youtube.com/watch?v=GaYtzNBVVLE) | видео | **скачано без выжимки** |
| `nR6yqunaDL4` | 2025-06-15 | [Смиренного Бог піднесе - Іван Пендлишак](https://www.youtube.com/watch?v=nR6yqunaDL4) | видео | **скачано без выжимки** |
| `ZmKKHcraq-g` | 2025-06-13 | [Як навчитись стримуватись - Іван Пендлишак](https://www.youtube.com/watch?v=ZmKKHcraq-g) | видео | **скачано без выжимки** |
| `IY6pJXPpORM` | 2025-06-13 | [Як стати миротворцем - Іван Пендлишак](https://www.youtube.com/watch?v=IY6pJXPpORM) | трансляция | **скачано без выжимки** |
| `a2huaVy_2XM` | 2025-06-11 | [Який цар - такі і люди - Іван Пендлишак](https://www.youtube.com/watch?v=a2huaVy_2XM) | видео | **скачано без выжимки** |
| `DVpayUxVQ1o` | 2025-06-08 | [Сила Церкви Христа - Іван Пендлишак](https://www.youtube.com/watch?v=DVpayUxVQ1o) | видео | **скачано без выжимки** |
| `kAFBg9twNdM` | 2025-06-06 | [Твоє належить тобі - Іван Пендлишак](https://www.youtube.com/watch?v=kAFBg9twNdM) | видео | **скачано без выжимки** |
| `IebZ-V2w86I` | 2025-06-06 | [Народжений від плоті чи від духа - Іван Пендлишак](https://www.youtube.com/watch?v=IebZ-V2w86I) | трансляция | **скачано без выжимки** |
| `bCk1QScDGUY` | 2025-06-04 | [Пріоритет у дружбі - Іван Пендлишак](https://www.youtube.com/watch?v=bCk1QScDGUY) | видео | **скачано без выжимки** |
| `W0Gw7CR8pps` | 2025-06-01 | [Як уникнути небезпеки - Іван Пендлишак](https://www.youtube.com/watch?v=W0Gw7CR8pps) | видео, короткое (135 с) | **скачано без выжимки** |
| `rJEKEn-blVA` | 2025-05-31 | [Це не твоя вагова категорія - Іван Пендлишак](https://www.youtube.com/watch?v=rJEKEn-blVA) | видео | **скачано без выжимки** |
| `kBFI1xHhRLQ` | 2025-05-30 | [Духовні рівні розвитку - Іван Пендлишак](https://www.youtube.com/watch?v=kBFI1xHhRLQ) | видео | **скачано без выжимки** |
| `-F9q0ORh4Cs` | 2025-05-30 | [Закон у світлі Євангелії - Іван Пендлишак](https://www.youtube.com/watch?v=-F9q0ORh4Cs) | трансляция | **скачано без выжимки** |
| `j4M8HMEU4B4` | 2025-05-25 | [Що таке Боже Царство? - Іван Пендлишак](https://www.youtube.com/watch?v=j4M8HMEU4B4) | видео | **скачано без выжимки** |
| `DHDdoQFy1n8` | 2025-05-23 | [Відповіді немає - Іван Пендлишак](https://www.youtube.com/watch?v=DHDdoQFy1n8) | видео | **скачано без выжимки** |
| `lAAqAXegaMU` | 2025-05-23 | [Що руйнує духовне здоров'я? - Іван Пендлишак](https://www.youtube.com/watch?v=lAAqAXegaMU) | трансляция | **скачано без выжимки** |
| `kW4OhN5_u4I` | 2025-05-21 | [Бог кличе тебе, щоб зробити кращим! - Іван Пендлишак](https://www.youtube.com/watch?v=kW4OhN5_u4I) | видео | **скачано без выжимки** |
| `QQnMMPnbThg` | 2025-05-18 | [Справжній друг - Іван Пендлишак](https://www.youtube.com/watch?v=QQnMMPnbThg) | видео | **скачано без выжимки** |
| `gVla2ifNZuM` | 2025-05-16 | [Як стати мудрим? - Іван Пендлишак](https://www.youtube.com/watch?v=gVla2ifNZuM) | видео | **скачано без выжимки** |
| `XoNUVWj4OyI` | 2025-05-16 | [Люби і будеш щасливим! - Іван Пендлишак](https://www.youtube.com/watch?v=XoNUVWj4OyI) | трансляция | **скачано без выжимки** |
| `FFoauULwlss` | 2025-05-11 | [Укріпися надією на Господа! - Іван Пендлишак](https://www.youtube.com/watch?v=FFoauULwlss) | видео | **скачано без выжимки** |
| `CqMsXWcFI3s` | 2025-05-09 | [Не руйнуй своє життя образами - Іван Пендлишак](https://www.youtube.com/watch?v=CqMsXWcFI3s) | видео | **скачано без выжимки** |
| `I44s5k759Sg` | 2025-05-09 | [Чи є у свободи межі? - Іван Пендлишак](https://www.youtube.com/watch?v=I44s5k759Sg) | трансляция | **скачано без выжимки** |
| `_gy-cDKqdQk` | 2025-05-04 | [До чого досягнув, так і поступай - Іван Пендлишак](https://www.youtube.com/watch?v=_gy-cDKqdQk) | видео | **скачано без выжимки** |
| `6-hfnlL-ghk` | 2025-05-02 | [Освячення через приниження - Іван Пендлишак](https://www.youtube.com/watch?v=6-hfnlL-ghk) | видео | **скачано без выжимки** |
| `3uePJgVE2zQ` | 2025-05-01 | [Пастки сатани: як їх розпізнати та уникнути - Іван Пендлишак](https://www.youtube.com/watch?v=3uePJgVE2zQ) | трансляция | **скачано без выжимки** |
| `v704nmSy9Is` | 2025-04-30 | [Чи готовий ти до труднощів? - Іван Пендлишак](https://www.youtube.com/watch?v=v704nmSy9Is) | видео | **скачано без выжимки** |
| `7l7OkoJ81_4` | 2025-04-29 | [Суть Божого страху - Іван Пендлишак](https://www.youtube.com/watch?v=7l7OkoJ81_4) | видео | **скачано без выжимки** |
| `R8YoiSHCoLk` | 2025-04-28 | [Мудрість випробує тебе - Іван Пендлишак](https://www.youtube.com/watch?v=R8YoiSHCoLk) | видео | **скачано без выжимки** |
| `XW97ZEo8AS8` | 2025-04-27 | [Чого не варто соромитись - Іван Пендлишак](https://www.youtube.com/watch?v=XW97ZEo8AS8) | видео | **скачано без выжимки** |
| `YkW0KTukcrg` | 2025-04-25 | [Бог спасає, але і ти щось роби - Іван Пендлишак](https://www.youtube.com/watch?v=YkW0KTukcrg) | видео | **скачано без выжимки** |
| `gNZzx3lbyGM` | 2025-04-24 | [Багато покликаних, мало вибраних! - Іван Пендлишак](https://www.youtube.com/watch?v=gNZzx3lbyGM) | трансляция | **скачано без выжимки** |
| `q1cbAayxb24` | 2025-04-20 | [Як ефективно будувати стосунки з близькими людьми - Іван Пендлишак](https://www.youtube.com/watch?v=q1cbAayxb24) | видео | **скачано без выжимки** |
| `rYy5qqtgQCU` | 2025-04-18 | [Про важливість позитивного мислення! - Іван Пендлишак](https://www.youtube.com/watch?v=rYy5qqtgQCU) | трансляция | **скачано без выжимки** |
| `Q2J1pWJ43kU` | 2025-04-16 | [Шануй батька і матір - Іван Пендлишак](https://www.youtube.com/watch?v=Q2J1pWJ43kU) | видео | **скачано без выжимки** |
| `UstXM_2hFDY` | 2025-04-11 | [Як навчитися спокійно на все реагувати? - Іван Пендлишак](https://www.youtube.com/watch?v=UstXM_2hFDY) | видео | **скачано без выжимки** |
| `UK3D17tzCic` | 2025-04-10 | [Як очистити своє серце від гріха - Іван Пендлишак](https://www.youtube.com/watch?v=UK3D17tzCic) | трансляция | **скачано без выжимки** |
| `aPXpL5zAmsk` | 2025-04-09 | [До кого ми йдемо, коли біда? - Іван Пендлишак](https://www.youtube.com/watch?v=aPXpL5zAmsk) | видео | **не начато** |
| `2qzOn968VOY` | 2025-04-06 | [Бог з нами, коли ми з ним! - Іван Пендлишак](https://www.youtube.com/watch?v=2qzOn968VOY) | видео | **не начато** |
| `Oq0V2FYiZiU` | 2025-04-04 | [Церква повинна служити людям! - Іван Пендлишак](https://www.youtube.com/watch?v=Oq0V2FYiZiU) | видео | **не начато** |
| `xGcAAro02VM` | 2025-04-03 | [Таємні гріхи - Іван Пендлишак](https://www.youtube.com/watch?v=xGcAAro02VM) | трансляция | **не начато** |
| `fOysGqdoaZs` | 2025-04-02 | [Багато навчатись - мука для тіла - Іван Пендлишак](https://www.youtube.com/watch?v=fOysGqdoaZs) | видео | **не начато** |
| `p4rpuoRaH2Q` | 2025-03-31 | [За все це Бог приведе тебе на суд - Іван Пендлишак](https://www.youtube.com/watch?v=p4rpuoRaH2Q) | видео | **не начато** |
| `95NYUUnTnkY` | 2025-03-30 | [Бог тобі поверне - Іван Пендлишак](https://www.youtube.com/watch?v=95NYUUnTnkY) | видео | **не начато** |
| `bHfJWw9e7pY` | 2025-03-29 | [На все випадок - Іван Пендлишак](https://www.youtube.com/watch?v=bHfJWw9e7pY) | видео | **не начато** |
| `KSoMCaAzjfU` | 2025-03-28 | [Ні в кого немає так, як він бажає - Іван Пендлишак](https://www.youtube.com/watch?v=KSoMCaAzjfU) | видео | **не начато** |
| `vv4supXG2yA` | 2025-03-26 | [Про ефективність домашніх груп - Іван Пендлишак](https://www.youtube.com/watch?v=vv4supXG2yA) | видео | **не начато** |
| `eWVQ2D0Fse4` | 2025-03-24 | [Що посіяв, те прийдеться жати! - Іван Пендлишак](https://www.youtube.com/watch?v=eWVQ2D0Fse4) | видео | **не начато** |
| `aQp6f8KKZnA` | 2025-03-23 | [Репутація важливіша грошей! - Іван Пендлишак](https://www.youtube.com/watch?v=aQp6f8KKZnA) | видео | **не начато** |
| `m9tX1zCOF20` | 2025-03-22 | [Серце мудрого в домі плачу - Іван Пендлишак](https://www.youtube.com/watch?v=m9tX1zCOF20) | видео | **не начато** |
| `yZcfsJw64FM` | 2025-03-21 | [Дух критиканства - Іван Пендлишак](https://www.youtube.com/watch?v=yZcfsJw64FM) | видео | **не начато** |
| `NPUVoOq2dlc` | 2025-03-19 | [За всяке служіння є нагорода! - Іван Пендлишак](https://www.youtube.com/watch?v=NPUVoOq2dlc) | видео | **не начато** |
| `2782wFG4ZjQ` | 2025-03-17 | [Чи любиш ти гроші? - Іван Пендлишак](https://www.youtube.com/watch?v=2782wFG4ZjQ) | видео | **не начато** |
| `lyaZtS7rIz0` | 2025-03-16 | [Бог ніколи не запізнюється! - Іван Пендлишак](https://www.youtube.com/watch?v=lyaZtS7rIz0) | видео | **не начато** |
| `aGduotAmL5o` | 2025-03-15 | [Не обіцяй - Іван Пендлишак](https://www.youtube.com/watch?v=aGduotAmL5o) | видео | **не начато** |
| `LxXLhkBpBAw` | 2025-03-14 | [За скільки би ти продав Христа? - Іван Пендлишак](https://www.youtube.com/watch?v=LxXLhkBpBAw) | видео | **не начато** |
| `brT4AvwG0MM` | 2025-03-12 | [Не все підлягає поясненню - Іван Пендлишак](https://www.youtube.com/watch?v=brT4AvwG0MM) | видео | **не начато** |
| `F_B7Nmn108Q` | 2025-03-10 | [Негативні сторони успіху - Іван Пендлишак](https://www.youtube.com/watch?v=F_B7Nmn108Q) | видео | **не начато** |
| `4TNRoDBSfNo` | 2025-03-09 | [Важливо знати час - Іван Пендлишак](https://www.youtube.com/watch?v=4TNRoDBSfNo) | видео | **не начато** |
| `JIboZDIiplc` | 2025-03-08 | [Як Бог не дасть розуму, гроші не допоможуть! - Іван Пендлишак](https://www.youtube.com/watch?v=JIboZDIiplc) | видео | **не начато** |
| `rK-cy9hCBJk` | 2025-03-07 | [Навчися бути задоволеним! - Іван Пендлишак](https://www.youtube.com/watch?v=rK-cy9hCBJk) | видео | **не начато** |
| `S4uulkY33qU` | 2025-03-05 | [Чому Бог допускає смуток? - Іван Пендлишак](https://www.youtube.com/watch?v=S4uulkY33qU) | видео | **не начато** |
| `QAfrYMw0leM` | 2025-03-03 | [Чотири малих, але наймудріші! - Іван Пендлишак](https://www.youtube.com/watch?v=QAfrYMw0leM) | видео | **не начато** |
| `kAzkzx2YHfg` | 2025-03-02 | [Не дай Бог з Івана пана - Іван Пендлишак](https://www.youtube.com/watch?v=kAzkzx2YHfg) | видео | **не начато** |
| `3V3Dkah3KcE` | 2025-03-01 | [Як Бог парує людей? - Іван Пендлишак](https://www.youtube.com/watch?v=3V3Dkah3KcE) | видео | **не начато** |
| `uNHP7YEvQis` | 2025-02-28 | [Як влаштувати своє життя? - Іван Пендлишак](https://www.youtube.com/watch?v=uNHP7YEvQis) | видео | **не начато** |
| `NMrPPRvMkSA` | 2025-02-27 | [Де межа ненаситності - Іван Пендлишак](https://www.youtube.com/watch?v=NMrPPRvMkSA) | видео | **не начато** |
| `toEjy5DhNUY` | 2025-02-26 | [Звідки береться совість? - Іван Пендлишак](https://www.youtube.com/watch?v=toEjy5DhNUY) | видео | **не начато** |
| `puXwiLNuAzk` | 2025-02-23 | [Святиня Крові Христа - Іван Пендлишак](https://www.youtube.com/watch?v=puXwiLNuAzk) | видео | **не начато** |
| `1DaMuc7zGug` | 2025-02-22 | [Раб чи син - Іван Пендлишак](https://www.youtube.com/watch?v=1DaMuc7zGug) | видео | **не начато** |
| `0-hd_3MOO_4` | 2025-02-21 | [Як дізнатись, що тебе простив  Бог - Іван Пендлишак](https://www.youtube.com/watch?v=0-hd_3MOO_4) | видео | **не начато** |
| `df8BOnYbtDo` | 2025-02-20 | [Що найбільше не любить Бог? - Іван Пендлишак](https://www.youtube.com/watch?v=df8BOnYbtDo) | видео | **не начато** |
| `NL2R9WWTVq8` | 2025-02-19 | [Кайся, поки Бог дає покаяння - Іван Пендлишак](https://www.youtube.com/watch?v=NL2R9WWTVq8) | видео | **не начато** |
| `1LNUVb2t0-g` | 2025-02-17 | [Що високе у людей - те низьке у Бога - Іван Пендлишак](https://www.youtube.com/watch?v=1LNUVb2t0-g) | видео | **не начато** |
| `sH6L3jEIC8I` | 2025-02-16 | [Не зупиняйся на досягнутому - Іван Пендлишак](https://www.youtube.com/watch?v=sH6L3jEIC8I) | видео | **не начато** |
| `kF_IN7n0-Nk` | 2025-02-15 | [Наклепник і сварливий - Іван Пендлишак](https://www.youtube.com/watch?v=kF_IN7n0-Nk) | видео | **не начато** |
| `V9ipHVTJijU` | 2025-02-14 | [Чому бідний, бо лінивий! - Іван Пендлишак](https://www.youtube.com/watch?v=V9ipHVTJijU) | видео | **не начато** |
| `QXP6Uj_uwX0` | 2025-02-12 | [Не відповідай нерозумному - Іван Пендлишак](https://www.youtube.com/watch?v=QXP6Uj_uwX0) | видео | **не начато** |
| `44-DSBSU1fg` | 2025-02-10 | [Незаслужені прокляття - Іван Пендлишак](https://www.youtube.com/watch?v=44-DSBSU1fg) | видео | **не начато** |
| `VVIQpaII5bo` | 2025-02-09 | [Палка і пряник - Іван Пендлишак](https://www.youtube.com/watch?v=VVIQpaII5bo) | видео | **не начато** |
| `O6HQBJLsh7s` | 2025-02-08 | [Методи заохочення - Іван Пендлишак](https://www.youtube.com/watch?v=O6HQBJLsh7s) | видео | **не начато** |
| `jhQvs4ICgQA` | 2025-02-07 | [Чи ти змінився в Христі? - Іван Пендлишак](https://www.youtube.com/watch?v=jhQvs4ICgQA) | видео | **не начато** |
| `bVkp5GbMICA` | 2025-02-05 | [Релігійні крайності - Іван Пендлишак](https://www.youtube.com/watch?v=bVkp5GbMICA) | видео | **не начато** |
| `aBts5MPTVos` | 2025-02-03 | [Знай свої слабкі місця - Іван Пендлишак](https://www.youtube.com/watch?v=aBts5MPTVos) | видео | **не начато** |
| `WaRwDil6YQ0` | 2025-02-02 | [Візьми Ісуса в свій човен - Іван Пендлишак](https://www.youtube.com/watch?v=WaRwDil6YQ0) | видео, короткое (180 с) | **не начато** |
| `O4PC7lV9FIc` | 2025-02-01 | [Чим оскверняється тіло - Іван Пендлишак](https://www.youtube.com/watch?v=O4PC7lV9FIc) | видео | **не начато** |
| `LP-21RAT6ds` | 2025-01-31 | [Одне вино, а скільки проблем - Іван Пендлишак](https://www.youtube.com/watch?v=LP-21RAT6ds) | видео | **не начато** |
| `EmXlI2Qa3BY` | 2025-01-30 | [Раб гріха - Іван Пендлишак](https://www.youtube.com/watch?v=EmXlI2Qa3BY) | видео | **не начато** |
| `YZv-ostq5nY` | 2025-01-29 | [Не дружи з такими - Іван Пендлишак](https://www.youtube.com/watch?v=YZv-ostq5nY) | видео, короткое (171 с) | **не начато** |
| `O7NZzOfBVHQ` | 2025-01-28 | [Як себе поводити в гостях - Іван Пендлишак](https://www.youtube.com/watch?v=O7NZzOfBVHQ) | видео | **не начато** |
| `yQ8gBYFDCO4` | 2025-01-27 | [Бог ненавидить підлість - Іван Пендлишак](https://www.youtube.com/watch?v=yQ8gBYFDCO4) | видео | **не начато** |
| `D4ddpb6ViwQ` | 2025-01-26 | [Вороги бувають різні - Іван Пендлишак](https://www.youtube.com/watch?v=D4ddpb6ViwQ) | видео | **не начато** |
| `cFfdZJC5wy8` | 2025-01-25 | [Як побороти депресію - Іван Пендлишак](https://www.youtube.com/watch?v=cFfdZJC5wy8) | видео | **не начато** |
| `s-qRluRVHGk` | 2025-01-24 | [Тобі кінець, якщо ... - Іван Пендлишак](https://www.youtube.com/watch?v=s-qRluRVHGk) | видео | **не начато** |
| `X5ceJFZqjkE` | 2025-01-23 | [Цих не чіпайте - Іван Пендлишак](https://www.youtube.com/watch?v=X5ceJFZqjkE) | видео | **не начато** |
| `lQHxQTB4fZc` | 2025-01-22 | [Випробувана віра - Іван Пендлишак](https://www.youtube.com/watch?v=lQHxQTB4fZc) | видео | **не начато** |
| `FICEIK9jwrk` | 2025-01-21 | [Орел і ворон - Іван Пендлишак](https://www.youtube.com/watch?v=FICEIK9jwrk) | видео | **не начато** |
| `DLZpavWVkTY` | 2025-01-20 | [Вітер випробувань - Іван Пендлишак](https://www.youtube.com/watch?v=DLZpavWVkTY) | видео | **не начато** |
| `tvI6AHm3r-w` | 2025-01-19 | [Хто любить правду Божу - Іван Пендлишак](https://www.youtube.com/watch?v=tvI6AHm3r-w) | видео | **не начато** |
| `wVmxOL3IyzQ` | 2025-01-18 | [Я тобі покажу - Іван Пендлишак](https://www.youtube.com/watch?v=wVmxOL3IyzQ) | видео | **не начато** |
| `NqsJnCQGiBg` | 2025-01-17 | [Все закінчиться в день смерті - Іван Пендлишак](https://www.youtube.com/watch?v=NqsJnCQGiBg) | видео | **не начато** |
| `GSi1osQMNxI` | 2025-01-16 | [Бог дає перемогу у війнах - Іван Пендлишак](https://www.youtube.com/watch?v=GSi1osQMNxI) | видео | **не начато** |
| `-sq7r9DC0RE` | 2025-01-14 | [Прийми ці благословіння від Господа - Іван Пендлишак](https://www.youtube.com/watch?v=-sq7r9DC0RE) | видео | **не начато** |
