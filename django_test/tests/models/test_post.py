import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='Chainsaw Man Deaths entrance')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'Chainsaw Man Deaths entrance'