import mouse
import keyboard
from time import time

repeats = int(input("Repeticiones del bucle: "))

clicks_down = []
clicks_up = []

# teach_movements

print("El bot esta aprendiendo")

is_pressing = False
duration_click = 0
time_to_click = time()

while True:
    if keyboard.is_pressed('ESCAPE'):
        break
    if mouse.is_pressed():
        if not is_pressing:
            is_pressing = True
            clicks_down.append([mouse.get_position(), time() - time_to_click])
            duration_click = time()
    else:
        if is_pressing:
            is_pressing = False
            clicks_up.append([mouse.get_position(), time() - duration_click])
            time_to_click = time()

while keyboard.is_pressed('ESCAPE'):
    pass

# repeat_movements

print("El bot ha iniciara!")

finish = False
i = 0
k = 0
is_bot_pressing = False
time_current = time()
time_before_up_click = 0
time_before_down_click = time() + clicks_down[0][1]

while i < repeats and not finish:

    if keyboard.is_pressed('ESCAPE'):
        finish = True
        break

    if time() > time_before_down_click and k < clicks_down.__len__():
        if not is_bot_pressing:
            is_bot_pressing = True
            time_before_up_click = time() + clicks_up[k][1]
            mouse.move(clicks_down[k][0][0], clicks_down[k][0][1], True)
            mouse.press()
        elif is_bot_pressing and time() >= time_before_up_click:
            is_bot_pressing = False
            if k < clicks_down.__len__() - 1:
                time_before_down_click = time() + clicks_down[k + 1][1]
            mouse.move(clicks_up[k][0][0], clicks_up[k][0][1], True)
            mouse.release()
            k += 1

    # print("time: {}, next: {}".format(time_current, time_before_down_click))

    elif k >= clicks_up.__len__():
        k = 0
        i += 1
        time_current = time()
        time_before_up_click = 0
        time_before_down_click = time() + clicks_down[0][1]

    if i >= repeats:
        finish = True
        break

exit()
