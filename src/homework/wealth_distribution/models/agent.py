import random
import uuid
from typing import Dict, Optional, Any, Union


class Agent:

    def __init__(self, money: float, agent_id: Optional[str] = None):
        if not agent_id:
            agent_id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.money = money

    def win(self, amount: int = 1):
        self.money = self.money + amount
        pass

    def lose(self, amount: int = 1):
        self.money = self.money - amount
        pass

    def trade(self, other: 'Agent', amount: int = 1):
        r = random.random()
        if r > 0.5 and other.money >= amount:
            self.money = self.money + amount
            other.money = other.money - amount

        if r <= 0.5 and self.money >= amount:
            self.money = self.money - amount
            other.money = other.money + amount
        pass

    def to_dict(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "money": self.money
        }
