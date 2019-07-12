import json
import collections as cl



def main():
    input("reading")
    reading()
    input("displaying")
    displaying()
    input("writing")
    writing()



def reading():
    f = open("myu_s.json", 'r')

    # read json format
    json_data = json.load(f)
    name_list = ["eri", "honoka", "kotori", "umi", "rin", "mai", "nozomi", "hanayo", "niko"]

    for name in name_list:
        print("{0:6s} hight:{1}cm BWH: ".format(name, json_data[name]["height"]), end="\t")
        for i in range(len(json_data[name]["BWH"])):
            print("{}".format(json_data[name]["BWH"][i]), end="\t")
        print()
    return



def displaying():
    f = open("myu_s.json", 'r')
    json_data = json.load(f)
    print("{}".format(json.dumps(json_data, indent=4)))
    return



def writing():
    name_list = ["honoka", "eri", "kotori", "umi", "rin", "mai", "nozomi", "hanayo", "niko"]

    height = [157, 162, 159, 159, 155, 161, 159, 156, 154]

    BWH = [[78, 58, 82],[88, 60, 84],[80, 58, 80],[76, 58, 80],
           [75, 59, 80],[78, 56, 83],[90, 60, 82],[82, 60, 83],[74, 57, 79]]

    test = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]

    ys = cl.OrderedDict()

    for i in range(len(name_list)):
        data = cl.OrderedDict()
        data["BWH"] = BWH[i]
        data["height"] = height[i]

        data["test"] = test[i]

        ys[name_list[i]] = data

    print("{}".format(json.dumps(ys, indent=None)))

    fw = open('test.json', 'w')
    json.dump(ys, fw, indent=4)



if __name__=='__main__':
    main()
