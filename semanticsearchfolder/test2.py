import asyncio
import nest_asyncio
nest_asyncio.apply()
from pyppeteer import launch

async def run():
    browser = await launch({'args': ['--no-sandbox', '--disable-setuid-sandbox'], 'executablePath': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'})
    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.waitForSelector('.gLFyf')
    searchbar = await page.querySelector(".gLFyf")
    await searchbar.type("Kan polisen bestämma att demonstrationen äger rum någon annanstans i Sverige?")
    await page.keyboard.press('Enter')
    # Wait for the search results to load
    await page.waitForNavigation()
    # Extracting URLs from the search results
    urls = await page.evaluate('''() => {
        const results = document.querySelectorAll('.g');
        const urls = [];
        for (let i = 0; i < Math.min(results.length, 5); i++) {
            const link = results[i].querySelector('a');
            if (link) {
                urls.push(link.href);
            }
        }
        return urls;
    }''')
    # Display the top five URLs in the terminal
    print("Top five URLs:")
    for url in urls:
        print(url)
    # Here, we'll just leave the browser open until manually closed
    while True:
        await asyncio.sleep(60) # Keep the event loop running

asyncio.run(run())
