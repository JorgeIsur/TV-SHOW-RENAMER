import os
import re
path = '/home/isur/Videos/TV Shows/HajimeNoIppo/HajimeNoIppo/Season02/'
Destination = '/home/isur/Videos/TV Shows/HajimeNoIppo/HajimeNoIppo/Season02/'
files = os.listdir(path)
files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
count=1
def main():
    for count,filename in enumerate(files):
        dst ="HajimeNoIppoS02E" + str(count+1) + ".mkv"
          
        # rename() function will
        # rename all the files
        os.rename(os.path.join(path, filename),  os.path.join(Destination, dst))  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()