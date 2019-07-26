import asyncio
import re
import concurrent.futures
import requests



async def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop = asyncio.get_event_loop()
        futures = []
        response = []
        for i in range(20):
            # look here for sending more parameters to the loop.runn_in_executor
            # basically we must use functools
            # https://stackoverflow.com/questions/53368203/passing-args-kwargs-to-run-in-executor
            url = 'https://httpdump.io/{}/a/{}'
            url1 = re.sub('{}','placeholder', url)
            futures.append(loop.run_in_executor(executor, requests.get,url1))

        for response in await asyncio.gather(*futures):
            print(response)



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
