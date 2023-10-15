
# Version 

2.11.0


# 1. create project

```
scrapy startproject scrappy_tutorial_2023
```

# 2. first spider 

Create spider 

```
scrapy genspider quote quotes.toscrape.com
```

Start spider, the spiders is placed at spiders/quote.py

```
scrapy crawl quote
```

This spider manually save file to crawl_data. 
But this is not we do with scrapy.

We do not manually save file. Let scrapy handle the output. 

# 3. Spider - yield json

```
scrapy genspider quote2 quotes.toscrape.com
```

The spiders is placed at spiders/quote2.py

Let's run the spider 

```
scrapy crawl quote2
```

Now, store it 
```
scrapy crawl quote2 -O quotes.json
```

About xpath, // is matching whole page, without // is from the current context (ex: `context.xpath("span/small[@class="author"]/text()")` ). 