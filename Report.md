# Final Project RL  (Pong Game via Q-Learning)
Younes Shafiee 40108194

This project contains Two parts. in every folder you can find them. 
This project implements Pong game via Q-learning(off-plicy).

### Need to mention game enviroment was implemented in continiuos space. 


## To run 
You can open the main.py file to see which arguments are availabe to pass and config. but better to run it with default values. Because there are some parameters(like ball size) that conflict the behavior of collisions. 

So run the below scrip in terminal to see the game.

cmd: python main.py --load --filename {train file name, ex:50kepisode}
run this: $ python main.py --load --filename 50Kepisode.pkl


## to train again
You need to omit --load argument in the above cmd and pass a new name for the train file result. Default arguments are enough.


### Q1
Q values are stored in Q dic and we can have them by just running the final_show(self, Q) function once again and add a print line of code in there. Better way is to install an extension of VSCode (ext install Percy.vscode-pydata-viewer) and click on the file.pkl to see the "action-state" values.

# Q2
Reward are just a three mode based. if agent succeed on passing the ball from opponent, get +1 reward; if agent couldnt respond the opponent responses and recieved a goal, gets -1 penalty; and 0 reward for ending the episode without a winner.
states are made by three things for first part(without moving blocks): paddle position in y-axis and ball condition in cartesian Coordinates (x,y). for second part(with moving blocks) we add the position of moving blocks in x-axis to our states.
Actions are just adding an amount of distance in appropriate direction (along the up or down) to agent position.
Choosing the actions are made by Q-learning algorithm. It picks the actions (UP, DOWN) by an Epsilon-greedy manner.





### Thank to Owner of this Repo: https://github.com/alexandru-dinu/pong-qlearning.git
