sample = {
    "physics": 88, "maths": 75, "chemistry": 72, "Basic electrical": 89
}
mini = sample["physics"]
sub = "physics"
for i in sample:
    if sample[i] < mini:
        mini = sample[i]
        sub=i
print(sub+" ", end='')
print(mini)
