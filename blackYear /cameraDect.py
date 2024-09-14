import keyboard

# Симулюємо натискання клавіші 'a'
keyboard.press_and_release('a')

# Відслідковуємо натискання клавіші 'q'
keyboard.on_press_key('q', lambda _: print("Клавішу 'q' натиснуто"))