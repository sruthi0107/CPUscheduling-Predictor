# CPUscheduling-Predictor
This project explores the application of Machine learning in the field of operating systems. Given the arrival time and burst time of a set of 5 input
processes, the best CPU scheduling algorithm is determined based on the waiting time. The CPU scheduling algorithms that have been used in this project are 
FCFS, SJF, SRTF and Round Robin. Machine learning here was used to train the model to predict the most suitable CPU Scheduling algorithm given the inputs.

### Dataset
Datasets of several sizes ranging from 500 records to 10000 records were created and tested. Random values were generated for each set of process following which all the 
4 CPU scheduling algorithms were applied. The algorithm with the least waiting time was assigned as the label.

### Model
Several ML algorithms were tested to determine the best model along with 2 different scalers- MinMax and Standard scalers. The results have been tabulated in the 
Experiments and Results document.
