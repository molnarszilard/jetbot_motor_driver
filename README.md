# jetbot_motor_driver

I have a Jetbot from sparkfun. I have noticed that the included motor driver is not working (Remote I/O error), so I've done some research.

I have found this repo: https://github.com/sparkfun/Qwiic_SCMD_Py

Here the driver is implemented a little bit differently, but it seems to work with a Qwiic motor driver, and the Jetpack 4.6.

I have done the following:

downloaded the jetbot repo:

git clone https://github.com/hailoclu/jetbot.git

or 

git clone https://github.com/NVIDIA-AI-IOT/jetbot

If you project is run inside a jupyter lab/notebook, then run the following using the integrated terminal.
Clone the qwiic repo inside jetbot/jetbot/:

git clone https://github.com/sparkfun/Qwiic_SCMD_Py.git

cd Qwiic_SCMD_Py

pip3 install sparkfun-qwiic-scmd

Inside jetbot/jetbot there is a file called robot.py. If you want to keep it, then simply create a new file: robot2.py as the file given by this repo.
Or you can change the content of robot.py. (Note if you create a new file --ex: robot2.py-- you have to add it in the __init__.py, and inside your notebook you have to include as such.)

The code should work after a restart of the jupyter (if the jupyter is auromatically run at the startup, then restart the Jetson). OR in jupyter open a terminal and copy the modified files in '/usr/local/lib/python3.6/dist-packages/jetbot-0.4.3-py3.6.egg/jetbot/'. After you installed qwiic, I recommend to restart your jetson, after if you want to rewrite something in the code, then you can simply copy the modified file inside the given directory.

Initially, the jetbot drivers are written with small values (around 0 and 1), this code requires 0-255 range, so do a little bit of experiment in this files (althought, I have tried to implement an 'if' for this case.)
