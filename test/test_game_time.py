import pytest
import pandas as pd
from grfc import scheduler as sc
from . import GRFC_FILE, ROUND


def valid_data(data):
    return pd.DataFrame(list(filter(lambda dt: dt is not None, data)))


def rename_stats(stats):
    count = stats.loc['count']
    count.name = 'matches played'
    mean = stats.loc['mean']
    mean.name = 'average time played'
    return pd.DataFrame([count, mean])


def data_stats(data):
    stats = rename_stats(data.describe().loc[['count', 'mean']])
    total_time = data.sum()
    total_time.name = 'total time played'
    return stats.append(total_time)


@pytest.mark.wip
def test_overall_time_offs():
    data = [sc.time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 19)]
    stats = data_stats(valid_data(data))
    assert len(stats) == 3
    assert len(stats.columns) == 10
    assert dict(stats.loc[:, 'Nicholas']) == {'matches played': 4.0, 'average time played': 34.75, 'total time played': 139.0}
