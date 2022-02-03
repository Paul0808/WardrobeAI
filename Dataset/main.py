import numpy as np
import shutil, os
import pandas

working_directory = os.getcwd()

dataset = pandas.read_csv(os.path.join(working_directory,'input/myntradataset/styles.csv'), error_bad_lines=False)


dataset_filtered = dataset[dataset.masterCategory.isin(['Apparel', 'Footwear']) &
                           ~dataset.subCategory.isin(['Innerwear', 'Loungewear and Nightwear',
                                                      'Socks'])]

print(dataset_filtered)

value_counts = dataset_filtered['subCategory'].value_counts()

indexes = value_counts.index

values = value_counts.values

types_used = indexes[:]
print('Types used: ', types_used)

dataset_invalid = []

dataset_tops = dataset_filtered[dataset_filtered['subCategory'] == 'Topwear']

for img_id in dataset_tops.id:
    try:
        shutil.copy(working_directory + '/input/myntradataset/images/' + str(img_id) + '.jpg',
                    working_directory + '/output/tops/' + str(img_id) + '.jpg')
    except:
        dataset_invalid.append(str(img_id))

dataset_bottoms = dataset_filtered[dataset_filtered['subCategory'] == 'Bottomwear']

for img_id in dataset_bottoms.id:
    try:
        shutil.copy(working_directory + '/input/myntradataset/images/' + str(img_id) + '.jpg',
                    working_directory + '/output/bottoms/' + str(img_id) + '.jpg')
    except:
        dataset_invalid.append(str(img_id))

dataset_shoes = dataset_filtered[dataset_filtered.subCategory.isin(['Shoes', 'Sandal', 'Flip Flops'])]

for img_id in dataset_shoes.id:
    try:
        shutil.copy(working_directory + '/input/myntradataset/images/' + str(img_id) + '.jpg',
                    working_directory + '/output/shoes/' + str(img_id) + '.jpg')
    except:
        dataset_invalid.append(str(img_id))

dataset_dress = dataset_filtered[dataset_filtered.subCategory.isin(['Dress', 'Saree'])]

for img_id in dataset_dress.id:
    try:
        shutil.copy(working_directory + '/input/myntradataset/images/' + str(img_id) + '.jpg',
                    working_directory + '/output/dress/' + str(img_id) + '.jpg')
    except:
        dataset_invalid.append(str(img_id))

dataset_complete = dataset_filtered[dataset_filtered['subCategory'] == 'Apparel Set']

for img_id in dataset_complete.id:
    try:
        shutil.copy(working_directory + '/input/myntradataset/images/' + str(img_id) + '.jpg',
                    working_directory + '/output/complete/' + str(img_id) + '.jpg')
    except:
        dataset_invalid.append(str(img_id))

print(dataset_invalid)