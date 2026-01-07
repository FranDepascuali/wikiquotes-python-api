import pytest
import wikiquotes
from tests.authors.Author import fetch_all_authors

RANDOM_TRIES = 3  # Constants should be UPPER_CASE


@pytest.fixture(scope="module")
def all_authors():
    return fetch_all_authors()


@pytest.mark.parametrize(
    "author",
    fetch_all_authors(),
    ids=lambda author: f"{author.name}_{author.language}"
)
class TestAuthor:

    def test_get_quotes(self, author):
        """Test that all expected quotes are fetched."""
        fetch_quotes = wikiquotes.get_quotes(author.name, author.language)

        missing_quotes = set(author.quotes) - set(fetch_quotes)

        assert not missing_quotes, (
            f"Author: {author.name}. Missing quotes: {missing_quotes}"
        )

    def test_quotes_length(self, author):
        """Test that fetched quotes meet minimum length and have no duplicates."""
        fetch_quotes = wikiquotes.get_quotes(author.name, author.language)

        # New quotes may be added, but quotes shouldn't be removed
        assert len(fetch_quotes) >= len(author.quotes), (
            f"Expected at least {len(author.quotes)} quotes, got {len(fetch_quotes)}"
        )

        # No duplicates
        assert len(fetch_quotes) == len(set(fetch_quotes)), (
            "Duplicate quotes found"
        )

    def test_random_quote(self, author):
        """Test that random_quote returns different quotes when possible."""
        fetch_quotes = wikiquotes.get_quotes(author.name, author.language)
        number_of_quotes = len(fetch_quotes)

        # Skip test if only one quote
        if number_of_quotes <= 1:
            pytest.skip(f"Only {number_of_quotes} quote(s) available")

        # Try multiple times to get different random quotes
        for _ in range(RANDOM_TRIES):
            quote1 = wikiquotes.random_quote(author.name, author.language)
            quote2 = wikiquotes.random_quote(author.name, author.language)

            if quote1 != quote2:
                return  # Success - got different quotes

        pytest.fail(
            f"random_quote returned the same quote {RANDOM_TRIES} times "
            f"for {author.name} (out of {number_of_quotes} available quotes)"
        )
