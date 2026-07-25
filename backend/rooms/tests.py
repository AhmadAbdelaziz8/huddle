from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class RoomAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_room(self):
        response = self.client.post(reverse("room-list-create"))
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertIn("join_url", response.data)

    def test_get_room(self):
        create_response = self.client.post(reverse("room-list-create"))
        room_id = create_response.data["id"]
        response = self.client.get(reverse("room-detail", kwargs={"pk": room_id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.data["id"]), str(room_id))

    def test_delete_room(self):
        create_response = self.client.post(reverse("room-list-create"))
        room_id = create_response.data["id"]
        response = self.client.delete(reverse("room-detail", kwargs={"pk": room_id}))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.client.get(reverse("room-detail", kwargs={"pk": room_id})).status_code, 404)
