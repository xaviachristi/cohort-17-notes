"""A CLI tool for searching anime."""

from argparse import ArgumentParser, Namespace

import requests as req

BASE_URL = "https://api.jikan.moe/v4/anime?"


def generate_url(query: str, max_results: int, include_nsfw: bool) -> str:
    """Returns a formatted URL based on CLI arguments."""

    url = BASE_URL + f"&limit={max_results}&q={query}" + ("&sfw" if not include_nsfw else "")
    return url


def display_anime_data(anime_data: dict):
    """Displays key details about an anime from a dict."""
    title = anime_data['titles'][0]['title']
    score = anime_data['score']
    scored_by = anime_data['scored_by']
    rating = anime_data["rating"].split(" - ")[0]

    print(f"{title} ({rating}) ~ {score}/10 ({scored_by})")


def display_results(results: list[dict]) -> None:
    """Displays each anime result in sequence."""

    for r in results:
        display_anime_data(r)

def get_arguments() -> Namespace:
    ...

if __name__ == "__main__":

    raise NotImplementedError("You need to write the code!")
