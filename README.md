# yt-bulk-audio-extracter
Download audio files from multiple at once

Install requirements
```bash
pip install -r requirements.txt
```

Provide urls in extracter.py
```python
...
youtube_urls = [
  "https://www.youtube.com/watch?v=VIDEO_ID_1",
  "https://www.youtube.com/watch?v=VIDEO_ID_2",
  # add other yt videos URLs here...
]
...
```
Run extracter
```bash
python3 extracter.py 
```

Once done, you'll find your audio files in output folder