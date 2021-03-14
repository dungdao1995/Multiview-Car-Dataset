import pandas as pd
import random
import shutil


#print(df.loc[1])


#Get the path for 4 classes: front, rear, left_side, right_side of the car
def getPath(df):
    front = []
    rear = []
    left_side = []
    right_side = []
    for idx, deg in enumerate(df.loc[1]):
        if (0<=float(deg)<=10) or (350<=float(deg)<=360):
            rear.append(df.loc[0][idx])
        elif 50<=float(deg)<=130:
            left_side.append(df.loc[0][idx])
        elif 170<=float(deg)<=190:
            front.append(df.loc[0][idx])
        elif 230<=float(deg)<=310:
            right_side.append(df.loc[0][idx])
    
    return front, rear, left_side, right_side

#slit the data into training and validation data
def splitData(front, rear, left_side, right_side):
    #Shuffle the link of images
    random.shuffle(front)
    random.shuffle(rear)
    random.shuffle(left_side)
    random.shuffle(right_side)

    ratio_training = 0.8 # training data = 80% data, validation = 20%
    #Training Data
    front_train  = front[:int(ratio_training*len(front))]
    rear_train = rear[:int(ratio_training*len(rear))]
    left_side_train = left_side[:int(ratio_training*len(left_side))]
    right_side_train = right_side[:int(ratio_training*len(right_side))]

    print(front_train[0])
    for i in front_train:
        shutil.copy2(i, 'Data_new_1308/Training/front')

    for i in rear_train:
        shutil.copy2(i, 'Data_new_1308/Training/rear')
    
    for i in left_side_train:
        shutil.copy2(i, 'Data_new_1308/Training/left_side')

    for i in right_side_train:
        shutil.copy2(i, 'Data_new_1308/Training/right_side')

    #Validation data
    front_val  = front[int(ratio_training*len(front)):]
    rear_val = rear[int(ratio_training*len(rear)):]
    left_side_val = left_side[int(ratio_training*len(left_side)):]
    right_side_val = right_side[int(ratio_training*len(right_side)):]

    count = 0
    print(front_val[0])
    for i in front_val:
        shutil.copy2(i, 'Data_new_1308/Validation/front')
        count+=1

    print('Count = {}'.format(count))

    for i in rear_val:
        shutil.copy2(i, 'Data_new_1308/Validation/rear')
    
    for i in left_side_val:
        shutil.copy2(i, 'Data_new_1308/Validation/left_side')

    for i in right_side_val:
        shutil.copy2(i, 'Data_new_1308/Validation/right_side')


if __name__ == '__main__':
    df = pd.read_csv ('epfl_targets.csv', header=None)
    front, rear, left_side, right_side = getPath(df)
    #splitData(front, rear, left_side, right_side)
    print(len(front))
    print(len(rear))
    print(len(left_side))
    print(len(right_side))




