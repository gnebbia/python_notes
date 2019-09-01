https://bpaste.net/raw/Js3n
import sys
import asyncio

import tornado.httpclient
import tornado.ioloop


async def main():
    """Read a bunch of URLs from stdin, write those URLs and return code to
       stdout."""

    # Note: if you have too many URLs don't do this
    urls = sys.stdin.read().splitlines()

    client = tornado.httpclient.AsyncHTTPClient(max_clients=1024)

    async def get(client, url):
        request = await client.fetch(url, raise_error=False)
        sys.stdout.write(f"{request.code:>3} {url}")

    await asyncio.gather(*[
        get(client, url) for url in urls
    ])


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
