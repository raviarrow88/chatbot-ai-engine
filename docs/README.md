# HOW IT WORKS




Testing is being done in `sandbox/` folder. 
```
cd sandbox/gromacs/
scrapy crawl gromacs
```
Note: `https://doc.scrapy.org/en/0.24/intro/tutorial.html` to get started




STAGE 1. Get all the actual content. Remove
    1 get content inside <body></body> tags
    2 remove `<style></style>` tags
    3 remove `<script></script>` tags
    4 remove navbar
    5 remove footer
    6 remove sidebar




STAGE 2. Follow the child URLs of the reference link. (this is done, only when an check button is checked.
    # and do above for all pages

STAGE 3: saving the individual pages into db in prefixed structure. Sometimes, there might be a miss in the 
structure, depending on the complexity of the website or tool. But its good to maintain the consistency 
through out!
    

## References:
https://doc.scrapy.org/en/latest/topics/selectors.html
