echo "real name: Isha Suba"
echo "Linux username: ishasuba"
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "a" | grep -v "[bdeghijklnpqrsvwxyz]" | wc -l
gunzip -c dictionary.gz | grep "b" | grep -v "[cdefghjkmopqsuvwxyz]" | wc -l
gunzip -c dictionary.gz | grep "c" | grep -v "[befghjklpqrstuvwxyz]" | wc -l
gunzip -c dictionary.gz | grep "z" | grep -v "[bcdefhjklmpqstuvwxy]" | wc -l
