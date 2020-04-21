import os
 
os.chdir("I:\\")
         
for root, dirs, files in os.walk(".", topdown = False):
   for file in files:
      if file.startswith('._'):
          os.remove(os.path.join(root, file))

print('DONE')
