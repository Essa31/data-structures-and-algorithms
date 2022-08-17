import pytest
from hashtable.hashtable import *


def test_setting_data_into_hash_table(hash_table):
    hash_table.set("key3", "#!!#")
    assert len(hash_table.keys()) == 3
    assert hash_table.keys()[2] == "key3"


def test_retrieving_based_on_key(hash_table):
    assert hash_table.get("key1") == "Ahmad"
    assert hash_table.get("key2") == "Ali"
    assert hash_table.contains("key1") is True


def test_retrieving_unavailable_key_from_hash_table(hash_table):
    assert hash_table.get("key5") is None
    assert hash_table.contains("key6") is False


def test_return_all_keys_in_hash_table(hash_table):
    assert hash_table.keys() == ["key1", "key2"]


def test_handling_collision_within_hash_table(hash_table):
    hash_table.set("key1", "Essa")
    assert len(hash_table.get("key1")) == 2
    hash_table.set("key1", "!!@")
    assert len(hash_table.get("key1")) == 3


def test_retrieve_value_from_bucket_that_has_collision(hash_table):
    hash_table.set("key1", "Essa")
    assert hash_table.get("key1") == ("Essa","Ahmad")
    hash_table.set("key1", "@")
    assert hash_table.get("key1") == ("@", "Essa","Ahmad")


def test_hash_key_to_in_range_value(hash_table):
    assert hash_table._HashTable__hash("Essa") == 452


@pytest.fixture
def hash_table():
    hash_table = HashTable()
    hash_table.set("key1", "Ahmad")
    hash_table.set("key2", "Ali")
    return hash_table