import pytest
import wikiquotes
from tests.authors.Author import fetch_all_authors

RANDOM_TRIES = 3


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
        extra_quotes = set(fetch_quotes) - set(author.quotes)

        if missing_quotes:
            # Print full comparison for debugging
            error_msg = (
                f"\n\n{'='*80}\n"
                f"Author: {author.name}\n"
                f"Expected {len(author.quotes)} quotes, fetched {len(fetch_quotes)}\n"
                f"{'='*80}\n"
                f"\nMISSING QUOTES ({len(missing_quotes)}):\n"
                f"{'-'*80}\n"
            )
            for i, q in enumerate(missing_quotes, 1):
                error_msg += f"{i}. {q}\n\n"

            error_msg += (
                f"\n{'='*80}\n"
                f"ALL FETCHED QUOTES ({len(fetch_quotes)}):\n"
                f"{'='*80}\n"
            )
            for i, q in enumerate(fetch_quotes, 1):
                error_msg += f"{i}. {q}\n\n"

            if extra_quotes:
                error_msg += (
                    f"\n{'='*80}\n"
                    f"EXTRA QUOTES NOT IN TEST DATA ({len(extra_quotes)}):\n"
                    f"{'='*80}\n"
                )
                for i, q in enumerate(extra_quotes, 1):
                    error_msg += f"{i}. {q}\n\n"

            pytest.fail(error_msg)

    def test_quotes_length(self, author):
        """Test that fetched quotes meet minimum length and have no duplicates."""
        fetch_quotes = wikiquotes.get_quotes(author.name, author.language)

        # New quotes may be added, but quotes shouldn't be removed
        assert len(fetch_quotes) >= len(author.quotes), (
            f"\n\nAuthor: {author.name}\n"
            f"Expected at least {len(author.quotes)} quotes, got {len(fetch_quotes)}\n"
            f"\nFetched quotes:\n"
            f"{chr(10).join('  - ' + q[:80] + '...' if len(q) > 80 else '  - ' + q for q in fetch_quotes[:10])}"
        )

        # No duplicates
        duplicates = [q for q in fetch_quotes if fetch_quotes.count(q) > 1]
        assert len(fetch_quotes) == len(set(fetch_quotes)), (
            f"\n\nDuplicate quotes found for {author.name}:\n"
            f"{chr(10).join('  - ' + q[:80] + '...' if len(q) > 80 else '  - ' + q for q in set(duplicates))}"
        )

    def test_random_quote(self, author):
        """Test that random_quote returns different quotes when possible."""
        fetch_quotes = wikiquotes.get_quotes(author.name, author.language)
        number_of_quotes = len(fetch_quotes)

        # Skip test if only one quote
        if number_of_quotes <= 1:
            pytest.skip(f"Only {number_of_quotes} quote(s) available")

        # Try multiple times to get different random quotes
        collected_quotes = []
        for _ in range(RANDOM_TRIES):
            quote1 = wikiquotes.random_quote(author.name, author.language)
            quote2 = wikiquotes.random_quote(author.name, author.language)
            collected_quotes.extend([quote1, quote2])

            if quote1 != quote2:
                return  # Success - got different quotes

        pytest.fail(
            f"\n\nrandom_quote returned the same quote {RANDOM_TRIES} times "
            f"for {author.name}\n"
            f"Total quotes available: {number_of_quotes}\n"
            f"\nQuotes returned:\n"
            f"{chr(10).join('  - ' + q[:80] + '...' if len(q) > 80 else '  - ' + q for q in set(collected_quotes))}"
        )
