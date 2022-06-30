from src.main import ChoresList


def test_given_an_empty_list_of_chores_when_created_it_should_return_an_empty_list():
    my_chores = ChoresList()
    assert my_chores.get_list() == []
