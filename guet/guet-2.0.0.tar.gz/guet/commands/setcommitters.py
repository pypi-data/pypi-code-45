from guet.commands.command import Command
from guet.config.committer import filter_committers_with_initials, Committer
from guet.config.get_committers import get_committers
from guet.config.set_author import set_committer_as_author
from guet.config.set_current_committers import set_current_committers as set_committers


class SetCommittersCommand(Command):

    def execute_hook(self) -> None:
        committers = get_committers()
        committer_initials = self.args
        committers_to_set = filter_committers_with_initials(committers, committer_initials)

        correct_number_of_committers_present = len(committers_to_set) is len(committer_initials)

        if not correct_number_of_committers_present:
            for initials in committer_initials:
                committer_with_initial_present = False
                for committer in committers:
                    if committer.initials == initials:
                        committer_with_initial_present = True
                if not committer_with_initial_present:
                    print(f"No committer exists with initials '{initials}'")
        else:
            set_committer_as_author(committers_to_set[0])
            set_committers(committers_to_set)

    def help(self):
        pass

    @classmethod
    def help_short(cls) -> str:
        return 'Set the current committers'
