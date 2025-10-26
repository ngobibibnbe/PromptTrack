# **PromptTrack**
<p align="center">
  <a href="https://colab.research.google.com/github/ngobibibnbe/PromptTrack/blob/master/test/PromptTrack_Demo.ipynb" target="_blank">
    <img src="https://img.shields.io/badge/Open%20in%20Colab-FFD43B?style=for-the-badge&logo=googlecolab&logoColor=black" alt="Open In Colab"/>
  </a>
</p>

## 📄 **Overview**
**PromptTracker** is a powerful object tracking tool that enables the detection and tracking of objects in videos using **text-based  prompts**. It supports advanced object detection models such as **MDETR** and **OWL-VITV2**, providing robust tracking with options to handle **fixed populations** in enclosed environments. visit our official python librarie here: https://pypi.org/project/PromptTrack

---

## 📥 **Installation**

To install PromptTracker, use the following command:

```python
pip install PromptTrack
pip install --no-deps bytetracker
```




The package has been implemented for python from 3.9 to earlier (last version currently 3.12)
You can check our [github repo](https://github.com/ngobibibnbe/PromptTrack)


## Usage

### Step 1 initialization
```python
from PromptTrack import PromptTracker
#initialize PromptTrack
tracker = PromptTracker()
```

### Step 2: Object Detection

Detect objects in a video using a text prompt:

### Parameters:
- **video_file (str)**: Path to the MP4 input video file.
- **prompt (str)**: Comma-separated names of entities to track (e.g., "pig,bird").
- **nms_threshold (float)**: Non-Maximum Suppression threshold for filtering overlapping detections.
- **detection_threshold (float)**: Confidence threshold for reporting detections.
- **detector (str)**: Detection model to use ("MDETR" or "OWL-VITV2").

```python
tracker.detect_objects(video_file, prompt="penguin",nms_threshold=0.8, detection_threshold=0.3 ,detector="OWL-VITV2")
```


### Step 3: Tracking Objects

Process the video using a Multiple Object Tracker (MOT):

### Parameters:
- **video_file (str)**: Path to the input video file.
- **fixed_parc (bool, default=True)**: Set to True if the number of tracked objects remains constant.
- **track_thresh (float, default=0.40)**: Detection confidence threshold for the tracker.
- **match_thresh (float, default=1.0)**: Matching threshold between new detections and existing tracks (1 to match all, 0 to match none).
- **frame_rate (int, default=6)**: Frame rate of the video.
- **max_time_lost (float, default=inf)**: Maximum time an object can be missing before being removed.
- **nbr_frames_fixing (int, default=300)**: Number of frames considered for tracking in a fixed setting.


```python
tracker.process_mot (video_file, fixed_parc=True,track_thresh=0.40, match_thresh=0.8, frame_rate=25,max_time_lost=float('inf'),nbr_frames_fixing=800)
```


### Step 4: Read Processed Video

To visualize the tracked objects in the processed video:

### Parameters:
- **video_file (str)**: Path to the input video file.
- **fps (int, default=20)**: Frames per second for video playback.

```python
tracker.read_video_with_mot(video_file,fps=20)
```
## Full example usage 

```python
from PromptTrack import PromptTracker
tracker = PromptTracker()

video_file = "[path_to_your_video]"
tracker.detect_objects(video_file, prompt="penguin", nms_threshold=0.8, detection_threshold=0.3, detector="OWL-VITV2")

tracker.process_mot(video_file, fixed_parc=True, track_thresh=0.40, match_thresh=1, frame_rate=25, max_time_lost=float('inf'), nbr_frames_fixing=800)

tracker.read_video_with_mot(video_file, fps=20)
```

## Examples (on our github)

<p align="center">
  <img src="images/pig_1.gif" width="45%" />
  <img src="images/pig_2.gif" width="45%" />
</p>

<p align="center">
  <img src="images/rabbit.gif"  height="200px" width="29%" />
  <img src="images/penguin.gif"  height="200px" width="29%" />
    <img src="images/zebbra.gif"  height="200px" width="29%" />

</p>




## 📄 **Updates**
- Promptrack Python Library available https://pypi.org/project/PromptTrack/   (December 2023)
- Added OWL-VIT V2 as detector   (December 2024)

