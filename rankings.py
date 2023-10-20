import csv
import json
def saveCsv(dictData,name,Tag = False):

    print("to csv..")
    with open(f'{name}.csv', 'a', encoding='utf-8',newline='') as csvfile:
        fp = csv.DictWriter(csvfile,fieldnames=dictData[0].keys())
        if Tag:
            fp.writeheader()
        try:
            fp.writerows(dictData)
        except Exception as e:
            print(e)

def save_ranking(name):
    f = open(f'./json/{name}.json', 'r')
    content = f.read()
    f.close()
    fromDatas = json.loads(content)["data"]
    datas =[]
    time_name = name.split("_")[-1]
    for fromData in fromDatas:
        data ={
            "University":fromData["aliases"],
            f"No. of FTE Students_{time_name}":int(fromData["stats_number_students"].replace(",","")),
            f"No. of students per staff_{time_name}":fromData["stats_student_staff_ratio"],
            f"International Students_{time_name}":fromData["stats_pc_intl_students"],
            f"Female:Male Ratio_{time_name}":str(fromData["stats_female_male_ratio"]),
            f"Time High Education_{time_name}": fromData["rank"].replace("=",""),
            f'Time_{time_name}': time_name
        }
        print(data)
        datas.append(data)
    saveCsv(datas,name,True)

def save_All(name):
    f = open(f'./json/{name}.json', 'r')
    content = f.read()
    f.close()
    fromDatas = json.loads(content)["data"]
    datas =[]
    for fromData in fromDatas:
        data ={
            "University":fromData["aliases"],
            "No. of FTE Students":fromData["stats_number_students"],
            "No. of students per staff":fromData["stats_student_staff_ratio"],
            "International Students":fromData["stats_pc_intl_students"],
            "Female:Male Ratio":fromData["stats_female_male_ratio"],
            "Time High Education": fromData["rank"].replace("=",""),
            "Time":name.split("_")[-1]

        }
        print(data)
        datas.append(data)
    if name == "rankings_2017":
        saveCsv(datas,"rankings_all",True)
    else:
        saveCsv(datas,"rankings_all",False)


save_ranking("rankings_2017")
save_ranking("rankings_2018")
save_ranking("rankings_2019")
save_ranking("rankings_2020")
save_ranking("rankings_2021")
save_ranking("rankings_2022")
save_ranking("rankings_2023")

for name in ["rankings_2017","rankings_2018","rankings_2019","rankings_2020","rankings_2021","rankings_2022","rankings_2023"]:
    save_All(name)


# https://www.timeshighereducation.com/sites/default/files/the_data_rankings/arts_humanities_rankings_2023_0__80ec75f8685f22deffb4a4360592053f.json
# https://www.timeshighereducation.com/sites/default/files/the_data_rankings/arts_humanities_rankings_2022_0__00f8c6b4881c4092e0927ee6464eb959.json
# https://www.timeshighereducation.com/sites/default/files/the_data_rankings/arts_humanities_rankings_2021_0__7766d2b47427ff8e132b92c286980372.json
# https://www.timeshighereducation.com/sites/default/files/the_data_rankings/arts_humanities_rankings_2020_0__c44ef1ab44ef1f960ffd24d7b5da2d31.json
