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
    time_delay = 14.5

    # (timestamp_in_seconds, "Lyric Line")
    # I have added your lyrics here! You just need to tweak the seconds (the first number).
    timed_lyrics = [
        (0.5, "Sometimes, it hits like that  (v_v)"),
        (3.0, "I'm moving but my mind's on you  ( ◡_◡)"),
        (6.0, "Some nights, it feels like that  (._.)"),
        (9.0, "My mind keeps spinnin' back to you  (@_@)"),
        (12.0, "Kaise kahun eh dil nu mai  (T_T)"),
        (15.0, "Kyun tu samajh na paaye ab  (o_o)"),
        (18.0, "Teri yaadon mai — mai bhi, mai bhi  (~_~)"),
        (21.0, "Kaise kahun eh dil nu mai  (T_T)"),
        (24.0, "Kyun tu samajh na paaye ab  (o_o)"),
        (27.0, "Teri yaadon mai — mai bhi, mai bhi  (~_~)"),
        (30.0, "You stay on my mind  (˘▾˘)"),
        (32.0, "On my mind  (˘▾˘)"),
        (34.0, "It feels like  (O_o)"),
        (36.0, "Deja vu  (✧_✧)"),
        (38.0, "You stay on my mind  (˘▾˘)"),
        (40.0, "On my mind  (˘▾˘)"),
        (42.0, "It feels like  (O_o)"),
        (44.0, "Deja vu  (✧_✧)"),
        (46.0, "De de de de de de  ヾ(⌐■_■)ノ♪"),
        (48.0, "(Deja vu)  ヾ(⌐■_■)ノ♪"),
        (50.0, "De de de de de de  ♪(┌・。・)┌"),
        (52.0, "(It feels like deja vu)  ヾ(⌐■_■)ノ♪"),
        (54.0, "De de de de de de  ~(˘▾˘~)"),
        (56.0, "Deja vuu  (✧_✧)"),
        (58.0, "De de de de de de de  ~(‾▿‾)~"),
        (61.0, "Oh, Aaj v  (._.)"),
        (63.0, "Laggya kuch yun  (v_v)"),
        (66.0, "Chalde-chalde teri yaad hi aa jaave  ( ◡_◡)"),
        (69.0, "I kinda fade out mid-talk  (O_O)"),
        (72.0, "One more trigger brings me  (0_0)"),
        (74.0, "Right back  (O_o)"),
        (76.0, "Right back  (!__!)"),
        (78.0, "Kaise kahun eh dil nu mai  (T_T)"),
        (81.0, "Kyun tu samajh na paaye ab  (o_o)"),
        (84.0, "Teri yaadon mai — mai bhi, mai bhi  (~_~)"),
        (87.0, "Kaise kahun eh dil nu mai  (T_T)"),
        (90.0, "Kyun tu samajh na paaye ab  (o_o)"),
        (93.0, "Teri yaadon mai — mai bhi, mai bhi  (~_~)"),
        (96.0, "You stay on my mind  (˘▾˘)"),
        (98.0, "On my mind  (˘▾˘)"),
        (100.0, "It feels like  (O_o)"),
        (102.0, "Deja vu  (✧_✧)"),
        (104.0, "You stay on my mind  (˘▾˘)"),
        (106.0, "On my mind  (˘▾˘)"),
        (108.0, "It feels like  (O_o)"),
        (110.0, "Deja vu  (✧_✧)"),
        (112.0, "De de de de de de  ヾ(⌐■_■)ノ♪"),
        (114.0, "(Deja vu)  ヾ(⌐■_■)ノ♪"),
        (116.0, "De de de de de de  ♪(┌・。•)┌"),
        (118.0, "(It feels like deja vu)  ヾ(⌐■_■)ノ♪"),
        (120.0, "De de de de de de  ~(˘▾˘~)"),
        (122.0, "Deja vuu  (✧_✧)"),
        (124.0, "De de de de de de de  ~(‾▿‾)~")
    ]

    # Initialize the audio player
    pygame.mixer.init()
    # Ensure your audio file is named exactly this and in the same folder
    pygame.mixer.music.load(r"C:\Users\senpq\Projects\python\deja_vu_audio.opus")
    pygame.mixer.music.play()

    print("\n 🎵 Now Playing - Deja Vu (Harry Grover) 🎵 \n")

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