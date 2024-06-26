class TestMainEndpoints:
    def test_home(self, client):
        response = client.get("/")
        assert response.status_code == 200
