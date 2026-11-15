import time
import sys

try:
    import pygame
except ImportError:
    import subprocess
    print("pygame not found. Installing pygame...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

# ==========================================
# 1. CONFIGURATION
# ==========================================
SONG_TITLE = "Prema Yatra ❤️ (Telugu Audio / English Lyrics)"
AUDIO_FILE = r"C:\Users\senpq\Projects\GitHub\SongScript\Prema_Yatra\Prema Yatra.mp3"  # Matches your uploaded filename

# Fine-tune offset in seconds if your audio player has slight startup latency (e.g., -0.2 or +0.2)
SYNC_OFFSET = 0.0

# Exact timestamps mapped directly from Prema Yatra.mp3
TIMED_LYRICS = [
    (11.8, "--- [Verse 1 – Rama] ---"),
    (12.0, "I have been searching for you, for so many years,  (v_v)"),
    (17.5, "Every step, every tear, my eyes look towards the sky.  (T_T)"),
    (23.5, "I have waited for you, my heart holds a truth so deep,  ( ◡_◡)"),
    (29.0, "When I look into your eyes, I see my world, my dreams.  (✧_✧)"),

    (35.8, "--- [Verse 1 – Sita] ---"),
    (36.0, "Rama, I have been waiting for you, my beloved,  (˘▾˘)"),
    (41.5, "Through every struggle, through every fear.  (._.)"),
    (46.0, "My heart is pure, shining bright like the moon,  (✿◠‿◠)"),
    (52.0, "I am ready now, to hold you close and never let go.  (づ｡◕‿‿◕｡)づ"),

    (65.3, "--- [Chorus – Together] ---"),
    (65.5, "When I see you, words fade away,  (O_o)"),
    (71.5, "Our hearts unite, yet I cannot find the words to say.  (♡_♡)"),
    (77.5, "Rama and Sita, a love divine,  ✨(˘▾˘)✨"),
    (83.0, "I am yours, and you are mine, for all of time.  (♥_♥)"),

    (96.8, "--- [Verse – Rama] ---"),
    (97.0, "Even the wind cannot stop me, every morning calls your name,  (~_~)"),
    (102.5, "I could never forget you, my love remains the same.  ( ◡_◡)"),
    (107.5, "I've crossed countless stones and endless roads to find you,  (ง •̀_•́)ง"),
    (113.5, "And now I've stepped into a love that's pure and true.  (✧_✧)"),

    (119.3, "--- [Verse 2 – Sita] ---"),
    (119.5, "Without you, my life feels incomplete,  (v_v)"),
    (125.0, "Without you, even moonlight and melodies lose their beauty.  (T_T)"),
    (131.0, "I am here now, with everything I have to say,  (o_o)"),
    (136.5, "Lost in your love, I wish to forever stay.  (˘▾˘)"),

    (142.8, "--- [Verse 2 – Rama] ---"),
    (143.0, "The love I have for you flows endlessly,  ~(˘▾˘~)"),
    (148.5, "Perhaps I'm crazy in love, completely.  (@_@)"),
    (154.0, "In my heart, there is only you,  (♥_♥)"),
    (157.5, "Sita, my love, my sweetest dream come true.  (✿◠‿◠)"),

    (161.8, "--- [Chorus – Together] ---"),
    (162.0, "When I see you, words fade away,  (O_o)"),
    (167.5, "Our hearts unite, yet I cannot find the words to say.  (♡_♡)"),
    (173.5, "Rama and Sita, a love divine,  ✨(˘▾˘)✨"),
    (179.0, "I am yours, and you are mine, for all of time.  (♥_♥)"),

    (184.8, "--- [Bridge – Rama] ---"),
    (185.0, "I will never let you go; love is our journey,  (づ￣ ³￣)づ"),
    (190.5, "Every moment with you is a beautiful story.  ( ◡_◡)"),
    (195.5, "Sita, with you, through every night and every dawn,  (˘▾˘)"),
    (200.5, "You are the queen of my heart, my forever one.  👑(✧_✧)"),

    (206.3, "--- [Bridge – Sita] ---"),
    (206.5, "This day, this night, Rama, you live within my heart,  (♡_♡)"),
    (212.0, "Your love is my salvation, my beautiful start.  (✿◠‿◠)"),
    (217.5, "This journey will never end, even through tears we stand,  (T_T)♡"),
    (223.0, "Now my heart sees beauty in love, hand in hand.  (づ｡◕‿‿◕｡)づ"),

    (228.8, "--- [Final Chorus – Together] ---"),
    (229.0, "When I see you, words fade away,  (O_o)"),
    (234.5, "Our hearts unite, yet I cannot find the words to say.  (♡_♡)"),
    (240.5, "Rama and Sita, a love divine,  ✨(˘▾˘)✨"),
    (246.0, "I am yours, and you are mine, for all of time.  (♥_♥)"),
]
# ==========================================


def type_lyric(line, duration):
    """Types out a lyric line smoothly over 'duration' seconds."""
    if not line:
        time.sleep(duration)
        return

    # Print section dividers instantly
    if line.startswith("---") and line.endswith("---"):
        print(f"\n{line}")
        return

    char_delay = duration / len(line)
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()


def play_lyrics():
    """Plays Prema Yatra.mp3 and types out the synced English lyrics."""
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_FILE)
    pygame.mixer.music.play()

    print(f"\n 🎵 Now Playing - {SONG_TITLE} 🎵 \n")
    start_time = time.time()

    for i, (timestamp, line) in enumerate(TIMED_LYRICS):
        elapsed = time.time() - start_time
        wait = (timestamp + SYNC_OFFSET) - elapsed
        if wait > 0:
            time.sleep(wait)

        if i + 1 < len(TIMED_LYRICS):
            line_duration = TIMED_LYRICS[i + 1][0] - timestamp - 0.25
        else:
            line_duration = 4.5

        line_duration = max(line_duration, 0.8)
        type_lyric(line, line_duration)

    # Keep script alive through the final outro reprise until the track ends
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)


if __name__ == "__main__":
    play_lyrics()