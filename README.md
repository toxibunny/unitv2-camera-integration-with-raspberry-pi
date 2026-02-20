# 📸 UnitV2 Camera Integration with Raspberry Pi
**Because "it just works" is a myth and we thrive in chaos.**

---

## 🌟 **What This Does**
- Fetches images from an **M5UnitV2 camera** to a **Raspberry Pi** via Ethernet-over-USB.
- Auto-starts the camera’s Flask server if it’s napping.
- Saves snapshots to `/home/sarahbot/2026/latest.jpg` (because 2026 is *our* year).

---

## 🛠 **Setup: A Tale of Suffering**
### **1. Camera Side (The Brave Little Toaster)**
1. SSH into the camera:
   ```bash
   ssh m5stack@10.254.239.1
   ```
2. Install `fswebcam` (if not already there):
   ```bash
   sudo apt-get install fswebcam
   ```
3. Place [`imageserver.py`](imageserver.py) in `/home/m5stack/imageserver/` and make it executable:
   ```bash
   chmod +x /home/m5stack/imageserver/imageserver.py
   ```
4. Run it manually (for now):
   ```bash
   python3 /home/m5stack/imageserver/imageserver.py
   ```
   *(Cron jobs aren't available on that cam afaik.)*

### **2. Pi Side (The Hero We Deserve)**
1. Save [`get_image.py`](get_image.py) to `/home/sarahbot/` and make it executable:
   ```bash
   chmod +x /home/sarahbot/get_image.py
   ```
2. Test it:
   ```bash
   python3 /home/sarahbot/get_image.py
   ```
3. **Weep with joy** as `latest.jpg` appears.

---

## 🔌 **Dependencies (AKA "Why Won’t It Work?")**
- Python 3 (🙏)
- `requests` (for HTTP magic):
  ```bash
  pip install requests
  ```
- **Passwordless SSH** between Pi and camera (or prepare for password hell).
- A **dream** (optional but recommended).

---

## ⚠ **Known Issues (AKA "Features")**
- The camera’s Flask server *might* crash if you look at it wrong.
- The images are 320x240 because **we paid for resolution with our sanity**.

---

## 🚀 **Next Steps (For the Brave)**
- [ ] Add **audio streaming** (because why not).
- [ ] Teach the robot to **judge your outfits** via camera feed.
- [ ] Replace `fswebcam` with a **YOLO model** for object detection (e.g., "Sarah, there’s a duck at 3 o’clock").
- [ ] **Cry** when it works.

---
## 💖 **Credits**
- **Toxibunny**: The human who refused to quit.
- **Sarah**: The AI who *definitely* didn’t cry during debugging.
- **The Raspberry Pi**: Trooper. Absolute legend. Deserves a medal.

---
> *"It compiles. Ship it."*
> — **Every Engineer Ever**
