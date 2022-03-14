import scrapy
import json


class TaskSpiderSpider(scrapy.Spider):
    name = 'task_spider'
    allowed_domains = ['www.booking.com']
    start_urls = [
        'https://www.booking.com/hotel/de/adlon-kempinski-berlin.en-gb.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaOQBiAEBmAEJuAEZyAEM2AED6AEBiAIBqAIDuAKjx7mRBsACAdICJDUxNDcyYjc4LWJlNTItNDIzYy05YmYzLWE2YzljZTI4NTUzNNgCBOACAQ;sid=71b9a344a2902c93eb6accfd79806249;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647207343;srpvid=661c97d610bf000a;type=total;ucfs=1&#hotelTmpl']

    # start_urls = ['https://www.booking.com/hotel/ba/zigana-apartmani.en-gb.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaOQBiAEBmAEJuAEZyAEM2AED6AEBiAIBqAIDuALW2rmRBsACAdICJDA3MDRjOGUwLTdkMWUtNDkxOS1iNWJhLTk5YzI0YzkxZDgzN9gCBOACAQ;sid=71b9a344a2902c93eb6accfd79806249;dist=0;group_adults=2;group_children=0;hapos=1;hpos=1;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1647209825;srpvid=ff4c9caf0fe6014b;type=total;ucfs=1&#hotelTmpl']

    def parse(self, response):
        # Hotel Name
        hotel_name_xpath = "//h2[@class='hp__hotel-name']/text()"
        hotel_name = response.xpath(hotel_name_xpath).getall()

        # Adress
        address_xpath = "//p[@class='address address_clean']/span/text()"
        address = response.xpath(address_xpath).getall()

        # Classification
        classification_xpath = "//*[@id='wrap-hotelpage-top']/div[2]/span/span[1]/div/div/span/div/span/span"
        classification = response.xpath(classification_xpath).getall()

        # review points
        score_xpath = '//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div/div/text()'
        score = response.xpath(score_xpath).get()
        score_text_xpath = '//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div/div[2]/div[1]/text()'
        score_text = response.xpath(score_text_xpath).get()

        # number of reviews
        review_number_xpath = "//*[@id='js--hp-gallery-scorecard']/a/div/div/div/div/div[2]/div[2]/text()"
        review_number = response.xpath(review_number_xpath).get()

        # Description
        decscription_xpath = "//div[@id='property_description_content']/*/text()"
        decscriptions = response.xpath(decscription_xpath).getall()

        # Room categories
        rooms_xpath = "//table[@id='maxotel_rooms']/tbody/tr[not(@class) or @class='odd']"
        rooms = response.xpath(rooms_xpath)
        room_descriptions = []
        for room in rooms:
            room_descriptions.append("".join(room.xpath(".//td[2]//a/text()").getall()).replace('\n', ''))

        # Alternative hotels
        # There is no alternative hotels section in the recent one

        yield {
            'Hotel Name': "".join(hotel_name).replace('\n', ''),
            'Address': "".join(address).replace('\n', ''),
            'Classification': len(classification),
            'Review Points ': score_text + " : " + score,
            'Number of reviews': review_number,
            'Description': ''.join(decscriptions).replace('\n', ''),
            'Rooms': room_descriptions
        }
        pass
