from gpiozero import DistanceSensor
from time import sleep

# 1. 하드웨어 설정
# echo: 데이터를 받는 핀 (GPIO 24)
# trigger: 신호를 보내는 핀 (GPIO 23)
# *실제 연결하신 핀 번호로 수정하세요*
sensor = DistanceSensor(echo=18, trigger=17)

print("=== 초음파 거리 측정 시작 (RPi 5) ===")
print("종료하려면 Ctrl+C를 누르세요.")

try:
    while True:
        # 거리 측정 (단위: 미터 -> 센티미터로 변환을 위해 100을 곱함)
        distance = sensor.distance * 100
        print(f"현재 거리: {distance:.1f} cm")
        sleep(1)

except KeyboardInterrupt:
    print("\n측정을 종료합니다.")