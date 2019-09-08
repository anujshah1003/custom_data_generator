

class Config():
    def __init__(self):
        pass
    
    num_classes=5
    labels_to_class = {0:'daisy',1:'dandelion',2:'rose',3:'sunflower',4:'tulip'}
    class_to_labels = {'daisy':0,'dandelion':1,'rose':2,'sunflower':3,'tulip':4}
    resize = 224	
    num_epochs =10
    batch_size =10


