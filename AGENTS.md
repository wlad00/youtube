# AGENTS.md

Репозиторий с конспектами YouTube-видео христианских авторов и субтитрами к ним.

## Структура

```
alexander-bolotnikov/
  lessons/    — библейские уроки
  streams/    — стримы
ivan-pendlishak/
  <файлы прямо в папке>
```

Папка автора — слаг «имя-фамилия» латиницей. Новый автор — новая папка верхнего уровня.

## Именование файлов

`ГГГГ-ММ-ДД-slug.<ext>` — дата публикации видео на YouTube, slug из названия транслитом.
Если известен только месяц — `ГГГГ-ММ-slug` (как у `ivan-pendlishak`).

Конспект и субтитры одного видео носят одинаковое базовое имя:

```
2026-08-22-zakon-ili-duh.md
2026-08-22-zakon-ili-duh.ru.srt
```

## Скачивание субтитров

Когда пользователь пишет «скачай субтитры: `<ссылка>`» — без других уточнений:

1. Определить автора и дату публикации видео, выбрать папку и имя по правилам выше.
2. Скачать русские субтитры в `.srt`.
3. `--sub-langs "ru.*"` обычно отдаёт два идентичных файла (`.ru.srt` и `.ru-orig.srt`) — оставить `.ru.srt`, второй удалить.
4. Не коммитить без явной просьбы.

Рабочая команда (запускать из корня репозитория):

```powershell
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "ru.*" --convert-subs srt -o "<папка>/<имя>.%(ext)s" "<ссылка>"
```

Cookies (`--cookies-from-browser chrome`) для публичных видео не нужны. Добавлять только если YouTube ответит `Sign in to confirm you're not a bot`; при этом Chrome должен быть закрыт, иначе файл cookies заблокирован.

### Если `yt-dlp` не найден в PATH

Установлен через winget, но PATH обновляется только в новых оболочках. Явные пути:

```
yt-dlp:  %LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe
ffmpeg:  %LOCALAPPDATA%\Microsoft\WinGet\Packages\yt-dlp.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-N-125875-g5d4d3bdc61-win64-gpl\bin
```

`--convert-subs srt` требует ffmpeg — при запуске по явному пути добавлять `--ffmpeg-location <путь к bin>`.

Предупреждение `No supported JavaScript runtime could be found` на скачивание субтитров не влияет.

## Формат конспекта

`.md` с шапкой: заголовок, автор, тип, ссылка на YouTube, Video ID, дата публикации, дата обновления конспекта. Дальше — раздел об источнике, «Коротко», «Подробный конспект» с нумерованными разделами. Ориентироваться на существующие файлы.
