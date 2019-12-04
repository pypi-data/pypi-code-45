# mocker fixture becomes available after installing pytest-mock
# https://github.com/pytest-dev/pytest-mock
def test_ping_matomo(mocker):
  from .matomo_sdk_py import ping_matomo
  def mockreturn(*args, **kwargs): return "foo"
  mocked_post = mocker.patch('matomo_sdk_py.matomo_sdk_py.requests.post', side_effect=mockreturn)
  ping_matomo("/test", "https://example.com", 1, "abcdef", "https://example.matomo.cloud")

  # check that mocked object is called
  # https://github.com/pytest-dev/pytest-mock/commit/68868872195135bdb90d45a5cb0d609400943eae
  mocked_post.assert_called()


# TODO
# Create a functional test against a real matomo endpoint
# Check the response as follows
# assert response.__dict__['_content'] == '{"status":"success","tracked":1,"invalid":0}'
# This ensures that the payload was matomo-valid also (not just that the http request was sent)
