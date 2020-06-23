import scrapy
from ..items import FlipkartItem
import pandas as pd

class SamsungSpider(scrapy.Spider):
    name = 'flipkart'
    start_urls = [
        "https://www.flipkart.com/search?q=samsung+mobiles",
        "https://www.flipkart.com/search?q=mi+mobiles"
         ]

    def parse(self, response):
        items = FlipkartItem()
        print(response)
        AllDiv = response.css("._1UoZlX")
        for samsung in AllDiv:
            title =  samsung.css("._3wU53n::text").extract()
            price = samsung.css("._2rQ-NK::text").extract_first()
            memory = samsung.css(".tVe95H:nth-child(1)::text").extract()
            screen = samsung.css(".tVe95H:nth-child(2)::text").extract()
            camera = samsung.css(".tVe95H:nth-child(3)::text").extract()
            battery = samsung.css(".tVe95H:nth-child(4)::text").extract()
            processor = samsung.css(".tVe95H:nth-child(5)::text").extract()
            warranty = samsung.css(".tVe95H:nth-child(6)::text").extract()


            items['title'] = title
            items['price'] = price
            items['memory'] = memory
            items['screen'] = screen
            items['camera'] = camera
            items['battery'] = battery
            items['processor'] = processor
            items['warranty'] = warranty
            

            yield items

        NextPage = response.css('a._2Xp0TH+ ._3fVaIS::attr(href)').get()

        print('___________________________________________________________',NextPage,'____________________________________________')
        if NextPage is not None:
            yield response.follow(NextPage,callback=self.parse)
        else:
            print('Done')

   
