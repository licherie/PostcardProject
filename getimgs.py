import requests
def load_requests(source_url, sink_path):
  #  source_url : "https://i.ebayimg.com/00/s/NzY1WDExNzE=/z/CaYAAOSwGN5dGjNe/$_57.JPG?set_id=8800005007',%20'https://i.ebayimg.com/00/s/MTIwMFgxNjAw/z/NpwAAOSws8RdGPOd/$_57.JPG?set_id=8800005007"
   # sink_path : "C://apache//htdocs//PostcardProject//postcardImages"
    import requests
    r = requests.get(source_url, stream=True)
    if r.status_code == 200:
        with open(sink_path, 'wb') as f:
            for chunk in r:
                f.write(chunk)

# my_img_data = pandas.read_csv("C://apache//htdocs//PostcardProject//myImgLinks.csv")
# frontImgs = my_img_data.frontImg.tolist()
# backImgs = my_img_data.backImg.tolist()
#
# for index, imgUrl in enumerate(frontImgs):
#     sink_path = "C://Users//SEAB//Desktop//" + "postcard" + str(index) + "front"
#     load_requests(imgUrl, )
