## HDImageRecognition

# Install Keras on Amazon EC2
https://blog.keras.io/running-jupyter-notebooks-on-gpu-on-aws-a-starter-guide.html

# Install Keras on Mac

1. Download anaconda
2. conda create -n keraslearn python=2.7
3. source activate keraslearn
4. conda install numpy pandas jupyter notebook matplotlib scipy
5. conda install mkl nose sphinx pydot-ng
6. conda install theano pygpu
7. pip install keras
8. Go to $HOME/.keras/keras.json
9. change backend to theano
10. python -c "import keras; print keras.__version__"
11. pip install --upgrade keras
12. pip install -U scikit-learn
13. conda install h5py
14. sudo pip install utils


# Data Setup

```
#### Data needs to be loaded in below train, test and valid folders appropriately.

#####

    train/
        faucet/
            trainfaucet001.jpg
            trainfaucet002.jpg
            ...
        flowerpots/
            trainflowerpots001.jpg
            trainflowerpots002.jpg
            ...
        hammer/
            trainhammer001.jpg
            trainhammer002.jpg
            ...
        thermostats/
            trainthermostats001.jpg
            trainthermostats002.jpg
            ...        
    valid/
        faucet/
            validfaucet001.jpg
            validfaucet002.jpg
            ...
        flowerpots/
            validflowerpots001.jpg
            validflowerpots002.jpg
            ...
        hammer/
            validhammer001.jpg
            validhammer002.jpg
            ...
        thermostats/
            validthermostats001.jpg
            validthermostats002.jpg
            ...        
    test/
        faucet/
            testfaucet001.jpg
            testfaucet002.jpg
            ...
        flowerpots/
            testflowerpots001.jpg
            testflowerpots002.jpg
            ...
        hammer/
            testhammer001.jpg
            testhammer002.jpg
            ...
        thermostats/
            testthermostats001.jpg
            testthermostats002.jpg
            ...   
     unknown/
        unknown/
```

# Install Flask
http://flask.pocoo.org/docs/0.12/installation/

# Run Flask Python file
python ImageRecognitionAPI.py
