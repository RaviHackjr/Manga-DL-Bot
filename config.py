env_vars = {
  # Get From my.telegram.org
  "API_HASH": "65b44989de9accc59c64691b308da0f7",
  # Get From my.telegram.org
  "API_ID": "22817133",
  #Get For @BotFather
  "BOT_TOKEN": "7758233512:AAHGOQlM6EYfrSp357lMH77DJfWB3Rc3qXo",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "tititititititioooo",
  # Force Subs Channel username without @
  "CHANNEL": "NineAnimeOfficial",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "Chapter {chap_num} {chap_name} @Manhwa_Chat_Ocean",
  # Put Thumb Link 
  "THUMB": "https://i.postimg.cc/LXkqSfRS/android-chrome-512x512.png"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
