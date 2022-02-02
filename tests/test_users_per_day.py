import pandas as pd

from utils.users_per_day import _get_users_per_day


def test__get_users_per_day():
    data = pd.DataFrame(
        data = {
            'user_id': ["u1", "u2", "u1",
                        "u2", "u3", "u1"],
            'date': ["2022-01-01", "2022-01-01", "2022-01-01",
                     "2022-01-02", "2022-01-02", "2022-01-02"]
                }
        )

    result = _get_users_per_day(data, "text_search")
    should_be = pd.DataFrame(
        data = {
            "date": ["2022-01-01", "2022-01-02"],
            "total": [2, 3],
            "type": ["text_search", "text_search"]
        }
    )

    pd.testing.assert_frame_equal(result, should_be)

