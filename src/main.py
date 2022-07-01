def _sort_tuple(tup):
	return(sorted(tup, key = lambda x: x[1]))

class ChoresList:
    def __init__(self):
        self.chores = []

    def get_list(self):
        if not self.chores:
            return []
        return [chore for chore, priority in _sort_tuple(self.chores)]

    def add_chore(self, chore: str, priority=None, depends_on: str=None):
        if depends_on:
            [priority] = [priority for chore_desc, priority in self.chores if chore_desc == depends_on]
            priority += 1
            new_list = []
            for chore_tup in self.chores:
                if chore_tup[1] >= priority:
                    (chore_text, prio) = chore_tup
                    new_list.append((chore_text, prio + 1))
                else:
                    new_list.append(chore_tup)
            self.chores = new_list
        elif not priority:
            priority = len(self.chores) + 1
        self.chores.append((chore, priority))

    def get_priotity_item(self, chore_priority: int):
        items = [chore for chore, priority in self.chores if priority == chore_priority]
        return items
