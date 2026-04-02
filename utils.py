# utils.py

def get_last_sender(chat_log):
    last_line = chat_log.strip().split("\n")[-1]

    try:
        # [12:48 am, 02/04/2026] Sumit: Hi
        sender = last_line.split("]")[1].split(":")[0].strip()
        return sender
    except IndexError:
        return None


def should_reply(chat_log, my_name):
    last_sender = get_last_sender(chat_log)

    if last_sender is None:
        return False

    print("🧠 Last sender detected:", last_sender)

    return last_sender.lower() != my_name.lower()