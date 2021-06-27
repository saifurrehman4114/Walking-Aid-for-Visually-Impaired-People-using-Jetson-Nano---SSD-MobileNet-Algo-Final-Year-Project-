import os 

import multiprocessing




def docker_init():
    
    os.system('gnome-terminal -x bash -c "docker/run.sh -v ~/jetson-inference:/jetson-inference -r ./packages_download_run_model.sh"')
    
    	
def autolabeling_init():

    os.system('python3 auto_labeling.py')



     
p1 = multiprocessing.Process(target=docker_init)

#p2 = multiprocessing.Process(target=autolabeling_init)



# starting process 1
p1.start()

# starting process 2
#p2.start()

while True:
 
 autolabeling_init()


