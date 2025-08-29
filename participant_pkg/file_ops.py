import csv
from pathlib import Path

workspace = Path("workspace")# create folder work space
workspace.mkdir(exist_ok=True)
csv_file = workspace / "contact.csv"



def save_participant(path, participant_dict):
  

  file_exists = path.exists()
  fieldnames = participant_dict.keys()
# newline='' prevent writer from adding additional blank line during input and output handling
  with open(csv_file, "a", encoding="utf-8",newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    if not file_exists:
      writer.writeheader() #if file not exist

    writer.writerow(participant_dict)


  # with open(csv_file, "r", encoding="utf-8")as f:
  #   reader = csv.reader(f)

# load participant from csv and return them as list of dict
def load_participants(path):
  
    
  with open(path, 'r', newline='', encoding="utf-8") as csv_file:
     reader = csv.DictReader(csv_file)
     for row in reader:
       print(row)
  
  