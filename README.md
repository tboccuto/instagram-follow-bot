
# instagram-follow-bot
## Have cool stuff to share but no audience? This script works by following a bunch of people on instagram with the hope that they will follow 

## Versions
- Python 3.8.0
## Browser
- Chrome Version 92.0.4515.107 (Official Build) (x86_64)
- Firefox 

## Dependencies
- Usually ChromeDriver Version 92.0.4515.107, but now 'geckodriver 0.29.1'
- Selenium 3.141.0
- Selenium Webdriver

## TODOS
- search_follow_public_only needs to handle three consecutive private accounts successfully and continue. 
- follow_by_scroll needs to be able to load the dialogue box in the dom for longer then 12 elements. Currently it breaks at 12 elements
- Both need to add follow_button.click()
- Add Functionality for check_topic
