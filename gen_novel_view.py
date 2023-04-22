import os
import argparse
import glob
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--cfg", required=True, type=str)
parser.add_argument("--type", default="skip", type=str)
parser.add_argument("--view_idxes", default='80', type=str)
args = parser.parse_args()

subject = args.cfg.split('/')[-2]
dataset_path = os.path.join('dataset/wild', subject, 'images')
num_frames = len(glob.glob(os.path.join(dataset_path, '*.png')))
print(num_frames, 'frames being processesed...')

gen_paths = []
for frame_idx in range(num_frames):
    gen_path = os.path.join(f"experiments/human_nerf/wild/{subject}/latest/{args.type}_{frame_idx + 1}")
    if os.path.exists(gen_path):
        continue
    else:
        os.system(f"python run.py --type {args.type} --cfg {args.cfg} freeview.frame_idx {frame_idx + 1}")
    gen_paths.append(gen_path)

view_idxes = list(map(args.view_idxes.split('-'), int))
for view_idx in range(view_idxes[0], view_idxes[1]):
    aggr_dir = f"experiments/human_nerf/wild/{subject}/latest/{args.type}_aggr_{view_idx}"
    os.makedirs(aggr_dir, exist_ok=True)
    shutil.copy(
        os.path.join(f"experiments/human_nerf/wild/{subject}/latest/{args.type}_{frame_idx + 1}", "%06d.png" % frame_idx),
        aggr_dir
    )

