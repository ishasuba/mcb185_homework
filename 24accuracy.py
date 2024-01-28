def accuracy(tp, tn, fp, fn):
	acc = (tp + tn) / (tp + fp + tn + fn)
	rec = (tp) / (tp + fn)
	prec = (tp) / (tp + fp)
	F1 = (2 * prec * rec) / (prec + rec)
	print("Your accuracy score is", round(acc, ndigits=2), "and your F1 score is", round(F1, ndigits=2))
x = accuracy(4, 6, 8, 1)
print(x)
y = accuracy(1, 3, 10, 12)
print(y)
z = accuracy(-1, -3, -5, -6)
print(z)