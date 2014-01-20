Proectile
=========

Python script to calculate the path of a projectile and output a csv of coordinates.
The base for this file came from daniweb that has many Python scripts available.
I have modified it to provide an input function and write to CSV.
I also need to take out the lambda function so that I can manipulate the variables
a little more easily.
The reason for creating this scipt is to help design a robot launcher for a First Robotics Competition.
The robot has to launch a two feet diameter ball into a goal that is nearly 7 feet off the ground, 11 feet
wide and just over three feet from the bottom of the opening to the top. The program can be used to calculate an 
optimum launch angle and velocity. Optimum means the widest range of distance from the goal the ball can be
launched from and still score.
The greater the distance that the ball stays at a height that allows it to pass through the goal, the more flexibility
the robot has in terms of the range of distances it can be from the goal, fire and still score.
The program was used in this way. First a video was taken of the launch mechanism firing the ball. This video was 
imported into Tracker, a freeware physics program. The path of the center of mass was tracked and exported as X, Y
coordinates to Excel. This could then be graphed and the initial velocity and angle of projection calculated.
This velocity and angle were input to the Pythong scipt and the resulting X and Y coordinates plotted against the 
observed results. This validated that the model closely matched observed results. Then it is possible to use the 
Python script output for guidance in experimentation, rather than doing lots of experiments with different 
launcher setups.
Experimentation with different launch velocities and angle of projection showed that the model could find values 
that launched the ball into the goal from anywhere between 9 and 20 feet from the goal, either on the way up to 
mamxium height, or on the way down. This would have been very time consuming to recreate in the physical world.
Once the ideal launch velocity and angle were determined, the launcher was tuned to generate those values and
the launcher worked as required.
