from bs4 import BeautifulSoup
from collections import Counter


file_path = 'python_class_question.html' 
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')[1:] 


all_colors = []
for row in rows:
    colors_cell = row.find_all('td')[1] 
    colors = [color.strip().upper() for color in colors_cell.text.split(',')]
    all_colors.extend(colors)


corrected_colors = {'BLEW': 'BLUE', 'ARSH': 'ASH'} 
all_colors = [corrected_colors.get(color, color) for color in all_colors]


color_counts = Counter(all_colors)


sorted_colors = sorted(color_counts.keys())  
color_to_value = {color: idx for idx, color in enumerate(sorted_colors)}  


total_weighted_sum = sum(color_to_value[color] * count for color, count in color_counts.items())
total_colors = sum(color_counts.values())
mean_index = total_weighted_sum / total_colors  


mean_color = sorted_colors[round(mean_index)]

def median_color(color_counts):
    sorted_colors = sorted(color_counts.keys())
    frequencies = [color_counts[color] for color in sorted_colors]
    cumulative = 0
    total = sum(frequencies)
    for i, freq in enumerate(frequencies):
        cumulative += freq
        if cumulative >= total / 2:
            return sorted_colors[i]
        
def variance_color(color_counts):
    sorted_colors = sorted(color_counts.keys())
    frequencies = [color_counts[color] for color in sorted_colors]
    mean_freq = sum(frequencies) / len(frequencies)
    return sum((freq - mean_freq) ** 2 for freq in frequencies) / len(frequencies)

def probability_of_color(color, color_counts):
    total = sum(color_counts.values())
    return color_counts[color.upper()] / total


median_color_result = median_color(color_counts)
most_worn_color = color_counts.most_common(1)[0][0]
median_color_result = median_color(color_counts)
variance_result = variance_color(color_counts)
probability_red = probability_of_color("RED", color_counts)


print("All Colors (Monday to Friday):", all_colors)
print("Color Frequencies:", color_counts)
print("Most Worn Color:", most_worn_color)
print("Mean Color:", mean_color)
print("Median Color:", median_color_result)
print("Variance of Colors:", variance_result)
print("Probability of Choosing Red:", probability_red)