from plyer import notification
import win32com.client
import time
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def get_user_time_input():
    while True:
        try:
            hours = int(input('Enter hours: '))
            minutes = int(input('Enter minutes: '))
            seconds = int(input('Enter seconds: '))
            return hours, minutes, seconds
        except ValueError:
            print('Please enter valid integer values.')


def send_reminder():
 notification.notify(
    title='Water Reminder',
    message='Time to drink water',
    timeout=7
 )
 speaker.Speak('Time to drink water')


def main():
 hours,minutes,seconds= get_user_time_input()
 time_intrval=hours * 3600 + minutes * 60 + seconds
 
 if time_intrval<=0:
    print('time interval should be greater than 0')
    return
 print('Type "exit" at any prompt to stop the reminders.')
 while True:
  send_reminder()
  print('did you drank water:yes or no ')
  ans=input()
  if ans == 'exit':
    print('Exiting the reminder program.')
    break
  t=time.strftime('%H:%M:%S',time.localtime())
  if ans=='yes':
    print('water drank at ',t)
  elif ans=='no':
    print('please consider drinking it, you need to stay hydrated dear!')
  else:
    print('please answer in yes or no ')
 
  time.sleep(time_intrval)

if __name__ == "__main__":
    main()