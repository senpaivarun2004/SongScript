# 🎵 Eno Eno Aagide Lyric Player

A Python script that plays the song **Eno Eno Aagide** (from Kannada cinema) and displays synchronized, animated lyrics with custom emojis in your terminal.

---

## 🛠️ How It Works (Simply Explained)

1. **Audio Playback**:
   - The script uses `pygame.mixer` to load and play `Eno_Eno_Aagide.mp3` dynamically using relative paths.

2. **Music Synchronization**:
   - Every lyric line is assigned a specific timestamp (in seconds).
   - The script tracks elapsed time since the music started and waits until the exact moment (with a small timing offset calibration) to trigger the next lyric.

3. **Dynamic Typing Effect**:
   - Instead of printing the line all at once, characters are printed one by one.
   - The typewriter speed is automatically adjusted! The script calculates the time difference between the current lyric and the next lyric, and divides that duration by the number of characters in the line (`char_delay = duration / len(line)`). This ensures the line is fully typed out just in time for the next one.

4. **Auto-Dependency Install**:
   - If `pygame` (used for audio playback) is not installed on your system, the script will automatically run `pip install pygame` before starting.

---

## 🚀 How to Run

1. Open your terminal in this directory.
2. Run the script:
   ```bash
   python eno_eno_aagide.py
   ```
