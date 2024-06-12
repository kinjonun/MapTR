import mmcv


ann_file = "/home/sun/MapTR/data/nuscenes/nuscenes_map_infos_temporal_val.pkl"

data = mmcv.load(ann_file, file_format='pkl')
# data_infos = list(data)
print(data[0][0])