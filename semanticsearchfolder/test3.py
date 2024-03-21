import asyncio
import nest_asyncio
nest_asyncio.apply()

from pyppeteer import launch
import json

async def fetch_data_from_google():
    browser = await launch({'args': ['--no-sandbox', '--disable-setuid-sandbox'], 'executablePath': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'})
    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.waitForSelector('.gLFyf')
    searchbar = await page.querySelector(".gLFyf")
    await searchbar.type("vad är polisens öppettider i växjö?" + "i Sverige ?")
    await page.keyboard.press('Enter')
    # Wait for the search results to load
    await page.waitForNavigation()
    # Extracting URLs from the search results
    urls = await page.evaluate('''() => {
        const results = document.querySelectorAll('.g');
        const urls = [];
        for (let i = 0; i < Math.min(results.length, 7); i++) {
            const link = results[i].querySelector('a');
            if (link)
 {
                let url = link.href.split("#")[0]; // Remove anything after #
                urls.push(url);
            }
        }
        return urls;
    }''')
    # Do not close the browser here
    return browser, urls

async def find_matching_entry(browser, urls):
    with open(r'C:\Users\NItro\Desktop\Tulips_Projects\prv\prv\Removing_Repeat_Content\combine.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    matching_entries = []
    for entry in data:
        if entry['url'] in urls:
            matching_entries.append(entry)
    return matching_entries

async def main():
    browser, urls = await fetch_data_from_google()
    matching_entries = await find_matching_entry(browser, urls)
    for entry in matching_entries:
        print("Title:", entry["title"])
        print("URL:", entry["url"])
        print("Date:", entry["date"])
        print("Content:", entry["content"])
        print()
    # You can close the browser after you're done with your tasks
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())