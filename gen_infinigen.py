import os
import glob
from html4vision import Col, imagetable

path_to_results = 'static/infinigen_output'
complete_path_list = glob.glob(f'./{path_to_results}/*')
path_list = []
for path in complete_path_list:
    pre_path = os.path.join(f'./{path_to_results}', os.path.basename(path))
    path_list.append(pre_path)

#print(path_list)

gt_dict = {'Image': [],'AO': [], 'DiffCol': [], 'DiffDir': [], 'DiffInd': [], 'Emit': [], 'Env': [],
           'GlossCol': [], 'GlossDir': [], 'GlossInd': [],  'TransCol': [],
           'TransDir': [], 'TransInd': [], 'VolumeDir': []}

for key, value in gt_dict.items():
    for path in path_list:
        specific_path = os.path.join(path, 'frames', key, 'camera_0' ,f'{key}_0_0_0048_0.png')
        gt_dict[key].append(specific_path)

#print(gt_dict)

cols = [
    Col('id1', 'ID'),
]

for key, value in gt_dict.items():
    cols.append(Col('img', key, value))

imagetable(cols=cols, sticky_header=True, overlay_toggle=True,
           out_file='infinigen.html',
           imsize=1,
           imscale=0.5,
           style='''img {border: 1px solid black;-webkit-box-shadow: 2px 2px 1px #ccc; box-shadow: 2px 2px 1px #ccc;}
                    thead {background-color: #EEEEEE; border: 1px solid black;-webkit-box-shadow: 2px 2px 1px #ccc; box-shadow: 2px 2px 1px #ccc;}'''
)