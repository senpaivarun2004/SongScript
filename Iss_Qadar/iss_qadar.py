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
        (15.0, "Iss qadar dil ne laya tha tumhein  💔🥺"),
        (18.0, "Toot kar bhi manaya tha tumhein  🫂✨"),
        (22.0, "Iss qadar dil ye tere naal tha  ❤️‍🩹"),
        (26.0, "Khud ko rote bhi hasaya tha tumhein  🥹🥀"),
        (29.0, "Neend tooti sapne chhoote  😔💭"),
        (32.0, "Khwaab dekhe jo sukoon ke  🌌✨"),
        (34.0, "Faasle mein bhi main dhoondhu  🚶‍♂️🔍"),
        (36.0, "Pal tere sukoon ki  🕊️❤️"),
        (39.0, "Kalam tu meri has ke likhta jaa raha tha  ✍️📜"),
        (43.0, "Kya likhu jo meri tu hi na rahi  📝🚫"),
        (46.0, "Mera dil abhi bhi tere paas hai  ❤️🤲"),
        (50.0, "Lekin tujhko na ye ehsaas hai  🥺🥀"),
        (53.0, "Lene aaoonga main tujhse mera dil  🚶‍♂️💔"),
        (55.0, "Doonga usko jiski ye talash hai  💞✨"),
        
        # Long instrumental break
        (75.0, "Iss qadar dil mein laya tha tumhein  💔🥺"),
        (79.0, "Toot kar bhi manaya tha tumhein  🫂✨"),
        (83.0, "Iss qadar dil tere naal tha  ❤️‍🩹"),
        (87.0, "Khud ko rote bhi hasaya tha tumhein  🥹🥀"),
        (91.0, "Katti raat nahi tere ye bagair  🌙😔"),
        (94.0, "Baithi naa le tu kisi ke jo hai ghair  🚫👤"),
        (96.0, "Iss qadar chaha tha tumhein  💞✨"),
        (100.0, "Jaan mera dil tha tera hi ek makaan  🏠❤️"),
        (103.0, "Raatein aati yaadein laati  🌌💭"),
        (106.0, "Khwaabon mein tu muskurati  😊✨"),
        (108.0, "Jaane kahan tu kho sa gaya hai  🌫️🥀"),
        (112.0, "Pyaar likhne baith'ta hoon  ✍️❤️"),
        (115.0, "Yaad tumko hi karta hoon  🥺💭"),
        (117.0, "Kya tu sun rahi hai lafz ko mere  🎧🎶"),
        (120.0, "Iss qadar saya tha tumhein  💔🥺"),
        (124.0, "Toot kar manaya tha tumhein  🫂✨"),
        (128.0, "Iss qadar tu mere naal tha  ❤️‍🩹"),
        (130.0, "Har pal hasaya tha tumhein  🥹🥀")
    ]

    pygame.mixer.init()
    # Ensure you download the MP3 and save it as exactly this name in the same folder!
    pygame.mixer.music.load("Iss Qadar.mp3") 
    pygame.mixer.music.play()

    print("\n 🎵 Now Playing - Iss Qadar (Aviverse) 🎵 \n")

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