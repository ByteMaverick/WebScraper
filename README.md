---

#  🎞️ Image Downloader

A lightweight Python library to search and download images from the web effortlessly. Perfect for automation, batch downloads, and data collection projects.

---


## Features
- **🔍 Search and Download**: Collect images from Bing with custom queries.  
- **📂 Batch Processing**: Handle multiple queries in one go.  
- **⚙️ Error Handling**: Skips invalid links and logs errors.  
- **🗂️ Folder Management**: Automatically organizes downloads.  





---

## Installation
Install with pip:
```bash
pip install image_downloader
```

---

## Usage
```python
from image_downloader import ImageDownloader

downloader = ImageDownloader()
downloader.download_images("Chris Evans", "/path/to/save", count=30)
```

---

## Upcoming Features
### Extend Supported Sources
- Add support for Google Images, DuckDuckGo, Instagram, and Pinterest.
- Target specific sites like Unsplash or Flickr.

### Advanced Search Options
- Filters for size, type, color, and license.
- Advanced queries with AND, OR, NOT operators.

### Image Processing
- Resize, convert formats (JPEG/PNG), compress, and deduplicate images.
- Extract EXIF metadata.

### Performance Enhancements
- Multithreading/async for faster downloads.

### Machine Learning Integration
- Image classification, duplicate detection, and facial recognition.

---


