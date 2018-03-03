import time
import RPi.GPIO as GPIO
import os
def arm_down():

    
    GPIO.output(10,1)#arm downward
    GPIO.output(11,0)
    time.sleep(1)
    print("downward")

def arm_up():
    
    
    GPIO.output(10,0)#arm up
    GPIO.output(11,1)
    time.sleep(1)
    print("upward")
    


GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 6 in board FROM 3.3
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 6 in board FROM 5
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 7 in board FROM 3.3
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 8 in board FROM 3.3
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 8 in board FROM 5
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #pin number 8 in board FROM 5

GPIO.setup(9,GPIO.OUT) #pin number 6 in board FROM 3.3
GPIO.setup(2,GPIO.OUT) #pin number 2 in board FROM 3.3
GPIO.setup(3,GPIO.OUT) #pin number 3 in board FROM 3.3
GPIO.setup(26,GPIO.OUT) #pin number 4 in board FROM 3.3
GPIO.setup(10,GPIO.OUT) #pin number 4 in board FROM 3.3
GPIO.setup(11,GPIO.OUT) #pin number 4 in board FROM 3.3
GPIO.setup(25,GPIO.OUT) #pin number 4 in board FROM 3.3
GPIO.output(25,0)#buzzer


while(1):
    GPIO.output(25,0)#buzzer
    
    GPIO.output(10,1)#arm
    GPIO.output(11,1)
    

    start = 0
            
    sw1 = GPIO.input(22)
    
   
    if(sw1==1):
        start =1
        print("robo starts")
    
    
    
    #forward 1-0-1-0
    #reverse 0-1-0-1
    #right 0-0-1-0
    #left 1-0-0-0
    #relay 1 - gpio 9 - 6 wheel
     #relay 2 - gpio2 - 2 wheel
     #relay 3 - gpio3 - 3 wheel
     #relay 4 - gpio4 - 4 wheel
    while(start):
        os.system("mosquitto_pub -t control -m robo starts ")
        
        lim_up = GPIO.input(17)
        lim_down= GPIO.input(18)
        ir = GPIO.input(27)
        ir2 = GPIO.input(8)
        sw2 = GPIO.input(23)
        GPIO.output(25,0)#buzzer
        if(sw2==1):
            print("robo stop")
            os.system("mosquitto_pub -t control -m robo stops ")
            start=0
            GPIO.output(25,0)#buzzer

                
        


        while(lim_up!=1 and ir2==0 and ir==0):
            
            lim_up = GPIO.input(17)
            lim_down= GPIO.input(18)
            GPIO.output(25,0)#buzzer
            ir = GPIO.input(27)
            ir2 = GPIO.input(8)
            arm_up()

                
        while(lim_down!=1 and ir2==0 and ir==0):
            
            lim_up = GPIO.input(17)
            lim_down= GPIO.input(18)
            GPIO.output(25,0)#buzzer
            ir = GPIO.input(27)
            ir2 = GPIO.input(8)
            #print()
            arm_down()
            
            
            
 

        while(ir2==1):#lim1 is high
            print("no action arm in bottom")
            GPIO.output(10,0)#arm
            GPIO.output(11,0)
            GPIO.output(2,0)#motor 
            GPIO.output(3,0)
            GPIO.output(26,0)
            GPIO.output(9,0)
            GPIO.output(25,1)#buzzer
            time.sleep(1)

            os.system("mosquitto_pub -t control -m object_detected  ")

        
        



                
        while(lim_down==1 and ir==1 and lim_up ==0):#lim1 is high and ir high
            GPIO.output(25,0)#buzzer
            print("object detected lifting object")
            os.system("mosquitto_pub -t control -m  object_in_bottom")
            lim_up = GPIO.input(17)
            lim_down= GPIO.input(18)


            GPIO.output(2,0)#motor stop
            GPIO.output(3,0)
            GPIO.output(26,0)
            GPIO.output(9,0)
            #time.sleep(5)
            
            


        while(lim_up==1 and ir==1 and lim_down==0):
            
            GPIO.output(25,0)#buzzer
            print("arm in up with object")
            lim_up = GPIO.input(17)
            lim_down= GPIO.input(18)
            #arm_down()
            GPIO.output(10,1)#arm downward
            GPIO.output(11,1)
           
            

            
           


            print("motor backward")
            GPIO.output(2,0)#motor backward 
            GPIO.output(3,0)
            GPIO.output(26,1)
            GPIO.output(9,1)
            time.sleep(6)
            
            print("motor left")
            GPIO.output(2,0)#motor left 
            GPIO.output(3,1)
            GPIO.output(26,0)
            GPIO.output(9,1)
            time.sleep(6)
            print("motor forward")
            GPIO.output(2,1)#motor forward 
            GPIO.output(3,1)
            GPIO.output(26,0)
            GPIO.output(9,0)
            time.sleep(6)
            print("motor stop")
            os.system("mosquitto_pub -t control -m object_placed_in_room ")
            GPIO.output(2,0)#motor stop 
            GPIO.output(3,0)
            GPIO.output(26,0)
            GPIO.output(9,0)
            time.sleep(6)
            #arm_down()
            print("motor backward")
            GPIO.output(2,0)#motor backward 
            GPIO.output(3,0)
            GPIO.output(26,1)
            GPIO.output(9,1)
            time.sleep(6)

            print("motor right")
            GPIO.output(2,1)#motor left 
            GPIO.output(3,0)
            GPIO.output(26,1)
            GPIO.output(9,0)
            time.sleep(6)

            print("motor forward")
            GPIO.output(2,1)#motor forward 
            GPIO.output(3,1)
            GPIO.output(26,0)
            GPIO.output(9,0)
            time.sleep(6)

            GPIO.output(2,0)#motor stop 
            GPIO.output(3,0)
            GPIO.output(26,0)
            GPIO.output(9,0)
            time.sleep(6)
            while(lim_down==0):
                  
                  
                  lim_down= GPIO.input(18)
                  arm_down()
                  
            #lim_up = GPIO.input(17)
            #lim_down= GPIO.input(18)
          
                      
                      
                  
                  
                
            
            

            
            
        

