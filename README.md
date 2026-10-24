# Автономный сайт GitHub Sync 2.1

Обычный статический сайт без GitHub Pages и Releases. Кнопки скачивают установщики напрямую из папки `downloads/`, а приложения проверяют новые версии через `updates.json`.

## Состав

- `index.html` — сайт, современный дизайн и переключатель темы.
- `updates.json` — версии, ссылки, описания и SHA-256 установщиков.
- `downloads/GitHubSync-Setup.exe` — Windows 2.1.
- `downloads/GitHubSync-Remote.apk` — Android 2.1, versionCode 3.
- `downloads/GitHubSync-README.md` — инструкция к приложениям.
- `vercel.json` — заголовки скачивания и отключение кеша для `updates.json`.
- `update_manifest.py` — генератор манифеста для следующих версий.

## Локальная проверка

Откройте `index.html` и оставьте папку `downloads` рядом с ним. Для полноценной проверки лучше запустить любой статический HTTP-сервер.

## Бесплатная публикация без GitHub

1. Откройте **https://vercel.com/drop** и войдите в Vercel.
2. Перетащите **всю папку сайта** или содержимое ZIP в зону загрузки.
3. Дождитесь окончания загрузки. Это может занять время из-за размера установщика.
4. Получите адрес вида:

   ```text
   https://your-site.vercel.app
   ```

5. Проверьте ссылки:
   - `https://your-site.vercel.app/`
   - `https://your-site.vercel.app/updates.json`
   - `https://your-site.vercel.app/downloads/GitHubSync-Setup.exe`
   - `https://your-site.vercel.app/downloads/GitHubSync-Remote.apk`

**Важно:** загружайте не только `index.html`, но и `downloads`, `updates.json`, `vercel.json`.

## Включить проверку обновлений в приложениях

После публикации укажите корневой адрес сайта, например `https://your-site.vercel.app`:

- **Windows:** «Настройки → Сайт обновлений», затем кнопка «Обновить».
- **Android:** «Настройки → Сайт обновлений → Проверить обновления».

Добавлять `/updates.json` к адресу не нужно — приложение сделает это само.

## Как выпустить следующее обновление

1. Соберите новые EXE и APK и замените файлы в `downloads/` с сохранением имён.
2. Увеличьте версию и Android `versionCode`.
3. Запустите в папке сайта:

   ```bash
   python update_manifest.py --version 2.2.0 --android-code 4 --notes "Описание новой версии"
   ```

   Скрипт сам вычислит SHA-256 и перезапишет `updates.json`. Можно также отредактировать JSON вручную.
4. Загрузите обновлённую папку на хостинг.

Приложения увидят более высокую версию при следующей ручной проверке. Windows перед запуском установщика проверяет его SHA-256.

## Другой хостинг

Сайт подходит для любого статического хостинга. Структура адресов должна сохраняться:

```text
/index.html
/updates.json
/downloads/GitHubSync-Setup.exe
/downloads/GitHubSync-Remote.apk
```

GitHub нужен приложению для работы с репозиториями, но не используется для размещения этого сайта или обновлений.
