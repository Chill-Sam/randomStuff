from main import p
from save_class import saves

def save():
    selected_save = "s1.txt"    # Choose save from s1, s2 and s3 -> selected_save
    s = saves(selected_save, p)
    s.create_save()

def load():
    selected_save = "s1.txt"    # Choose save to laod s1, s2 and s3 -> selected_save
    s = saves(selected_save, p)
    s.load_save()