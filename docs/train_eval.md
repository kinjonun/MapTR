# Prerequisites

**Please ensure you have prepared the environment and the nuScenes dataset.**

# Train and Test

Train MapTR with 8 GPUs 
```
./tools/dist_train.sh ./projects/configs/maptr/maptr_tiny_r50_24e.py 8
bash ./tools/dist_train.sh ./projects/configs/maptrv2/maptrv2_nusc_r50_24ep.py 1
bash ./tools/dist_train.sh ./projects/configs/maptrv2/maptrv2_av2_3d_r50_6ep.py 1
```

Eval MapTR with 8 GPUs
```
./tools/dist_test_map.sh ./projects/configs/maptr/maptr_tiny_r50_24e.py ./path/to/ckpts.pth 8
bash ./tools/dist_test_map.sh ./projects/configs/maptrv2/maptrv2_nusc_r50_24ep.py ./ckpts/maptrv2_nusc_r50_24e.pth 1
bash ./tools/dist_test_map.sh ./projects/configs/maptrv2/maptrv2_av2_3d_r50_6ep_w_centerline.py ./ckpts/maptrv2_av2_3d_r50_6ep_w_centerline.pth 1
```




# Visualization 

we provide tools for visualization and benchmark under `path/to/MapTR/tools/maptr`