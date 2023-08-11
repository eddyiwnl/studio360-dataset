import os
from PIL import Image, ImageFont, ImageDraw
from matplotlib import font_manager
import numpy as np
import pandas as pd

# path = "C:/Users/edwar/Desktop/Cal Poly/Master's/matryodshka-360/room_0_dataset/out_1/"
path = "/data/eddu/matryodshka-replica360/replicas/room_0/out_z/"
dir_list = os.listdir(path)

dof_df = pd.read_csv("glob/train/room_0/room_0_only_z_sorted.txt", sep=',', header=None)
scene_list = dof_df[0].to_list()
img_list = []
# print(scene_list)
# print(dof_df)
# print(dir_list[0])
for each in scene_list:
    # print('each: ', type(each))
    for i in range(len(dir_list)):
        # print('compareto: ', dir_list[i].split('_')[3])
        if(each == int(dir_list[i].split('_')[2])):
            if(dir_list[i].split('_')[3] == 'pos00.jpeg'):
                img_list.append(path + dir_list[i])

# print(img_list)
# print(dof_df.loc[dof_df[0] == int(img_list[11].split('/')[-1].split('_')[2]), 1])
# print(img_list[11].split('/')[-1].split('_')[2])

font = font_manager.FontProperties(family='sans-serif', weight='bold')
fontFile = font_manager.findfont(font)
def create_collage(width, height, listofimages, collage_num):
    cols = 3
    rows = 3
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(fontFile, 45) 
        text = (p.split('/')[-1].split('_')[2] + '\n' 
                + 'x: ' + str(dof_df.loc[dof_df[0] == int(p.split('/')[-1].split('_')[2]), 1].item()) + '\n'
                + 'y: ' + str(dof_df.loc[dof_df[0] == int(p.split('/')[-1].split('_')[2]), 2].item()) + '\n'
                + 'z: ' + str(dof_df.loc[dof_df[0] == int(p.split('/')[-1].split('_')[2]), 3].item()))
        draw.text((5, 5), text, font = font, align ="left")
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            # print(i, x, y)
            try:
                new_im.paste(ims[i], (x, y))
            except IndexError:
                pass
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.save("glob/train/room_0/only_z/Collage" + collage_num + ".jpg")
for i in range(0, len(img_list), 9):
    collage_scenes = str(i) + '-' + str(i+9)
    create_collage(7680, 4320, img_list[i:i+9], collage_scenes)
# create_collage(1500, 1500, img_list[0:9], '0-8')
