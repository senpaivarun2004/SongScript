import time
import sys
import os

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
    # Since we are starting the audio at 90.0s, a time_delay of -0.8s works great, 
    # but you can increase/decrease this value if the lyrics type too early or late.
    time_delay = -0.8

    # Start the audio at this position (in seconds)
    # The first lyric starts at 94.5s, so we start the music at 90.0s for a brief intro
    start_pos = 90.0

    # (timestamp_in_seconds, "Lyric Line + Emojis")
    timed_lyrics = [
        (94.5, "Naanontara Alemaari, (•̀ᴗ•́) 🚶🌿"),
        (98.0, "Neenontara Sukumari, (◕‿◕) 🌸😊"),
        (100.5, "Shuruvaagide Preethi Lagori.. (♡‿♡) 💘🎉"),
        (105.0, "Maretogide Mane Daari, (⊙_⊙;) 😵🛣️ ❌"),
        (108.5, "Baa Torisi Daye Tori, (づ｡◕‿‿◕｡)づ 🤲💕"),
        (111.0, "Ninagendu Naanu Aabhaari..! (╯︵╰,) 🙏❤️"),
        (114.0, "Ninagende Bareda Kaagada, (✍◕‿◕) ✍️ 💌"),
        (117.0, "Ninna Kaige Needokaagada, (つ✧ω✧)つ 🤲📜"),
        (119.5, "Edheyalli Helokaagada, (´ . .̫ . `) 🤐❤️"),
        (122.0, "Bhayaveko, Eno.. (⁄ ⁄•⁄ω⁄•⁄ ⁄) 😳💓"),
        (124.5, "Ninaginta Bahala Chendada, (✿ ♥‿♥) 😍🌹"),
        (127.5, "Hudugeerallellu Illada, (☆▽☆) 👑✨"),
        (130.0, "Aakarshane Ninnallide Olave..! (❤ω❤) 💖🥰"),
        (138.0, "Matte..? (¬‿¬) 🤭💭"),
        (140.0, "Aaa, Agogide Maaya.. (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✨🪄💕"),
        (143.0, "Ee, Nanna Muddina Hrudaya.. (ಥ﹏ಥ) ❤️🥹"),
        (145.5, "Aaa, Kudinotake Edavi, (｡♥‿♥｡) 👀💘"),
        (148.0, "Jaari Biddide Jeeva.. (ღ˘⌣˘ღ) 💞🌸"),
        (150.5, "Naa, Rushiyante Idde.. (－‸ლ) 🧘😌"),
        (152.5, "Nee, Kushiyante Bande.. ヽ(•‿•)ノ 😊☀️"),
        (155.0, "Aaa, Mungurula Sarisi, (๑˃ᴗ˂)ﻭ 💇‍♀️✨"),
        (157.0, "Kedisibitte Nee Japava..! (♡ω♡ ) 😍💘"),
    ]

    # Initialize the audio player
    pygame.mixer.init()
    
    # Locate the audio file (check current directory, then check parent directory)
    audio_filename = "Eno_Eno_Aagide.mp3"
    audio_path = os.path.join(os.path.dirname(__file__), audio_filename)
    if not os.path.exists(audio_path):
        audio_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), audio_filename)

    # Load and play starting from start_pos
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(start=start_pos)
    print(f"\n 🎵 Now Playing - Eno Eno Aagide (Clipped to {start_pos}s) 🎵 \n")
    start_time = time.time()
    for i, (timestamp, line) in enumerate(timed_lyrics):
        # Skip lyrics that are before the starting position
        if timestamp + time_delay < start_pos:
            continue

        # Wait until the exact timestamp to start typing
        elapsed = time.time() - start_time
        wait = (timestamp + time_delay - start_pos) - elapsed
        if wait > 0:
            time.sleep(wait)

        # Calculate typing duration so the line finishes right before the next one starts
        if i + 1 < len(timed_lyrics):
            line_duration = timed_lyrics[i + 1][0] - timestamp - 0.3
        else:
            line_duration = 4.0 
        # Keep the typing duration within a reasonable range (between 1.0 and 4.5 seconds)
        # so it does not print too slowly during long musical interludes
        line_duration = min(max(line_duration, 1.0), 4.5)
        type_lyric(line, line_duration)

    # Wait until the song reaches 3:10 (190.0 seconds absolute time)
    # Since we started playing at 90.0s, we play for a total of 100.0 seconds
    target_elapsed = 190.0 - start_pos
    elapsed_now = time.time() - start_time
    remaining_sleep = target_elapsed - elapsed_now
    if remaining_sleep > 0:
        time.sleep(remaining_sleep)
    pygame.mixer.music.stop()

if __name__ == "__main__":
    print_lyrics()
