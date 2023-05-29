import sender_stand_request
import data


def get_new_order_track():
    order_body = data.order_body
    resp_order = sender_stand_request.post_new_order(order_body)
    return resp_order.json()["track"]

def positive_assert():
    track = get_new_order_track()
    track_response = sender_stand_request.get_order_body(track)

    assert track_response.status_code == 200

def test_get_order_body():
    positive_assert()