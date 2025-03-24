import os
import sys
import re

def fix_filename(root_folder: str):
  for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
      name, ext = os.path.splitext(filename)
      modified = False

      new_name = re.sub(r'\(Japan\)', '(J)', name)
      if new_name != name:
        name = new_name
        modified = True

      new_name = re.sub(r'Pocket Monsters -', 'Pokemon', name)
      if new_name != name:
        name = new_name
        modified = True

      if name.rstrip() != name:
        new_name = name.rstrip()
        modified = True
      
      if modified:
        new_filename = f'{new_name}{ext}'
        old_path = os.path.join(dirpath, filename)
        new_path = os.path.join(dirpath, new_filename)
        try:
          os.rename(old_path, new_path)
        except Exception as e:
          print(f'Failed to rename "{filename}": {e}')

if __name__ == '__main__':
  folder_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
  fix_filename(folder_path)
