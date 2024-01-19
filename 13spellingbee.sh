cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep "bdefghjklmpqstuvxy" | grep -E ".{4,}"
