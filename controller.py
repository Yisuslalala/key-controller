import keyboard 


# while True:
#     # Wait for the next event.
#     event = keyboard.read_event()
#     if event.event_type == keyboard.hook("ctrl") and event.name == 'space':
#         keyboard.wait('space was pressed')

count = 0
while True: 
    count = count + 1
    message = ""
    message = keyboard.is_pressed("ctrl")
    print(f"message: {message}, count: {count}")