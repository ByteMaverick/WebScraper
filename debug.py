import json

import requests
from bs4 import BeautifulSoup
import os
import shutil
import time


class ImageDownloader:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    def image_links_collector(self, name, count):
        # Define Url and Headers
        search_change = [ name +"headshots", name + " photos",name + " latest", name + " new",name + " premier"]
        img_links = []
        for search_command in search_change:
            search_query = search_command.replace(' ', '+')
            url = f"https://www.bing.com/images/search?q={search_query}&form=HDRSC3"

            # resquest HTML
            response = requests.get(url, headers=self.headers)

            # Parse Html
            Soup = BeautifulSoup(response.text, "html.parser")
            images = Soup.find_all("a", class_="iusc")  # Bing-specific class
            for img in images:
                metadata = img.get("m")  # Extract metadata JSON
                if metadata:
                    full_image_url = json.loads(metadata).get("murl")  # Extract full-resolution URL
                    img_links.append(full_image_url)
            # Check the requirements
            if len(img_links) >= count + 20:
                break

        return img_links[:count]

    def image_downloader(self, name, path_to_save, count=100, ):
        # Setting Timer
        time_started = time.time()

        # Creating folder
        path_to_cr_data = os.path.join(path_to_save, name)
        if os.path.exists(path_to_cr_data):
            shutil.rmtree(path_to_cr_data)
        os.mkdir(path_to_cr_data)

        # Searching and collecting relevant img links into a list 

        print("Searching the web.....")
        img_links = self.image_links_collector(name, count)
        print(f" Collected {len(img_links)} links")
        print("Downloading now...")

        # Downloading Images

        Downloaded_count = 1
        for link in img_links:
            try:
                if not link.startswith("http"):
                    continue
                response = requests.get(link, headers=self.headers)
                if response.status_code == 200:
                    # Create a unique filename for each image
                    file_name = os.path.join(path_to_cr_data, f"{name.replace(' ', '_')}_{Downloaded_count}.jpg")
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    Downloaded_count += 1


                else:
                    print(f"Failed to download image from {link}. Status code: {response.status_code}")


            except Exception as e:
                print(f"Error downloading image from {link}: {e}")

        time_completed = time.time()
        time_elapsed = time_completed - time_started
        print(
            f"Succesfully downloaded {Downloaded_count} images of {name}  at {path_to_cr_data} in {time_elapsed:.2f} seconds")

    def get_JavaScript_file(self, name, keyword=" "):
        search_query = name.replace(' ', '+')
        url = f"https://www.bing.com/images/search?q={search_query}&form=HDRSC3"

        # resquest HTML
        response = requests.get(url, headers=self.headers)

        # Parse Html
        Soup = BeautifulSoup(response.text, "html.parser")
        images = Soup.find_all(keyword)

        return images


if __name__ == "__main__":
    downloader = ImageDownloader()
   # downloader.image_downloader("Chris evans", "/Users/ansari/Desktop/WebScrapping/", count=30)

    heroes = [
        "Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth",
        "Scarlett Johansson", "Jeremy Renner", "Don Cheadle", "Paul Rudd",
        "Brie Larson"
    ]
    # Guardians of the Galaxy
    guardians = [
        "Chris Pratt", "Zoe Saldana", "Dave Bautista", "Karen Gillan",
        "Pom Klementieff", "Bradley Cooper", "Vin Diesel"
    ]
    # Other Key Characters
    key_characters = [
        "Josh Brolin", "Tessa Thompson", "Benedict Cumberbatch", "Tom Holland",
        "Chadwick Boseman", "Evangeline Lilly", "Elizabeth Olsen", "Anthony Mackie",
        "Sebastian Stan", "Tom Hiddleston", "Danai Gurira", "Letitia Wright",
        "Benedict Wong"
    ]

    # Supporting Characters
    supporting_characters = [
         "Cobie Smulders",
        "Samuel L. Jackson", "William Hurt", "Frank Grillo", "Hiroyuki Sanada"
    ]

    # Cameos and Special Appearances
    cameos = [
         "Taika Waititi",
        "Sean Gunn", "Michael Douglas", "Michelle Pfeiffer"
    ]


    print(downloader.get_JavaScript_file("Cobie Smulders", "img"))

   
