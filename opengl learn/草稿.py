import dis
import pickle

import pyclipper

def offset():
    pass

def main():
    last_layer=[]
    a=0
    name = 0
    layer_num = 1
    thickness = 1
    path_last_layer = 0
    current_layer=0
    is_up_outer=0
    is_up_inner=0
    offset_up = 0
    isremelt_up=0
    layer = 0
    path_last_layer = 'tmp/%s/%d.clitmp' % (name, (layer_num - 1) * thickness)
    try:
        with open(path_last_layer, 'rb') as f:
            last_layer = pickle.load(f)
        if last_layer['epa']['entity']['outer']:
            last_layer = last_layer['epa']['entity']['outer']
        elif last_layer['epa']['entity']['inners']:
            last_layer = last_layer['epa']['entity']['inners'][0]
        else:
            last_layer = last_layer['epa']['entity']['contour']
    except:
        last_layer=None
    if layer_num ==0:
        last_layer = None
    path_next_layer = 'tmp/%s/%d.clitmp' % (name, (layer_num+1) * thickness)
    try:
        with open(path_next_layer,'rb') as f:
            next_layer = pickle.load(f)
        if next_layer['epa']['entity']['outer']:
            next_layer = next_layer['epa']['entity']['outer']
        elif next_layer['epa']['entity']['inners']:
            next_layer = next_layer['epa']['entity']['inners'][0]
        else:
            next_layer = next_layer['epa']['entity']['contour']

    except:
        next_layer = None
    if current_layer:
        if is_up_outer or is_up_inner:
            init_up_contour = None
            if next_layer:
                clip_up = pyclipper.Pyclipper()
                clip_up.AddPaths(current_layer,pyclipper.PT_SUBJECT,True)
                clip_up.AddPaths(next_layer,pyclipper.PT_CLIP,True)
                tmp = clip_up.Execute(pyclipper.CT_DIFFERENCE,pyclipper.PFT_EVENODD,pyclipper.PFT_EVENODD)
                if tmp:
                    init_up_contour = offset(tmp, offset_up)
                else:
                    init_up_contour = offset(current_layer,offset_up)
            if init_up_contour:
                if isremelt_up or  layer['epa']['entity']['skin'] or layer['epa']['entity']['core'] :
                    if layer['epa']['entity']['skin']:
                        if layer['epa']['entity']['skin']['contour']:
                            clip_up = pyclipper.Pyclipper()
                            clip_up.AddPaths(layer['epa']['entity']['skin']['contour'],pyclipper.PT_SUBJECT,True)
                            clip_up.AddPaths(init_up_contour,pyclipper.PT_CLIP,True)
                            clip_up.Execute(pyclipper.CT_DIFFERENCE,pyclipper.PFT_EVENODD,pyclipper.PFT_EVENODD)





dis.dis(main)