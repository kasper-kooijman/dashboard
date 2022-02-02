import pandas as pd

from datetime import datetime

from utils.click_request_ratio import count_clicks_and_requests

def test_count_clicks_and_requests():
    day_1 = datetime(2022, 1,1)
    day_2 = datetime(2022,1,2)

    clicks = pd.DataFrame({
        "user_id": ["u1", "u2", "u3"],
        "datetime": [day_1, day_2, day_2],
    })

    requests = pd.DataFrame({
        "user_id": ["u1", "u2", "u3", "u3", "u4"],
        "datetime": [day_1, day_1, day_2, day_2, day_2],
    })

    result = count_clicks_and_requests(clicks, requests)

    should_be = pd.DataFrame({
        "date": ["2022-01-02", "2022-01-01"],
        "clicks": [2, 1],
        "requests": [3, 2],
        "total": [2/3, 1/2],
    })

    pd.testing.assert_frame_equal(result, should_be)