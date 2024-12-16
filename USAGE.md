<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from atoma_sdk import AtomaSDK

with AtomaSDK() as atoma_sdk:

    res = atoma_sdk.health.health()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from atoma_sdk import AtomaSDK

async def main():
    async with AtomaSDK() as atoma_sdk:

        res = await atoma_sdk.health.health_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->