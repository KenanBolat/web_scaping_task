# WEB SCRAPING TASK  
```by KENAN BOLAT```

## TO TEST Please the following steps 
- Following command will install python3 libraries and prepare the necessary environment    
  - ```` python3 -m pip install -r requirements.txt````
- A demo output can be seen within the ```tiral.json``` document 
- To test your instance just run : 
  - ``` scrapy crawl task_spider -o trial.json```
  - This will automatically look for the latest updates in the web page
- Main code block lies within the following ```.py``` document 
  - ```./task/task/spiders/task_spider.py```
  - In order to test other hotels you can change the ```start_url``` parameter at the line : ```8```  