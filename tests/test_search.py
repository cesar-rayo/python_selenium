#    Given the DuckDuckGo home page is displayed
#    When the user searches for "home"
#    Then the search results title contains "home"
#    And the search result query is "home"
#    And the search result links pertain "home"
import pytest
from search import DuckDuckGoSearchPage
from result import DuckDuckGoResultPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(web_browser, phrase):
    # driver comes from the web_browser fixture
    search_page = DuckDuckGoSearchPage(web_browser)
    result_page = DuckDuckGoResultPage(web_browser)

    search_page.load()
    search_page.search(phrase)

    assert phrase in result_page.search_input_value()

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    assert phrase in result_page.title()