import logging
import redis.asyncio as aioredis
from redis.exceptions import RedisError

from src.config import config

logger = logging.getLogger(__name__)

JTI_EXPIRY = 120

token_blocklist = aioredis.from_url(
    config.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
)


async def add_jti_to_blocklist(jti: str) -> bool:
    try:
        await token_blocklist.set(
            name=jti,
            value="blocked",
            ex=JTI_EXPIRY,
        )
        return True

    except RedisError as exc:
        logger.warning(
            "Redis error while adding JTI to blocklist. Token NOT blocked.",
            exc_info=exc,
        )
        return False


async def token_in_blocklist(jti: str) -> bool:
    try:
        return await token_blocklist.exists(jti) == 1

    except RedisError as exc:
        logger.warning(
            "Redis error while checking JTI blocklist. Assuming token is NOT blocked.",
            exc_info=exc,
        )
        return False

