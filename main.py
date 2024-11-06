import requests
from bs4 import BeautifulSoup
import csv
import random
import tkinter as tk
from tkinter import messagebox

# Scrape and write data to CSV
def scrape_anime_list():
    anime_data = []
    urls = [
        "https://myanimelist.net/topanime.php",
        "https://myanimelist.net/topanime.php?limit=50"
    ]

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        anime_list = soup.find_all('tr', class_='ranking-list')

        for anime in anime_list:
            rank = anime.find('span', class_='lightLink').text.strip()
            title = anime.find('h3', class_='anime_ranking_h3').a.text.strip()
            score = anime.find('span', class_='score-label').text.strip()
            anime_data.append([rank, title, score])

    # Save to CSV
    with open('anime_rankings.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Rank', 'Title', 'Score'])
        writer.writerows(anime_data)

    return anime_data

# Pick and display random anime
def pick_random_anime():
    random_anime = random.choice(anime_data)
    messagebox.showinfo("Random Anime", f"Rank: {random_anime[0]}\nTitle: {random_anime[1]}\nScore: {random_anime[2]}")

# Scrape data once and save it
anime_data = scrape_anime_list()

# Create GUI window
root = tk.Tk()
root.title("Random Anime Picker")

# Button to pick random anime
button = tk.Button(root, text="Pick Random Anime", command=pick_random_anime, padx=20, pady=10)
button.pack(pady=20)

# Run the GUI application
root.mainloop()

