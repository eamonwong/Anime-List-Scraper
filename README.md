# Anime-List-Scraper
This project scrapes the top 100 anime rankings from MyAnimeList and allows you to randomly select an anime to view its details in a GUI window. It uses Python libraries such as requests, BeautifulSoup, csv, and tkinter.

## Features and Functionality
- **Web Scraping**: Retrieves the top 100 anime from MyAnimeList by scraping two pages of rankings.
- **CSV Storage**: Saves the scraped anime rankings to a CSV file (anime_rankings.csv).
- **GUI Interface**: A button in a simple GUI window allows users to randomly select an anime and view its rank, title, and score.

## How to Use
1. Run the script to open the GUI window.
2. Click the "Pick Random Anime" button to randomly select an anime from the top 100 and view its rank, title, and score.
3. The anime_rankings.csv file will be generated in the project directory, storing the top 100 anime rankings.

## Code Overview
- **scrape_anime_list**: Scrapes the top 100 anime from MyAnimeList across two pages and saves the data to anime_rankings.csv.
- **pick_random_anime**: Selects a random anime from the top 100 and displays its details in a pop-up message box.
- **Tkinter GUI**: The interface features a single button to trigger the random anime selection.

## Additional Notes
- MyAnimeList's Terms of Service: Please ensure your use complies with MyAnimeList’s terms and conditions.
- Rate Limits: Avoid running the scraper too frequently to prevent overloading MyAnimeList's servers.

https://github.com/user-attachments/assets/6c587a39-7e2f-4056-8aba-16f84bbf12ac
