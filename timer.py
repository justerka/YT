import time

def countdown(userSec):
    while userSec>=0:
        minutes, seconds = divmod(userSec,60)
        timer = "{:02d}:{:02d}". format(minutes,seconds)
        print(timer, end="\r")
        time.sleep(1)
        userSec-=1
    print("бітті")

if __name__ == "__main__":
    userSec = int(input("Enter time in seconds:"))
    countdown(userSec)