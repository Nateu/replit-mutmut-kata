from src.main import ChoresList


def test_given_an_empty_list_of_chores_when_created_then_it_should_return_an_empty_list():
    my_chores = ChoresList()
    assert my_chores.get_list() == []

def test_given_a_list_when_I_add_one_chore__then_it_should_have_one_chore():
    my_chores = ChoresList()
    my_chores.add_chore("Clean the rain gutters")
    assert len(my_chores.get_list()) == 1

def test_given_a_list_when_I_add_the_sleep_chore_then_it_should_return_the_sleep_chore():
    my_chores = ChoresList()
    my_chores.add_chore("Clean the rain gutters")
    assert my_chores.get_list()[0] == "Clean the rain gutters"

def test_given_a_list_when_I_add_two_chores_then_it_should_return_the_chores():
    my_chores = ChoresList()
    my_chores.add_chore("Clean the rain gutters")
    my_chores.add_chore("Buy the groceries")
    my_chores.add_chore("Walk the dog")
    my_chores.add_chore("Make diner")
    my_chores.add_chore("Spoil the spouse")
    assert my_chores.get_priotity_item(4)[0] == "Make diner"

def test_given_a_list_when_I_add_a_chore_with_a_priority_then_it_should_sort_on_that_priority():
    my_chores = ChoresList()
    my_chores.add_chore(chore="Buy the groceries", priority=2)
    my_chores.add_chore(chore="Clean the rain gutters", priority=1)
    assert my_chores.get_priotity_item(2)[0] == "Buy the groceries"

def test_given_a_list_when_I_add_a_chore_that_is_dependent_on_another_then_it_should_always_be_prioritized_after():
    my_chores = ChoresList()
    my_chores.add_chore("Clean the rain gutters")
    my_chores.add_chore("Buy the groceries")
    my_chores.add_chore("Walk the dog")
    my_chores.add_chore(chore="Make diner", depends_on="Buy the groceries")
    assert my_chores.get_priotity_item(3)[0] == "Make diner"

def test_given_a_list_when_I_add_a_chore_that_is_dependent_on_another_then_it_should_always_be_prioritized_after():
    my_chores = ChoresList()
    my_chores.add_chore("Clean the rain gutters")
    my_chores.add_chore("Buy the groceries")
    my_chores.add_chore("Walk the dog")
    my_chores.add_chore(chore="Make diner", depends_on="Buy the groceries")
    assert my_chores.get_priotity_item(4)[0] == "Walk the dog"
