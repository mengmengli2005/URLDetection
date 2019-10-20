import random


def process_URL_list(file_dest1, file_dest2):
    fout_1 = open("phish_test1.txt", "w")
    fout_2 = open("phish_test2.txt", "w")
    fout_1.truncate()
    fout_2.truncate()
    with open(file_dest1) as file:
        i = 0
        for line in file:
            record = line.split(',')[1].strip() + ',1' + '\n'
            i = i + 1
            if i >= 1000:
                break
            fout_1.write(record)
        fout_1.close()
    with open(file_dest2) as file:
        i = 0
        for line in file:
            record = line.strip() + ',0' + '\n'
            i = i + 1
            if i >= 1000:
                break
            fout_2.write(record)
        fout_2.close()

def mix():
    fin_1 = open("phish_test1.txt", "r")
    fin_2 = open("phish_test2.txt", "r")
    fout = open("phish_test2000.txt", "w")
    fout.truncate()
    i = 0
    j = 0
    while i < 1000 or j < 1000:
        if random.choice([True, False]) and i < 1000:
            fout.write(fin_1.readline())
            i = i + 1
        elif j < 40000:
            fout.write(fin_2.readline())
            j = j + 1


# def process_kaggle_randomize(original_file, No_bad, No_good):
#     fout = open("kaggle_random_40000", "w")
#     fout.truncate()
#     with open(original_file, encoding = "ISO-8859-1") as file:
#         nb = 0
#         ng = 0
#         for line in file:


# 提取多个phishTank文件里的malicious URL
def process_phishTank(file_phishTank_list):
    fout = open("phishTank_dataset.txt","w")
    fout.truncate()
    with open(file_phishTank_list) as file:
        for line in file:
            with open(line.strip()) as subfile:
                for r in subfile:
                    tmp = r.split(',')[1].strip()
                    if tmp == 'url':
                        continue
                    record = "//" + tmp.split('//')[1] + ',1' + '\n'
                    fout.write(record)
    fout.close()


def process_kaggle_list(file_bad_good, No_bad, No_good):
    fout = open("kaggle_allBad_allGood.txt", "w")
    fout.truncate()
    with open(file_bad_good, encoding = "ISO-8859-1") as file:
        nb = 0
        ng = 0
        for line in file:
            # print(line)
            record = line.split(',')
            url = record[0]
            lable = record[1].strip()
            if url == 'url' or (lable != 'good' and lable != 'bad'):
                continue

            if lable == 'bad':
                malicious = '1'
            else:
                malicious = '0'

            out = '//' + url.strip() + ',' + malicious + '\n'
            if malicious == '0':
                if ng >= No_good:
                    continue
                else:
                    fout.write(out)
                    ng = ng + 1
            else:
                if nb >= No_bad:
                    continue
                else:
                    fout.write(out)
                    nb = nb + 1

            if nb + ng >= No_good + No_bad:
                break
        print('# good: %d', ng)
        print('# bad: %d', nb)
    fout.close()


# process_kaggle_list("Kaggle_data.txt", 1000000, 1000000)
# process_URL_list("phishing_verified_online.csv", "Benign_list_big_final.csv")
# mix()
process_phishTank("phishTank_list.txt")