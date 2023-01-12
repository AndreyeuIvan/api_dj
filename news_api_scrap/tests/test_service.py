from unittest import mock, main, TestCase

from service import get_news


class NewsAPITestCase(TestCase):
    @mock.patch("service.requests")
    def test_get_news(self, my_mock):

        req_mock = mock.MagicMock()
        req_mock.status_code = 200
        req_mock.json.return_value = (
            "Crypto finance firm BlockFi files for bankruptcy following the fall of FTX"
        )

        my_mock.get.return_value = req_mock

        self.assertEqual(
            "Crypto finance firm BlockFi files for bankruptcy following the fall of FTX",
            get_news("Finance"),
        )


if __name__ == "__main__":
    main()
