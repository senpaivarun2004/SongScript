import time
import sys
import pygame

def type_lyric(line, duration):
    """Type out a lyric line, finishing in roughly 'duration' seconds."""
    if len(line) == 0:
        time.sleep(duration)
        return
    
    char_delay = duration / len(line)
    
    sys.stdout.write("    ") 
    sys.stdout.flush()
    
    for char in line:
        sys.stdout.write(char) 
        sys.stdout.flush()     
        time.sleep(char_delay)
    print()

def print_lyrics():
    # Adjusted to -0.5 for terminal emoji rendering delay
    time_delay = -0.5 

    timed_lyrics = [
        (17.0, "Nadakkada avalude karimazhi mazhiyundallo  👁️✨"),
        (20.0, "Ningalil nirayunna mozhiyundallo  🗣️🎶"),
        (23.0, "Marupadi parayum valiyundallo  💬✨"),
        (29.0, "Ninnu kuzhi kandappo adi vayittile  🥰"),
        (34.0, "Manjula raathri siriyathu kandappo  🌙😊"),
        (38.0, "Ayyayo nenjila raani karimazhiyula  👸❤️"),
        (42.0, "Kalavaani koonthala kandappo kannannu udakki  💇‍♀️👀"),
        (44.0, "Chirikkale penne  😅"),
        (45.0, "Kalyani ninte vaaratha pulli  😍"),
        (48.0, "Enne nee kulukkile  💓"),
        (50.0, "Kannile niram kandu kayyile vala kandu  👁️💫"),
        (52.0, "Kaalile kulusittu enne nee kudukki  🦶✨"),
        (54.0, "Arayile aranjanam marakketti  🎀"),
        (55.0, "Kidakkumbol enikkente mohangal anapotti  🌊"),
        (59.0, "Ozhukum nokkala nee oruthi  👀"),
        (63.0, "Nottathinakondu chankathu padakka nokkala nee oru  💥💘"),
        (68.0, "Ithu minnaladi ninakkentha pedi  ⚡😨"),
        (70.0, "Kathakadikodi adutha nivadi  🏃‍♂️🚪"),
        (73.0, "Kappithakal paadi arakatta thedi  🎶"),
        (77.0, "Ninnodiyile suganthathinu raamajan thedi  🌸"),
        (80.0, "Tharambukalile chuttuchurayozhukunnu  🔥"),
        (82.0, "Paramanandara sukhamanthu thedunnu  😇"),
        (83.0, "Mohangal kavithakalaakunnu  ✍️❤️"),
        (86.0, "Ullonnu ariyaanida nenju pidikkunnu  💓"),
        (89.0, "Kannadi minnanu vellaaram kannulla  🪞✨"),
        (93.0, "Chelathamayulla penne alankaari  💃"),
        (95.0, "Muttolam mudiyulla kaanan azhagulla  💇‍♀️🌟"),
        (96.0, "Neela mizhiyulla penne  💙👁️"),
        (97.0, "Sringaari karimizhiyulla kalavaani  ✨"),
        (100.0, "Kaar koonthala kandappo  😍💇‍♀️"),
        (104.0, "Karimizhiyulla kalavaani  👀"),
        (108.0, "Kaa koonthalu kandappol kannonnu mudakki  🙈"),
        (111.0, "Chirikkalle pennu kalyani  😂"),
        (112.0, "Ninte paaratha pulli enne nee kudikkilla  🎯"),
        (115.0, "Kannile niram kandu kayyile vala kandu  🌈"),
        (118.0, "Kaalile kolichittu enne nee kudukki  🦶✨"),
        (120.0, "Arayile aranjaanam marakkattil kidakkumbol  🛏️"),
        (123.0, "Enakku mohangal nadappattu ezhukumpothu nokkala  🌊"),
        (127.0, "Nee oruthi notti munna kondu  👀"),
        (131.0, "Chandathu pidakkana nokkala nee oruthee  💖"),
        
        # Beat shift / Long gap
        (145.0, "Manjulla raathri siri kando  🌙😊"),
        (152.0, "Katta kannu kondu muranjaal  👁️⚔️"),
        (155.0, "Ninte karalile priyanga niranjaal  ❤️"),
        (158.0, "Ariyaan karingalil ninne ariyaan  🖤"),
        (161.0, "Ninte kanavala mohangal ariyaam parayaam  💭"),
        (164.0, "Muttaa chiriyathu vatta  😆"),
        (166.0, "Pattaa ketti mudiyile thattaa  🎀"),
        (169.0, "Muttaa kannil penne oru varumaandi  👀"),
        (172.0, "Nee vasaraatti ninte kadakkani munayo  🔪"),
        (175.0, "Karumbi ninte mizhiyo ninte karalila priyamo  👁️❤️"),
        (178.0, "Nee enikkekiya sundara raathriyo  🌌"),
        (181.0, "Sundari penne ninna kandappo  😍"),
        (185.0, "Thotta ente chankilu theeya  🔥"),
        (188.0, "Ninte chundila theno madhura manoharitha  🍯💋"),
        (191.0, "Chelulla paalappu polulla  🥛✨"),
        (193.0, "Punchiri kanden ullonnu kaali  😅"),
        (197.0, "Enchoran chundathe chelulla chaayathe  ☕"),
        (202.0, "Kondannarinjappol nenchakam paali  💓"),
        (208.0, "Karimizhiyulla kalavaandi kaal koonthala kandappo  💇‍♀️👁️"),
        (215.0, "Karimizhiyulla kalavaani koonthala kannappannu dakki  🙈"),
        (219.0, "Chirikkala penne kalyani  😂"),
        (221.0, "Ninte paala pulli enne kudukki kalavaa  😍"),
        (223.0, "Chirikkala penne kalyana  🎶✨")
    ]

    import os
    pygame.mixer.init()
    # Resolve path relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(script_dir, "..", "Kalyani_English_Lyric.mp3")
    pygame.mixer.music.load(audio_path) 
    pygame.mixer.music.play()

    print("\n 🎵 Now Playing - Kalyani 🎵 \n")

    start_time = time.time()

    for i, (timestamp, line) in enumerate(timed_lyrics):
        elapsed = time.time() - start_time
        wait = (timestamp + time_delay) - elapsed
        if wait > 0:
            time.sleep(wait)

        if i + 1 < len(timed_lyrics):
            line_duration = timed_lyrics[i + 1][0] - timestamp - 0.4
        else:
            line_duration = 2.0 
        
        # Keeps text typing smooth but snappy
        line_duration = min(max(line_duration, 0.8), 2.5) 

        type_lyric(line, line_duration)

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

if __name__ == "__main__":
    print_lyrics()