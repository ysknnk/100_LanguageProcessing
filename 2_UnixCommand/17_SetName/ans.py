# 2024年1月29日
"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
"""

f = open('2_UnixCommand/17_DiffLetters/popular-names.txt', 'r')
tmp_l = []

for i in f:
    tmp_l.append(i.split('\t')[0])

print(sorted(set(tmp_l)))

"""
# python
['Abigail', 'Aiden', 'Alexander', 'Alexis', 'Alice', 'Amanda', 'Amelia', 'Amy', 'Andrew', 'Angela', 'Anna', 'Annie', 'Anthony', 'Ashley', 'Austin', 'Ava', 'Barbara', 'Benjamin', 'Bertha', 'Bessie', 'Betty', 'Brandon', 'Brian', 'Brittany', 'Carol', 'Carolyn', 'Charles', 'Charlotte', 'Chloe', 'Christopher', 'Clara', 'Crystal', 'Cynthia', 'Daniel', 'David', 'Deborah', 'Debra', 'Donald', 'Donna', 'Doris', 'Dorothy', 'Edward', 'Elijah', 'Elizabeth', 'Emily', 'Emma', 'Ethan', 'Ethel', 'Evelyn', 'Florence', 'Frances', 'Frank', 'Gary', 'George', 'Hannah', 'Harper', 'Harry', 'Heather', 'Helen', 'Henry', 'Ida', 'Isabella', 'Jacob', 'James', 'Jason', 'Jayden', 'Jeffrey', 'Jennifer', 'Jessica', 'Joan', 'John', 'Joseph', 'Joshua', 'Judith', 'Julie', 'Justin', 'Karen', 'Kathleen', 'Kelly', 'Kimberly', 'Larry', 'Laura', 'Lauren', 'Liam', 'Lillian', 'Linda', 'Lisa', 'Logan', 'Lori', 'Lucas', 'Madison', 'Margaret', 'Marie', 'Mark', 'Mary', 'Mason', 'Matthew', 'Megan', 'Melissa', 'Mia', 'Michael', 'Michelle', 'Mildred', 'Minnie', 'Nancy', 'Nicholas', 'Nicole', 'Noah', 'Oliver', 'Olivia', 'Pamela', 'Patricia', 'Rachel', 'Rebecca', 'Richard', 'Robert', 'Ronald', 'Ruth', 'Samantha', 'Sandra', 'Sarah', 'Scott', 'Sharon', 'Shirley', 'Sophia', 'Stephanie', 'Steven', 'Susan', 'Tammy', 'Taylor', 'Thomas', 'Tracy', 'Tyler', 'Virginia', 'Walter', 'William']

# cut, sort, uniq
cut -f 1 2_UnixCommand/17_DiffLetters/popular-names.txt | sort | uniq | paste -d, -s
Abigail,Aiden,Alexander,Alexis,Alice,Amanda,Amelia,Amy,Andrew,Angela,Anna,Annie,Anthony,Ashley,Austin,Ava,Barbara,Benjamin,Bertha,Bessie,Betty,Brandon,Brian,Brittany,Carol,Carolyn,Charles,Charlotte,Chloe,Christopher,Clara,Crystal,Cynthia,Daniel,David,Deborah,Debra,Donald,Donna,Doris,Dorothy,Edward,Elijah,Elizabeth,Emily,Emma,Ethan,Ethel,Evelyn,Florence,Frances,Frank,Gary,George,Hannah,Harper,Harry,Heather,Helen,Henry,Ida,Isabella,Jacob,James,Jason,Jayden,Jeffrey,Jennifer,Jessica,Joan,John,Joseph,Joshua,Judith,Julie,Justin,Karen,Kathleen,Kelly,Kimberly,Larry,Laura,Lauren,Liam,Lillian,Linda,Lisa,Logan,Lori,Lucas,Madison,Margaret,Marie,Mark,Mary,Mason,Matthew,Megan,Melissa,Mia,Michael,Michelle,Mildred,Minnie,Nancy,Nicholas,Nicole,Noah,Oliver,Olivia,Pamela,Patricia,Rachel,Rebecca,Richard,Robert,Ronald,Ruth,Samantha,Sandra,Sarah,Scott,Sharon,Shirley,Sophia,Stephanie,Steven,Susan,Tammy,Taylor,Thomas,Tracy,Tyler,Virginia,Walter,William
"""
