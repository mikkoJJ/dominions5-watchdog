from typing import List

from . import data


class Dominions5TurnReport(object):
    """ The turn report object describes the current state of 
    turns in a running Dominions 5 game.
    """
    def __init__(self):
        self.ai_turns: List[str] = []
        """ List of turns by AI 
        """
        
        self.turns_done: List[str] = []
        """ List of nations that have done their turns.
        """
        
        self.turns_pending: List[str] = []
        """ List of nations whose turns are not done.
        """
    
    @classmethod
    def from_log_string(cls, log_string: str) -> 'Dominions5TurnReport':
        """Creates a turn report from a log string. The log
        string is expected to be of the format used by the Dominions 5
        server when it is running and logging the status of turns, ie.
        it looks eg like this::
        
          (Na1) Na2+ Na3- 
          
        Where Na1 is the shorthand of an AI nation, and Na2 and Na3 are
        human nations with a finished and unfinished turn respectively.

        Args:
            log_string (str): dominions 5 server log string

        Raises:
            RuntimeError: if the log string is not of the correct format

        Returns:
            Dominions5TurnReport: turn report object based on the log string
        """
        report = cls()
        
        for item in log_string.split(" "):
            # AI names are in brackets:
            if item[0] == "(":
                report.ai_turns.append(data.get_nation_long_name(item[1:-1]))
            
            # + means turn is done
            elif item[-1] == "+":
                report.turns_done.append(data.get_nation_long_name(item[:-1]))

            # - means turn is pending
            elif item[-1] == "-":
                report.turns_pending.append(data.get_nation_long_name(item[:-1]))

            else:
                raise RuntimeError(f"Got an unknown log item type: {item}")

        return report
