2019/08/12 update

## Highlight
1. Modify published topic to /zed/zed_node/rgb/image_rect_color
2. Modify rate from 10hz to 30hz    # same as 
3. Modify resolution from 2K to 720p.



# ZED
## setup zed rosnode
```
cd /zedcv2/scripts     # modify zedcv2 to YOUR NODE
git clone https://github.com/liu-chien/zedcv2.git
cd ~/catkin_ws
catkin_make
```

## Open zed node
```
rosrun zedcv2 zednode.py
```

## Using ZED with purely opencv
```python
from zedcv2 import Camera

zed = Camera()
    zed.set_resolution("2K")    # "2K", "1080p", "720p", "WVGA"
    zed.set_eye("left")         # "left", "right", "both"

    while(True):
        # Capture frame-by-frame
        frame = zed.retrieve_image()

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

```
