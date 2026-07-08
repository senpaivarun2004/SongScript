# ✨ 🎵 SongScript 🎶 ✨

> A collection of aesthetic, terminal-based lyric player scripts that sync perfectly with your music. 

Enjoy a beautiful, dynamic typewriting experience right in your console as your favorite songs play in the background!

---

## 🚀 Features

* 🎛️ **Synchronized Playback**: Music and lyrics are perfectly aligned using timestamp-based delays.
* ✍️ **Dynamic Typewriting**: The typewriter speed automatically adjusts per line to ensure text finishes printing right when the next lyric begins.
* 🧩 **Zero Setup**: Automatically checks and installs requirements (like `pygame`) if they are missing.
* 🎨 **Aesthetic Terminal Emojis**: Complements every lyric line with custom mood-matching emojis and text faces.

---

## 🎼 Supported Songs

| Song Name | Artist | Language | Folder Link |
| :--- | :--- | :--- | :--- |
| **Deja Vu** | Harry Grover | Punjabi / English | [📁 dejavu](file:///c:/Users/senpq/Projects/SongScript/dejavu) |
| **Eno Eno Aagide** | K. S. Harisankar | Kannada | [📁 Eno Eno Aagide](file:///c:/Users/senpq/Projects/SongScript/Eno%20Eno%20Aagide) |

---

## 🛠️ How to Run

1. Clone or download the repository.
2. Open your terminal in the song's directory (e.g., `dejavu`).
3. Run the python script:
   ```bash
   python dejavu.py
   ```
   *or*
   ```bash
   python eno_eno_aagide.py
   ```

---

## 🛠️ Creating Your Own SongScript

Feel free to add your own songs by following this template:
1. Put your audio file (`.mp3`, `.opus`, etc.) and the script in a new directory.
2. Set up the list of timestamps and lyric lines:
   ```python
   timed_lyrics = [
       (0.5, "First line of the song... 🎵"),
       (4.2, "Second line... ✨")
   ]
   ```
3. Load the audio file via `pygame.mixer` and run!
