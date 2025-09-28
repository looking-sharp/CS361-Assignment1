import subprocess

# start running the other python scripts
subprocess.Popen(["python", "image-service.py"])
subprocess.Popen(["python", "prng-service.py"])

#ensure files are empty
open('prng-service.txt', 'w').close()
open('image-service.txt', 'w').close()

