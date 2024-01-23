echo "real name: Isha Suba"
echo "Linux username: ishasuba"
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsvwxyz]" | wc -l 
