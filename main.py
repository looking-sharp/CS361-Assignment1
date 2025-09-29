import subprocess
import time
from PIL import Image

prngFileName = "prng-service.txt"
imageFileName = "image-service.txt"

def waitForResponseMessage(waitingFor):
    time.sleep(0.3)
    print(f"waiting for response from {waitingFor}")
    for i in range(3):
        time.sleep(0.5)
        print(f".")
    time.sleep(0.3)

# start running the other python scripts
subprocess.Popen(["python", "image-service.py"])
subprocess.Popen(["python", "prng-service.py"])

#ensure files are empty
open(prngFileName, 'w').close()
open(imageFileName, 'w').close()

time.sleep(0.5)
print('')
while(1):
    userResponse = (int)(input("Would you like to (1) See a Chest CT (2) exit: "))
    print()
    if(userResponse == 2):
        break
    # tell prng service to run
    with open(prngFileName, 'w') as f:
        f.write('run')
    # wait for prng service to return random number
    prngResponse = None
    with open(prngFileName, 'r') as f:
        # wait for number to be in file
        while(f.read().strip() == 'run'):
            f.seek(0) # reset file pointer
            waitForResponseMessage("prng service")
            time.sleep(0.5)
        f.seek(0) # reset file pointer
        prngResponse = f.read()
        # display response
        print(f"Response Recieved: {prngResponse} \n")
    time.sleep(1)
    # give random number to image service
    with open(imageFileName, 'w') as f:
        f.write(prngResponse)
    # wait for image service to return random image
    imageResponse = None
    with open(imageFileName, 'r') as f:
        # wait for number to be in file
        while(f.read().isdigit()):
            f.seek(0) # reset file pointer
            waitForResponseMessage("image service")
            time.sleep(0.5)
        f.seek(0) # reset file pointer
        imageResponse = f.read()
        # display response
        print(f"Response Recieved: {imageResponse} \n")
    time.sleep(0.5)

    img = Image.open(imageResponse)
    img.show()
    
    
    
        

