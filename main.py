from allora_sdk.v2.api_client import (
    AlloraAPIClient,
    ChainSlug,
    PriceInferenceToken,
    PriceInferenceTimeframe,
    AlloraTopic,
    AlloraInference,
)
import asyncio

async def main():
    client = AlloraAPIClient(chain_slug=ChainSlug.TESTNET,)

    tokens = await client.get_price_inference(PriceInferenceToken.BTC, PriceInferenceTimeframe.EIGHT_HOURS)

    print(tokens)

if __name__ == "__main__":
    asyncio.run(main())