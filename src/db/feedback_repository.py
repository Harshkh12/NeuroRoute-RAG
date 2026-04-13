from motor.motor_asyncio import AsyncIOMotorDatabase

class FeedbackRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["feedback"]

    async def save_feedback(self, data: dict) -> None:
        await self.collection.insert_one(data)

    async def get_feedback_for_query(self, query: str) -> list:
        cursor = self.collection.find({"query": query})
        return await cursor.to_list(length=50)

    async def get_avg_score(self, query: str) -> float:
        docs = await self.get_feedback_for_query(query)
        if not docs:
            return 0.0
        return sum(d["feedback"] for d in docs) / len(docs)
