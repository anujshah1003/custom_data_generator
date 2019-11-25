class Config():
    def __init__(self):
        pass
    
    num_classes=3
    labels_to_class = {0:'Archery',1:'Basketball',2:'Biking'}
    class_to_labels = {'Archery':0,'Basketball':1,'Biking':2}
    resize = 224	
    num_epochs =10
    batch_size =10


