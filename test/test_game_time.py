import pytest
from grfc import scheduler as sc, game_time as gt, GRFC_FILE


@pytest.mark.wip
def test_overall_time_offs():
    data = [sc.time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 19)]
    stats = gt.data_stats(*gt.valid_data(data))
    assert len(stats) == 4 and len(stats.columns) == 10
    assert 'turns as goalie' in stats.index
    assert dict(stats.loc[:, 'Nicholas']) == {'matches played': 5.0, 'average time played': 33.4, 'total time played': 167.0, 'turns as goalie': 1.0}
