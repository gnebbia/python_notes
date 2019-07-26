# Example 3: asynchronous requests with larger thread pool
import asyncio
import concurrent.futures
import requests

fuzzing_list = [
        '',
        'test',
        'test1',
        'test2',
        '.cgi',
        '.git',
        '.htocs',
        'webroot',
        ]

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(executor, requests.get,
                'https://httpdump.io/nqn5a'.format(i), )
            for i in fuzzing_list
        ]
        for response in await asyncio.gather(*futures):
            print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
