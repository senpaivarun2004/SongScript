import time
import sys

try:
    import pygame
except ImportError:
    import subprocess
    print("pygame not found. Installing pygame...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

def type_lyric(line, duration):
    """Type out a lyric line, finishing in roughly 'duration' seconds."""
    if len(line) == 0:
        time.sleep(duration)
        return
    
    # Calculate how long to pause between each character to fill the line duration
    char_delay = duration / len(line)
    
    for char in line:
        sys.stdout.write(char) 
        sys.stdout.flush()     
        time.sleep(char_delay)
    print()

def print_lyrics():
    # Adjust this delay (in seconds) if the lyrics are out of sync with the music overall.
    time_delay = -0.8

    # (timestamp_in_seconds, "Lyric Line + Emojis")
    timed_lyrics = [
        (10.5, "🎵 Eno Eno Aagide.. 🤔✨"),
        (14.0, "Nange Gotte Aagade..! 😵💭❓"),
        (18.5, "🎵 Eno Eno Aagide.. 💫💖"),
        (22.0, "Manasu Haadi Tappide..!! 💓🎶➡️🥹"),
        (29.0, "Aaa, Agogide Maaya.. ✨🪄💕"),
        (32.5, "Ee, Nanna Muddina Hrudaya.. ❤️🥰"),
        (35.0, "Aaa, Kudinotake Edavi, 👀💘"),
        (37.5, "Jaari Biddide Jeeva.. 💞🌸"),
        (40.0, "Naa, Rushiyante Idde.. 🧘😌"),
        (42.0, "Nee, Kushiyante Bande.. 😊☀️💖"),
        (44.0, "Aaa, Mungurula Sarisi, 💇‍♀️✨"),
        (46.5, "Kedisibitte Nee Japava..! 😍💘"),
        (49.0, "🎵 Eno Eno Aagide.. 🤔✨"),
        (52.5, "Nange Gotte Aagade.. 😵💭"),
        (55.5, "Eno Eno Aagide.. 💖💫"),
        (59.0, "Manasu Haadi Tappide.. 💓🎶"),
        (62.0, "Oh Oh Oh…!!! 🥹❤️🎶"),
        
        # Long musical interlude
        (94.5, "Naanontara Alemaari, 🚶🌿"),
        (98.0, "Neenontara Sukumari, 🌸😊"),
        (100.5, "Shuruvaagide Preethi Lagori.. 💘🎉"),
        (105.0, "Maretogide Mane Daari, 😵🛣️❌"),
        (108.5, "Baa Torisi Daye Tori, 🤲💕"),
        (111.0, "Ninagendu Naanu Aabhaari..! 🙏❤️"),
        (114.0, "Ninagende Bareda Kaagada, ✍️💌"),
        (117.0, "Ninna Kaige Needokaagada, 🤲📜"),
        (119.5, "Edheyalli Helokaagada, 🤐❤️"),
        (122.0, "Bhayaveko, Eno.. 😳💓"),
        (124.5, "Ninaginta Bahala Chendada, 😍🌹"),
        (127.5, "Hudugeerallellu Illada, 👑✨"),
        (130.0, "Aakarshane Ninnallide Olave..! 💖🥰"),
        (142.5, "Matte..? 🤭💭"),
        (144.5, "Aaa, Agogide Maaya.. ✨🪄💕"),
        (147.5, "Ee, Nanna Muddina Hrudaya.. ❤️🥹"),
        (150.0, "Aaa, Kudinotake Edavi, 👀💘"),
        (152.5, "Jaari Biddide Jeeva.. 💞🌸"),
        (155.0, "Naa, Rushiyante Idde.. 🧘😌"),
        (157.0, "Nee, Kushiyante Bande.. 😊☀️"),
        (159.5, "Aaa, Mungurula Sarisi, 💇‍♀️✨"),
        (161.5, "Kedisibitte Nee Japava..! 😍💘"),
        
        # Second musical interlude
        (194.0, "Nange Tusu Anumaana, 🤔💭"),
        (196.5, "Nijakuu Idu Naanena, 🪞🥺"),
        (199.0, "Badalaayisibitte Nee Nanna.. 💖🔄"),
        (203.0, "Solillada Huduga Naa, 💪😎"),
        (205.5, "Aadantide Balaheena, 🥺❤️"),
        (207.5, "Noduttire Ninna Naguunaa.. 😊💕✨"),
        (210.5, "Tusu Jamba Ninage Iddaru, 😏🌹"),
        (213.5, "Nanagista Neenu Aadaru, 🥰❤️"),
        (216.0, "Ninna Haage Yaaru Nannanu, 💖🙈"),
        (218.0, "Seledilla Innu..! 💘✨"),
        (221.0, "Jagavella Huduki Bandaru, 🌍🔍"),
        (224.0, "Nanaginta Olle Manasiro, ❤️👑"),
        (226.5, "Kalegaaranu Sigalaaranu Ninage..! 💞🌹✨"),
        (242.0, "Matte..? 🤭💭"),
        (244.0, "Aaa, Agogide Maaya.. ✨🪄💕"),
        (247.0, "Ee, Nanna Muddina Hrudaya.. ❤️🥰"),
        (250.0, "Aaa, Kudinotake Edavi, 👀💘"),
        (252.0, "Jaari Biddide Jeeva.. 💞🌸"),
        (255.0, "Naa, Rushiyante Idde.. 🧘😌"),
        (257.0, "Nee, Kushiyante Bande.. 😊☀️💖"),
        (259.0, "Aaa, Mungurula Sarisi, 💇‍♀️✨"),
        (261.5, "Kedisibitte Nee Japava..! 😍💘"),
        (265.5, "🎵 Eno Eno Aagide.. 🤔💖"),
        (269.0, "Nange Gotte Aagade..! 😵💭❓"),
        (272.5, "Eno Eno Aagide.. 💫❤️"),
        (276.0, "Manasu Haadi Tappide..!! 💓🎶🥹")
    ]

    import os
    # Initialize the audio player
    pygame.mixer.init()
    # Update this to match your audio file's name!
    audio_path = os.path.join(os.path.dirname(__file__), "Eno_Eno_Aagide.mp3")
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    print("\n 🎵 Now Playing - Eno Eno Aagide 🎵 \n")

    start_time = time.time()

    for i, (timestamp, line) in enumerate(timed_lyrics):
        # Wait until the exact timestamp to start typing
        elapsed = time.time() - start_time
        wait = (timestamp + time_delay) - elapsed
        if wait > 0:
            time.sleep(wait)

        # Calculate typing duration so the line finishes right before the next one starts
        if i + 1 < len(timed_lyrics):
            line_duration = timed_lyrics[i + 1][0] - timestamp - 0.3
        else:
            line_duration = 4.0 
        
        line_duration = max(line_duration, 1.0) 

        type_lyric(line, line_duration)

    # Keeps the script running until the song naturally finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

if __name__ == "__main__":
    print_lyrics()