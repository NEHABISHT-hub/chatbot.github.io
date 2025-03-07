import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
  api_key="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",
)

def is_last_message_from_sender(chat_log, sender_name="NiCk"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024")[-1]
    
    if sender_name in messages:
       return True
    return False
    
    # Step 1: Click at (1472, 1047)
pyautogui.click(1395, 1050)
time.sleep(1)  # Wait a moment

while True:
    time.sleep(3)

    # Step 2: Click and drag from (704, 231) to (1274, 897)
    pyautogui.moveTo(718, 222)
    pyautogui.dragTo(1073, 910, duration=2,button='left')  # Drag smoothly



    # Step 4: Copy text to clipboard (Ctrl + C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)
    pyautogui.click(714,279)

    # Step 5: Retrieve copied text
    chat_history = pyperclip.paste()
    # Now you can use copied_text as a variable in your script
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named neha who speaks hindi as well as english. she is from India and is a coder. You analyze chat history and respond like neha. output should be the next chat response (text only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response =completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 6: Click at (1234, 967)
        pyautogui.click(1234, 967)
        time.sleep(1)

        # Step 7: Paste copied text (Ctrl + V)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        # Step 8: Press Enter
        pyautogui.press("enter")