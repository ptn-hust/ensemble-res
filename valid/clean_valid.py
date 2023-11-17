ground_truth = []
with open("ecapa_valid_v2.txt", "r") as f:
    for line in f:
        ground_truth.append(float(line.split('\t')[2]))

pairs = []
scores = []
with open("ecapa_asv_score_valid.txt", "r") as f1:
    for line in f1:
        pairs.append(line.split('\t')[:2])
        scores.append(float(line.split('\t')[2]))

scores1 = []
with open("res2net_asv_score_valid.txt", "r") as f7:
    for line in f7:
        scores1.append(float(line.split('\t')[2]))

scores2 = []
with open("res2Next_asv_score_valid.txt", "r") as f8:
    for line in f8:
        scores2.append(float(line.split('\t')[2]))

submission_ecapa = []
submission_res2net = []
submission_res2Next = []
gt = []
for i in range(len(scores)):
    if ground_truth[i] == 1 and scores[i] <= 0.4:
        continue
    else:
        submission_ecapa.append([pairs[i][0], pairs[i][1], str(scores[i])])
        submission_res2net.append([pairs[i][0], pairs[i][1], str(scores1[i])])
        submission_res2Next.append([pairs[i][0], pairs[i][1], str(scores2[i])])
        gt.append([pairs[i][0], pairs[i][1], str(ground_truth[i])])

with open("ecapa_asv_score_valid_new.txt", "w") as f3:
    for line in submission_ecapa:
        f3.write('\t'.join(line) + '\n')

with open("ecapa_valid_v2_new.txt", "w") as f4:
    for line in gt:
        f4.write('\t'.join(line) + '\n')

with open("res2net_asv_score_valid_new.txt", "w") as f5:
    for line in submission_res2net:
        f5.write('\t'.join(line) + '\n')

with open("res2Next_asv_score_valid_new.txt", "w") as f6:
    for line in submission_res2Next:
        f6.write('\t'.join(line) + '\n')