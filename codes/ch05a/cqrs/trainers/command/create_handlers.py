from cqrs.commands import ProfileTrainerCommand
from cqrs.handlers import ICommandHandler
from repository.gino.trainers import TrainerRepository


class AddTrainerCommandHandler(ICommandHandler):

    def __init__(self):
        self.repo: TrainerRepository = TrainerRepository()

    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = await self.repo.insert_trainer(command.details)
        return result
