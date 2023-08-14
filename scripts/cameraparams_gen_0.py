import numpy as np
import pandas as pd
import os, errno

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

dof_df = pd.read_csv("glob/train/room_0_6dof.txt", sep=' ', header=None)
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
df = dof_df.rename(columns=rename_dict)
dfx = df.copy()
dfy = df.copy()
dfz = df.copy()

dfx['camera_pos_y'] = [0] * len(df.index)
dfx['camera_pos_z'] = [0] * len(df.index)
new_x = np.arange(-0.7204797863960266, 6.543098449707031, 0.01325470481)
dfx['camera_pos_x'] = new_x[0:548]

# print(len(new_x[0:548]))

dfy['camera_pos_x'] = [0] * len(df.index)
dfy['camera_pos_z'] = [0] * len(df.index)
new_y = np.arange(-0.9944400787353516, 3.21042275428772, 0.00767310735)
dfy['camera_pos_y'] = new_y[0:548]

dfz['camera_pos_x'] = [0] * len(df.index)
dfz['camera_pos_y'] = [0] * len(df.index)

silentremove("glob/train/room_0/room_0_only_x.txt")
silentremove("glob/train/room_0/room_0_only_y.txt")
silentremove("glob/train/room_0/room_0_only_z.txt")

dfx.to_csv("glob/train/room_0/room_0_only_x.txt", header=None, index=None, sep=' ')
dfy.to_csv("glob/train/room_0/room_0_only_y.txt", header=None, index=None, sep=' ')
dfz.to_csv("glob/train/room_0/room_0_only_z.txt", header=None, index=None, sep=' ')


# print(df)
