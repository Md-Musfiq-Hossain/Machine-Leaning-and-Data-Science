# Dictonary Filtering Based on condition

scores = {'Alice' : 85, 'Bob' : 70, 'Charlie' : 95, 'David' : 60}

filtered_scores = {name : score for name , score in scores.items() if score >= 80}

print('Filtered Scores: ', filtered_scores)