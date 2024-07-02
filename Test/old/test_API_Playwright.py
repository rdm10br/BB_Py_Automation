import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

# GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
# assert '', "GITHUB_API_TOKEN is not set"


# @pytest.fixture(scope="session")
# def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
#     headers = {
#         # We set this header per GitHub guidelines.
#         "Accept": "application/vnd.github.v3+json",
#         # Add authorization token to all requests.
#         # Assuming personal access token available in the environment.
#         "Authorization": f"token {GITHUB_API_TOKEN}",
#     }
#     request_context = playwright.request.new_context(
#         base_url="https://api.github.com", extra_http_headers=headers
#     )
#     yield request_context
#     request_context.dispose()

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    headers = {
    }
    request_context = playwright.request.new_context(
        base_url="https://sereduc.blackboard.com/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()
    

def test_api_endpoint(api_request_context: APIRequestContext):
    response = api_request_context.get('learn/api/v1/oauth2/authorizationcode')
    assert response.status == 200

teste = test_api_endpoint(APIRequestContext)
print(teste)