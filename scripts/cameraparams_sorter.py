import numpy as np
import pandas as pd
import os, errno

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

# dof_df = pd.read_csv("glob/train/room_0_6dof.txt", sep=' ', header=None)
dof_df = pd.read_csv("glob/train/room_0/room_0_only_x.txt", sep=' ', header=None)

# cwd = os.getcwd()
rename_dict = {
    0: 'camera_pos_x',
    1: 'camera_pos_y',
    2: 'camera_pos_z',
    3: 'ods_baseline',
    4: 'target1_offset_x', 
    5: 'target1_offset_y',
    6: 'target1_offset_z',
    7: 'target2_offset_x', 
    8: 'target2_offset_y',
    9: 'target2_offset_z',
    10: 'target3_offset_x', 
    11: 'target3_offset_y',
    12: 'target3_offset_z',
}
df = dof_df.rename(columns=rename_dict).reset_index().rename({'index': 'scene'}, axis=1)

print(df)

sorted_camera_pos_x = df.sort_values(by='camera_pos_x', ascending=True)
sorted_camera_pos_y = df.sort_values(by='camera_pos_y', ascending=True)
sorted_camera_pos_z = df.sort_values(by='camera_pos_z', ascending=True)

silentremove("glob/train/room_0/room_0_only_x_sorted.txt")
silentremove("glob/train/room_0/room_0_only_y_sorted.txt")
silentremove("glob/train/room_0/room_0_only_z_sorted.txt")


sorted_camera_pos_x.to_csv("glob/train/room_0/room_0_only_x_sorted.txt", header=None, index=None, sep=',')
# sorted_camera_pos_y.to_csv("glob/train/room_0/room_0_only_y_sorted.txt", header=None, index=None, sep=',')
# sorted_camera_pos_z.to_csv("glob/train/room_0/room_0_only_z_sorted.txt", header=None, index=None, sep=',')
