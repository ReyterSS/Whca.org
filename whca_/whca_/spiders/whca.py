import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class WhcaSpider(CrawlSpider):
    name = "whca"
    allowed_domains = ["www.whca.org"]
    start_urls = ["https://www.whca.org/facility-finder/"]
    rules = [
        Rule(LinkExtractor(restrict_xpaths='//li[@class="ill_directory_is_member"]/a[@href]'), callback='parse')
    ]

    def parse(self, response):
        facilities = {
            'Facility_name' : response.xpath('//div[@class="full_width ill_directory_is_member"]/h1//text()').get(),
            'Person_running_it': response.xpath('//p[@class="ill_directory_item_contact_info"]/b//text()').get(),
            'Job_title': response.xpath('//p[@class="ill_directory_item_contact_info"]/b//following-sibling::text()').get(),
            'Phone':  response.xpath('//span[@class="ill_directory_phone"]//text()').get(),
            # email =
            'Url': response.xpath('//a[@class="ill_directory_web_url"]/@href').get(),
            'Facility_type': response.xpath('//div[@class="ill_directory_category_facility-type"]//li//text()').get(),
            'Number_of_bads': response.xpath('//p[@class="licensedbeds"]//b//following-sibling::text()').get()
        }
        yield facilities
