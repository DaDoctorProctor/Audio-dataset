import os
import shutil

main_folder = "./Dataset"  # Replace this with the actual path to your main folder
output_folder = "./Output"  # Replace this with the desired output folder path

words = ["Adelante", "Atrás", "Izquierda", "Derecha"]

# Create output folders for each word
for word in words:
    word_folder = os.path.join(output_folder, word)
    os.makedirs(word_folder, exist_ok=True)

# Iterate through each person's folder
for person_folder in os.listdir(main_folder):
    if not os.path.isdir(os.path.join(main_folder, person_folder)):
        continue

    # Move the recordings to their respective word folders
    for i, word in enumerate(words):
        word_folder = os.path.join(output_folder, word)
        person_recordings = [f"recording{i}.wav" for i in range(10 * i, 10 * (i + 1))]
        for recording in person_recordings:
            src_path = os.path.join(main_folder, person_folder, recording)
            dst_path = os.path.join(word_folder, f"{person_folder}_{recording}")
            print(src_path,dst_path)
            shutil.copy(src_path, dst_path)


#%%
