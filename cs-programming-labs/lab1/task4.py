seconds = 7384
hours = seconds // 3600
min = (seconds % 3600) // 60
sec = seconds % 60
print(f"{hours:02d}:{min:02d}:{sec:02d}")