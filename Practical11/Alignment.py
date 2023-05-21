with open("ACE2_cat.fa") as f:
    cat_seq = f.read().splitlines()[1]
with open("ACE2_mouse.fa") as f:
    mouse_seq = f.read().splitlines()[1]
with open("ACE2_human.fa") as f:
    human_seq = f.read().splitlines()[1]

def align(seq1, seq2):
    edit_distance = 0
    identical_count = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            identical_count += 1
        else:
            edit_distance += 1
    alignment_score = identical_count / len(seq1)
    return (alignment_score, identical_count)

cat_mouse_score, cat_mouse_identical = align(cat_seq, mouse_seq)
cat_human_score, cat_human_identical = align(cat_seq, human_seq)
mouse_human_score, mouse_human_identical = align(mouse_seq, human_seq)

print("Alignment score and percentage of identical amino acids:")
print("Cat-Mouse:", cat_mouse_score, cat_mouse_identical/len(cat_seq))
print("Cat-Human:", cat_human_score, cat_human_identical/len(cat_seq))
print("Mouse-Human:", mouse_human_score, mouse_human_identical/len(mouse_seq))


