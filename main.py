
import time
import pyautogui
import pyperclip
import pyautogui
pyautogui.FAILSAFE = True
MY_NAME = "Prince Jain"

from config import *
from groq_ai import get_ai_reply
from utils import should_reply
# Step 1: Open Chrome
pyautogui.click(CHROME_ICON)
time.sleep(1)
last_processed_message = ""   # 🧠 MEMORY

while True:
    time.sleep(LOOP_DELAY)

    # Step 2: Select chat
    pyautogui.moveTo(*CHAT_START)
    pyautogui.dragTo(*CHAT_END, duration=2, button="left")

    # Step 3: Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    pyautogui.click(*AFTER_COPY_CLICK)

    chat_history = pyperclip.paste()
    print("Detected Sumit message:",chat_history)

    # ✅ CONDITION: new + from Mahi
    if should_reply(chat_history, MY_NAME):
        print("🤖 New message detected, replying...")

        reply = get_ai_reply(chat_history)
        pyperclip.copy(reply)

        pyautogui.click(*CHAT_BOX)
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
    else:
        print("⏸ Last message is mine, skipping")