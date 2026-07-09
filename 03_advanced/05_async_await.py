# =============================================================
# ADVANCED 5: ASYNC / AWAIT
# =============================================================
#
# BIG IDEA:
#   async lets one thread wait on MANY I/O tasks (network, disk)
#   without blocking. Great for APIs, scrapers, chat servers.
#
#   CPU-heavy work still needs threads/processes — async is for
#   waiting, not crunching numbers.
# =============================================================

import asyncio
import time


# --- Step 1: async def + await -------------------------------
async def say_after(delay: float, message: str) -> str:
    await asyncio.sleep(delay)   # non-blocking sleep
    return message


async def demo_basic():
    print(await say_after(0.1, "hello"))
    print(await say_after(0.1, "world"))


asyncio.run(demo_basic())

print("-" * 50)


# --- Step 2: Run tasks concurrently --------------------------
# await one-by-one = sequential. gather = overlapping waits.
async def demo_concurrent():
    start = time.perf_counter()
    results = await asyncio.gather(
        say_after(0.2, "one"),
        say_after(0.2, "two"),
        say_after(0.2, "three"),
    )
    elapsed = time.perf_counter() - start
    print(results)
    print(f"elapsed ≈ {elapsed:.2f}s (not ~0.6s — they overlapped)")


asyncio.run(demo_concurrent())

print("-" * 50)


# --- Step 3: create_task for fire-and-track ------------------
async def demo_tasks():
    t1 = asyncio.create_task(say_after(0.15, "A"))
    t2 = asyncio.create_task(say_after(0.05, "B"))
    # Both already running. Await when you need the result.
    print(await t2)   # B finishes first
    print(await t1)


asyncio.run(demo_tasks())

print("-" * 50)


# --- Step 4: Mental model ------------------------------------
print("""
SYNC vs ASYNC
-------------
def  / time.sleep     -> blocks the whole thread
async def / await asyncio.sleep -> frees the event loop to run others

You can only `await` inside an `async def`.
Entry point: asyncio.run(main())

Libraries: httpx, aiohttp (async HTTP), asyncio streams, etc.
""")


# =============================================================
# TRY IT YOURSELF:
#   1. Write async `fetch_fake(name, delay)` that sleeps then
#      returns f"{name} done".
#   2. Run three of them with asyncio.gather and print results.
# =============================================================


# =============================================================
# ✅ SOLUTION
# =============================================================
print("\n===== SOLUTION (Advanced 5) =====")


async def fetch_fake(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} done"


async def solution():
    results = await asyncio.gather(
        fetch_fake("users", 0.05),
        fetch_fake("posts", 0.05),
        fetch_fake("comments", 0.05),
    )
    print(results)


asyncio.run(solution())
