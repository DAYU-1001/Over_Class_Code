import numpy 
import matplotlib.pyplot
import scipy.special

#neural network class defination
class neuralNetwork:
    #initialise the neural network
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        #set number of nodes in each input,hidden,output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #link weight matrices,wih and who
        #weight inside the arrays are w_i_j,where link is from node i to node j in the next layer
        #w11 w21
        #w12 w22 etc
        self.wih=numpy.random.normal(0.0,pow(self.hnodes,-0.5),(self.hnodes,self.inodes))
        self.who=numpy.random.normal(0.0,pow(self.onodes,-0.5),(self.onodes,self.hnodes))

        #learning rate
        self.lr = learningrate
        
        #acitcation function is the sigmoid function
        self.activation_function=lambda x:scipy.special.expit(x)
        
        pass

    # train the neural netword
    def train(self,inputs_list,targets_list):
        #convert inputs list to 2d array
        inputs=numpy.array(inputs_list,ndmin=2).T
        targets=numpy.array(targets_list,ndmin=2).T

        hidden_inputs=numpy.dot(self.wih,inputs)
        hidden_outputs=self.activation_function(hidden_inputs)

        final_inputs=numpy.dot(self.who,hidden_outputs)
        final_outputs=self.activation_function(final_inputs)

        #error is the (target-actual)
        output_errors=targets-final_outputs

        #hidden layer error is the output_error,split by weights,recombined at hidden nodes
        hidden_errors=numpy.dot(self.who.T,output_errors)

        #update the weights for the links between the hidden and output layers
        self.who+=self.lr*numpy.dot((output_errors*final_outputs*(1.0-final_outputs)),nunpy.transpose(hidden_outputs))

        #update the weights for the links between the inputs and outputs layers
        self.wih+=self.lr*numpy.dot((hidden_errors*hidden_outputs*(1.0-hidden_outputs)),numpy.transpose(inputs))



        pass
    
    #query the neural network
    def query(self,inputs_list):
        #convert inputs list to 2D array
        inputs=numpy.array(inputs_list,ndmin=2).T

        #claculate sigmoid
        hidden_inputs=numpy.dot(self.wih,inputs)
        hidden_outputs=self.activation_function(hidden_inputs)

        final_inputs=numpy.dot(self.who,hidden_outputs)
        final_outputs=self.activation_function(final_inputs)

        return final_outputs