from gpiozero import LED, Button
import time

led = LED(18)
button = Button(26)

while True:
    time.sleep(0.01) 
    if button.is_pressed:
        led.on()
    else:
        led.off()

    # 작은 쉬는 시간을 줘서 CPU를 풀로 안쓰게 해