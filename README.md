# ZED
## setup zed rosnode
```
cd ~/catkin_ws/src
catkin_create_pkg zedcv2
cd zedcv2
mkdir scripts
cd scripts
git clone https://github.com/liu-chien/zedcv2.git
cd ~/catkin_ws
catkin_make zedcv2
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
