import asyncio
from pyppeteer import launch

async def run():
    browser = await launch(
        {'args': ['--no-sandbox', '--disable-setuid-sandbox'],
         'headless': False,  # Set this to True if you don't want to see the browser window
         'executablePath': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'  # Replace with the actual path to your Chrome executable
        }
    )
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
            if (link)
 {
                urls.push(link.href);
            }
        }
        return urls;
    }''')

    # Display the top five URLs in the terminal
    print("Top five URLs:")
    for url in urls:
        print(url)

    # Keep the browser open until manually closed
    while True:
        await asyncio.sleep(60)

    await browser.close()

asyncio.get_event_loop().run_until_complete(run())