import asyncio
from xbox_controller_async import XBoxControllerReaderAsync
from xbox_controller_sync import XBoxControllerReaderSync
import asyncio
import time

async def test_async_reader(duration=5):
    print("=== Async Reading Starting... ===")
    reader = XBoxControllerReaderAsync()
    await reader.start()

    start = time.time()
    try:
        while time.time() - start < duration:
            print("Async - Buttons:", reader.get_button_states())
            print("Async - Axes:   ", reader.get_axis_states())
            print("Async - Hats:   ", reader.get_hat_states())
            print("-" * 40)
            await asyncio.sleep(0.1)
    finally:
        await reader.stop()
    print("=== Async Read Done.===\n")


def test_sync_reader(duration=5):
    print("=== Sync Reading Starting... ===")
    reader = XBoxControllerReaderSync()
    reader.start()

    start = time.time()
    try:
        while time.time() - start < duration:
            print("Sync - Buttons:", reader.get_button_states())
            print("Sync - Axes:   ", reader.get_axis_states())
            print("Sync - Hats:   ", reader.get_hat_states())
            print("-" * 40)
            time.sleep(0.1)
    finally:
        reader.stop()
    print("=== Sync Read Done. ===")


async def main():
    await test_async_reader(duration=5)
    await asyncio.sleep(1)
    test_sync_reader(duration=5)


if __name__ == "__main__":
    asyncio.run(main())
